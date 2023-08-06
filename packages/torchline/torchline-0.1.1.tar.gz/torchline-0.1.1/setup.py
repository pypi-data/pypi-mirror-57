from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name="torchline", # Replace with your own username
    version="0.1.1",
    author="marsggbo",
    author_email="csxinhe@comp.hkbu.edu.hk",
    description="A framework for easy to use Pytorch",
    long_description='...',
    long_description_content_type="text/markdown",
    url="https://github.com/marsggbo/torchline",
    packages=find_packages(exclude=("tests", "projects")),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
