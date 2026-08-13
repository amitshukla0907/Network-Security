'''The setup.py file is an example of a Python script used for packaging and distributing Python projects. It typically contains metadata about the project, such as its name, version, author, and dependencies. The setup.py file is executed using the Python interpreter to install the package and its dependencies.
Here is an example of a simple setup.py file:
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """Read the requirements from a file and return them as a list."""
    requirement_lst:List[str] = []
    try:
        
        with open('requirements.txt', 'r') as file:
            lines=file.readlines()
        #process each line
            for line in lines:
                requirement =(line.strip())
                          
                if requirement and requirement!= '-e .':
                
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
        
    return requirement_lst
print(get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Amit Shukla',
    author_email='amitshukla090703.email@example.com',
    description='A simple Network Security package',
    packages=find_packages(),
    install_requires=get_requirements()
)
