from setuptools import setup, find_packages
from pathlib import Path

readme = Path(__file__).parent / "README.md"
long_description = readme.read_text() if readme.exists() else ""

setup(
    name="idk-command",
    version="0.0.2",
    description="A command-line tool for generating Linux commands based on user queries.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Loyston Pais",
    author_email="loyston500@gmail.com",
    url="https://github.com/loystonpais/idk-command", 
    packages=find_packages(),
    py_modules=["idk"],
    install_requires=[
        "requests",  
    ],
    entry_points={
        "console_scripts": [
            "idk=idk:main",  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
