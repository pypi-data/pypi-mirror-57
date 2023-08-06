import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="marketanalyst", # Replace with your own username
    version="0.1.0",
    author="Sayanta Basu",
    author_email="sayanta@agrud.com",
    description="This is wrapper for marketanalyst api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['requests','pandas','numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)