from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="phasefield",
    version="1.0",
    author="Matthew Collins and Andreas Dedner",
    author_email="a.s.dedner@warwick.ac.uk",
    description="Interface problem solver based on the phase-field methodology",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.dune-project.org/dune-fem/phasefield",
    packages = find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent"],
    install_requires=['UFL == 2017.1.0'],
    zip_safe = 0,
    package_data = {'': ['*.cc']}
  )
