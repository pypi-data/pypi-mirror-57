import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PPINot4Py", # Replace with your own username
    version="0.0.2",
    author="Alejandro Gomez Caballero",
    author_email="agcaballero@us.es",
    description="Python version of PPINot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isa-group/ppinot4py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)