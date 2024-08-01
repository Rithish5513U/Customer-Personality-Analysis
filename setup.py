from setuptools import find_packages, setup

def get_requirements(file):
    requirements=[]
    with open(file) as f:
        requirements=f.read().splitlines()
        if requirements[-1]=='-e .':
            requirements.pop()
        return requirements

setup(
    name="myproject",
    version="0.0.1",
    author="Rithish S",
    author_email="rithish.satish@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)