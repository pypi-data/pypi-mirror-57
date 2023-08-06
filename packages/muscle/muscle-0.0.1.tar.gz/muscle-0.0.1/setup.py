import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="muscle", # Replace with your own username
    version="0.0.1",
    author="ithai Levi",
    author_email="randomlinesofcode@gmail.com",
    description="Strength Training Program Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlofc/chalk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
