
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="soldaiSGA",
    version="1.0.0",
    author="Soldai Research",
    author_email="research@soldai.com",
    description="Soldai Simple Genetic Algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rviana-soldai/sga",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
