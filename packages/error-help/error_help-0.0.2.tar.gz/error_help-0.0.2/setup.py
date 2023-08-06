import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="error_help", # Replace with your own username
    version="0.0.2",
    author="Thomas C",
    author_email="topcat.thomas.phone@outlook.com",
    description="A small package to automate searching your errors.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/topcatthomas/errorHelp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)