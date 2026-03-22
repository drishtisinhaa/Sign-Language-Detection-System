# We have to install signLanguage folder as a local package 
from setuptools import setup,find_packages
# it'll look for the constructor file and whatever folder having the comnstructor file will be installed as a local package i.e. signLanguage
setup(
    name="Sign-Language-Recognition",
    version='0.1',
    author = "Drishti",
    author_email='drishti.sinha05@gmail.com',
    packages = find_packages(),
    install_requires = []
    
)