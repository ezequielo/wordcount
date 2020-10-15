import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordcount-ezequiel",
    version="1.0.0",
    author="E Rodriguez",
    author_email="ezequielra1@gmail.com",
    description="A simple wordcount app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ezequielo/wordcount",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)