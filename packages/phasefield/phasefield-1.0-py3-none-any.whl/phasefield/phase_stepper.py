#!/usr/bin/python
"""
Only contains phase base class currently
"""

from __future__ import print_function

import math
import numpy as np

import ufl
import os

from phasefield.external import External

from ufl import as_vector, Coefficient, dot, dx, grad, inner, Identity, SpatialCoordinate, TestFunction, TrialFunction, tr, transpose, replace
from ufl.algorithms import expand_indices
from ufl.algorithms.analysis import extract_arguments_and_coefficients
from ufl.algorithms.apply_derivatives import apply_derivatives
from ufl.algorithms.apply_algebra_lowering import apply_algebra_lowering

def formSum(form):
    """
    Takes a ufl form if it's a list sums it if not just returns the original form
    """
    try:
        return sum(form)
    except TypeError:
        return form

class dirichletMod:
    """
    Takes the possibly time dependend boundary conditions that the user has specified,
    and adds on the correct natural boundary conditions for u
    """
    def __init__(self, fun, dimRangePhase, space):
        self.fun = fun
        self.dimRangePhase = dimRangePhase
        self.space = space
        self.x = SpatialCoordinate(space)

    def __call__(self,t):
        #transform dictionary into a list
        transfun = [[v,k] for k, v in self.fun(t, self.x).items()]
        return [External.dirichletBC(self.space, self.dimRangePhase*[None]+transfun[i][0],
                            transfun[i][1]) for i in range(0,len(transfun))]

