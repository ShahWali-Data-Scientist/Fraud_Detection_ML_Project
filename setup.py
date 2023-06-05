from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='fraud_detection',
    version='1.0.0',
    author='Shah Wali',
    author_email='shahwalieng1@gmail.com',
    description='Fraud Detection Application',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)
