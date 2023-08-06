import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zdktestpac",
    version="0.0.4",
    author="ZDK",
    author_email="zhoudk@ihep.ac.cn",
    description="A test package for GBM data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZDKplayer/test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.x',
)