class PhaseStepper:
    """
    Base class for phasefield computations with timestepping
    auxParam has, dirichlet, storage, solver, orderFe, solverParameters, mono
    """
    def __init__(self, uflModel, solverParameters = {"newton.tolerance":1e-8,
                                                     "newton.linear.tolerance":1e-10,
                                                     "newton.verbose":False,
                                                     "newton.linear.verbose":False},
                 storage = "fem", solver = "gmres", orderFe = 1, mono = True, constrained = False ):

        self._debug = True

        # Check that if an obstacle potential is used the storage is consistent
        if(constrained == True and storage != "istl"):
            raise ValueError("Storage must be set to istl when using obstacle potential")

        self._uflModel = uflModel
        self.auxParam = {'solverParameters':solverParameters, 'storage':storage,
                         'solver':solver, 'orderFe':orderFe, 'mono':mono, 'constrained':constrained}

        self.gridView = External.mesh(self._uflModel.sharpCls.omega)

        self.dimRange = self._uflModel.inspectDict['dimRangePhase'] + self._uflModel.inspectDict['dimRangeBalance']


        # sets up all relevenat schemes models etc for monolithic scheme
        if self.auxParam['mono']:
            self.setupMono()
        else:
            self.setupCoupled()

        # set up the initial data
        self.initialInterpolate()

        # default indicator and phasefield parameters for adaptive grid
        self.indicator = 0
        for i in range(0, self._uflModel.inspectDict['dimRangePhase']):
            self.indicator = self.indicator + dot(grad(self.solution[i]), grad(self.solution[i]))

        # in format [refineTolerance, coarsenTolerance, minLevel, maxLevel]
        self.defaultRefine = [1.4, 1.2, 4, 12]

        try:
            from dune.fem.function import levelFunction, partitionFunction
            self.saveStep = self._uflModel.sharpCls.saveStep
            self.fileBase = self._uflModel.sharpCls.__name__ \
                            if not hasattr(self._uflModel.sharpCls,"fileBase") \
                            else self._uflModel.sharpCls.fileBase
            self.dimPhase = self._uflModel.inspectDict['dimRangePhase']
            self.dimBulk  = self._uflModel.inspectDict['dimRangeBalance']
            func  = [["phi_"+str(i),self.solution[i]] for i in range(self.dimPhase)]
            func += [["u_"+str(i),self.solution[i+self.dimPhase]] for i in range(self.dimBulk)]
            self.vtk = self.gridView.sequencedVTK(self.fileBase,
                                               pointdata=[self.solution], # dict(func),
                                               celldata=[levelFunction(self.gridView)])
            self.saveTime = None
        except AttributeError or ImportError:
            self.vtk = None


    #### mynote: same for epsilon and dt
    @property
    def time(self):
        return float(self._uflModel.time)
    @time.setter
    def time(self,value):
        self._uflModel.time.assign(value)
    @property
    def dt(self):
        return float(self._uflModel.dt)
    @dt.setter
    def dt(self,value):
        self._uflModel.dt.assign(value)
    @property
    def epsilon(self):
        return float(self._uflModel.eps)
    @epsilon.setter
    def epsilon(self,value):
        self._uflModel.eps.assign(value)

    def setupMono(self):
        # space requires auxParam and the range of the problem
        self.spc = self.setupSpace(self.gridView, self.dimRange)
        # solution at new and old timsteps
        self.solution = External.discreteFunction(self.spc, "solution")
        self.solutionN = External.discreteFunction(self.spc, "solutionN")

        self.x = SpatialCoordinate(self.spc)
        # *********************************** UFL Specific maybe new class? ***************
        # if smooth this will be coefficient otherwise given as initial fucntion
        self.trialFull = TrialFunction(self.spc)
        coeffN = self.solutionN

        # create coefficient vector of size dimRange
        # coefficient for implicit terms
        imCoeff = self.solution # Coefficient(self.spc)

        self.vFull = TestFunction(self.spc)

        if self._uflModel.inspectDict['numPhases'] == 1:
            phi = ufl.as_vector([imCoeff[0]])
            phiN = ufl.as_vector([coeffN[0]])
            vPhi = ufl.as_vector([self.vFull[0]])

        elif self._uflModel.inspectDict['dimRangePhase'] !=0:
            phi = ufl.as_vector([imCoeff[0], 1-imCoeff[0]])
            phiN = ufl.as_vector([coeffN[0], 1-coeffN[0]])
            vPhi = ufl.as_vector([self.vFull[0]])

        else:
           phi = 0
           phiN = 0
           vPhi = 0

        if self._uflModel.inspectDict['dimRangeBalance'] != 0:
            u = ufl.as_vector([imCoeff[j] for j in range(self._uflModel.inspectDict['dimRangePhase'], self.dimRange)])
            un = ufl.as_vector([coeffN[j] for j in range(self._uflModel.inspectDict['dimRangePhase'], self.dimRange)])
            vU = ufl.as_vector([self.vFull[j] for j in range(self._uflModel.inspectDict['dimRangePhase'], self.dimRange)])
        else:
            u = 0
            un = 0
            vU = 0

        #*****************************************************************************
        # pass in phi,phin,u,un,vphi,vnphi to setup so I can create spaces in here
        form = self._uflModel.setupPhase(phi, phiN, u, un, vPhi, vU, self.x)

        for row in form:
            print("##############")
            print(str(row[0]))
            print("####")
            print(str(row[1]))
            print("##############")


        #sums the lhs or rhs respectively to get the ufl forms
        lhs = sum(row[0] for row in form)
        rhs = sum(row[1] for row in form)

        # replace coeff with [trialFUll]
        # should only have to do this once when the implicit and explicit are on correct sides
        # mynote: why is imCoeff used instead of trialFull?
        lhs = replace(lhs,{imCoeff:self.trialFull})
        rhs = replace(rhs,{imCoeff:self.trialFull})
        print(self.checkDependencies(lhs-rhs))

        # setup the dirichlet boudnary conditions needs to be done after space but before model
        self.setupDirichlet()

        self.scheme = self.setupScheme(lhs,rhs)

        # residual unused if smooth well is used
        self.res = External.discreteFunction(self.spc, "residual")
        self.lower_lim = self.spc.interpolate(self.spc.dimRange*[-1.],
                                              name = "lower_lim")
        self.upper_lim = self.spc.interpolate(self.spc.dimRange*[0.],
                                              name = "upper_lim")


    def setupDirichlet(self):
        """
        set the domain of dirichlet ot the correct thing
        alter the dirichlet conditions to ensure that the phase field variables have None
        without this and setting auxParam['dirichlet'] = dirichlet
        the lise would be the wrong size
        """

        if "dirichlet" in dir(self._uflModel.sharpCls) and not self.auxParam['mono']:
            self.auxParam['dirichlet'] = dirichletMod(self._uflModel.sharpCls.dirichlet, 0,
                                                      self.spc_u)
            self.debug("Dirichlet boundary conditions for u in coupled scheme")

        elif "dirichlet" in dir(self._uflModel.sharpCls):
            self.auxParam['dirichlet'] = dirichletMod(self._uflModel.sharpCls.dirichlet,
                                                      self._uflModel.inspectDict['dimRangePhase'],
                                                      self.spc)
            self.debug("Dirichlet boundary conditions for u")

    def setupCoupled(self):
        from dune.fem.space import product as productSpace
        print(self._uflModel.inspectDict['dimRangeBalance'],
              self._uflModel.inspectDict['dimRangePhase'])
        self.spc_u = self.setupSpace(self.gridView,
                                     self._uflModel.inspectDict['dimRangeBalance'] )

        self.spc_phi = self.setupSpace(self.gridView, self._uflModel.inspectDict['dimRangePhase'] )

        # TODO: use External
        self.spc = productSpace(self.spc_phi, self.spc_u, components=["phi", "u"])
        self.x = SpatialCoordinate(self.spc)
        # TODO: create solution vectors at n+1 and previous time step
        # TODO: use External
        self.solution = self.spc.interpolate(self.spc.dimRange*[0],name = "solution")
        self.solution_n = self.spc.interpolate(self.spc.dimRange*[0], name = "solution_n")
        self.lower_lim = self.spc.interpolate(self.spc.dimRange*[0], name = "lower_lim")
        self.zeros = self.spc_phi.interpolate([0,],name="zeros")

        # define initial trial and test functions all defined in terms of separate spaces
        self.v_u = TestFunction(self.spc_u)
        self.v_phi = TestFunction(self.spc_phi)

        self.u = TrialFunction(self.spc_u)
        self.phi = TrialFunction(self.spc_phi)

        self.u_c = self.solution.u # Coefficient(self.spc_u)

        # implicit phi
        self.phi_c = self.solution.phi # Coefficient(self.spc_phi)

        # explicit phi
        # TODO: add time derivative in bulk
        self.phiN = self.solution_n.phi # Coefficient(self.spc_phi)

        if self._uflModel.inspectDict['numPhases'] == 1:
            form = self._uflModel.setupPhase(as_vector([self.phi_c[0]]),
                                             as_vector([self.phiN[0]]), self.u_c, self.u_c,
                                             self.v_phi, self.v_u, self.x)
        else:
            form = self._uflModel.setupPhase(as_vector([self.phi_c[0],1-self.phi_c[0]]),
                                             as_vector([self.phiN[0], 1-self.phiN[0]]),
                                             self.u_c, self.u_c, self.v_phi, self.v_u, self.x)
        # This has phi_c Coefficient and u a trial fuction in it
        self.lhsU = form[0][0]
        self.rhsU = replace(form[0][1], {self.u_c:self.u})
        self.rhsU = replace(self.rhsU, {self.phiN:self.phi_c})

        self.lhsPhi = form[1][0]
        self.lhsPhi = replace(self.lhsPhi, {self.phi_c:self.phi})
        self.lhsPhi = replace(self.lhsPhi, {self.phiN:self.solution_n.phi})

        # currently pass back as_vectpr([self.phi_c[0]])
        formPass = form[1][1]

        self.rhsPhi = form[1][1]

        self.rhsPhi = replace(self.rhsPhi, {self.phi_c:self.phi})
        self.rhsPhi = replace(self.rhsPhi, {self.phiN:self.phi})

        # TODO: use External
        self.rhs = self.zeros.copy()

        self.scheme = [None,None]
        self.scheme[1] = self.setupScheme(self.lhsPhi,self.rhsPhi)
        self.setupDirichlet()
        self.scheme[0] = self.setupScheme(self.lhsU,self.rhsU)

    def setupSpace(self, gridView, dimRange):
        self.debug("storage set as" + str(self.auxParam['storage']))
        return External.discreteFunctionSpace(self.gridView, dimRange=dimRange, order=self.auxParam['orderFe'],
                             storage=self.auxParam['storage'])

    def setupScheme(self, lhs, rhs):
        return External.scheme( lhs==rhs, self.auxParam.get('dirichlet',lambda t:None)(self._uflModel.time + self._uflModel.dt),
                               solver = self.auxParam['solver'],
                               parameters = self.auxParam['solverParameters'])

        # compute solution at next timestep
    def nextTime(self):
        """
        Compute solution at next time step and adapt grid.
        """
        # Currently won't work properly if constrained and coupled
        self.output()
        if self.auxParam['constrained']:
            self.nextTimeOBSTACLE()
        elif self.auxParam['mono']:
            self.nextTimeSMOOTH()
        else:
            self.nextTimeCoupled()
        self._uflModel.time.assign(self._uflModel.time + self._uflModel.dt)
        self.output()

    def output(self):
        if self.vtk is not None:
            if self.saveTime is None:
                self.vtk()
                self.saveTime = 0
            if self.saveTime <= self.time:
                self.vtk()
                self.saveTime += self.saveStep

    def nextTimeOBSTACLE(self):
        from dune.generator import algorithm, path
        from dune.fem.operator import linear
        zeros = self.spc.interpolate([0,],name="zeros")

        self.solutionN.assign(self.solution)
        self.scheme(zeros, self.res)

        matrix = linear(self.scheme).as_istl

        lower_lim = self.spc.interpolate(self.spc.dimRange*[-1], name = "lower_lim")
        upper_lim = self.spc.interpolate(self.spc.dimRange*[0], name = "upper_lim")

        solveObstacleProblemByTNNMG = algorithm.run('solveObstacleProblemByTNNMG',
                                                    path(__file__) + '/tnnmg.cc', self.gridView,
                                                    matrix, self.solution.as_istl,
                                                    self.res.as_istl,
                                                    lower_lim.as_istl,
                                                    upper_lim.as_istl)

        for i in range(len(self.solution.as_istl)):
                self.solution.as_istl[i] *= -1

    def nextTimeSMOOTH(self):
        External.assign(self.solution,self.solutionN)
        External.solve(self.scheme,self.solution)

    def nextTimeCoupled(self):
        from dune.generator import algorithm, path
        from dune.fem.operator import linear

        self.solution_n.phi.assign(self.solution.phi)
        self.scheme[0].solve(target=self.solution.u)
        self.solution_n.u.assign(self.solution.u)

        #assemble rght hand side
        self.scheme[1](self.zeros,self.rhs)
        matrix = linear(self.scheme[1]).as_istl

        self.lower_lim.assign(self.solution_n)

        for i in range(len(self.lower_lim.phi.as_istl)):
            self.lower_lim.phi.as_istl[i] *= -1

        # scheme[1].solve(target=solution.phi)

        solveObstacleProblemByTNNMG = algorithm.run('solveObstacleProblemByTNNMG',
                                                    path(__file__)+'/tnnmg.cc',
                                                    self.gridView, matrix,
                                                    self.solution.phi.as_istl,
                                                    self.rhs.as_istl,
                                                    self.lower_lim.phi.as_istl,
                                                    self.zeros.as_istl)

        for i in range(len(self.solution.phi.as_istl)):
            self.solution.phi.as_istl[i] *= -1

    def initialInterpolate(self):
        """
        initialize solution for start of simulation
        """

        x = SpatialCoordinate(self.spc)
        try:
            bulkInitial = self._uflModel.sharpCls.initial(x)[1]
        except IndexError:
            bulkInitial = []
        External.interpolate(self.solution, as_vector([self._uflModel.sharpCls.initial(x)[0][0]] + bulkInitial))

    def initialRefine(self, numRefine):
        """
        Does initial refinement of the trid
        """

        External.globalRefine(self.gridView,numRefine)
        self.initialInterpolate()

    def adapt(self):
        External.adaptMesh([self.solution],self.indicator, *self.defaultRefine)

    def initialAdapt(self, numRefine):
        for i in range(0, numRefine):
            self.adapt()
            self.initialInterpolate()

    def gridSetup(self, numGlobalRefine, numLocalRefine):
        self.initialRefine(numGlobalRefine)
        self.initialAdapt(numLocalRefine)

    def checkDependencies(self,form):
        from ufl.algorithms.formtransformations import compute_form_lhs
        v,u = form.arguments()
        form = compute_form_lhs(form)
        depend = self.dimRange*[None]
        scalarSpc = External.uflSpace(2)
        coeff = as_vector([Coefficient(scalarSpc) for i in range(self.dimRange)])
        print("'''''\n",coeff,"\n''''\n")
        for i in range(self.dimRange):
            depend[i] = self.dimRange*[False]
            testUnit = self.dimRange*[0]
            testUnit[i] = v[i] # self.vFull[i]
            form_i = replace(form, {v: as_vector(testUnit)})
            form_i = expand_indices(apply_derivatives(apply_algebra_lowering(form_i)))
            print("-----\nform_",i,str(form_i))
            form_i = replace(form_i, {u: coeff})
            form_i = (expand_indices(apply_derivatives(apply_algebra_lowering(form_i))))
            print("            ",str(form_i))
            _, test = extract_arguments_and_coefficients(form_i)
            print("###\n",[str(t) for t in test])
            print([(str(t),t in coeff) for t in test])
            for j in range(self.dimRange):
                depend[i][j] = coeff[j] in test
        return depend

    # if dubug flat is set outputs to log file
    def debug(self,output):
        try:
            if(self._debug):
                with open("pfout.log", "a") as myfile:
                    myfile.write(str(datetime.datetime.now()))
                    myfile.write(" - ")
                    myfile.write(output)
                    myfile.write("\n")
        except:
            pass
