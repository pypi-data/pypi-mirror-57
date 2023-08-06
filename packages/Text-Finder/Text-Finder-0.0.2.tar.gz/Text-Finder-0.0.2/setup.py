import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Text-Finder", # Replace with your own username
    version="0.0.2",
    author="Athul Raj Suresh",
    author_email="theraj2003@gmail.com",
    description="Cuts text given a keyword and endpoint.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/petafam69/TextFinder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
