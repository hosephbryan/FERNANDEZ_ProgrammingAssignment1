from setuptools import setup, find_packages

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

setup(
    name="ProgrammingAssignment1",
    version="0.1",
    description="Exploratory Data Analysis",
    author="Fernandez and Casia",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
    url="https://github.com/hosephbryan/FERNANDEZ_ProgrammingAssignment1",
)
