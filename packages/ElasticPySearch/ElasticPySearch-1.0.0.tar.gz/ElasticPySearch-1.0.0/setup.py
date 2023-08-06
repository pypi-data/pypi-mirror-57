import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ElasticPySearch", # Replace with your own username
    version="1.0.0",
    author="Sajan Kumar Bhagat",
    author_email="bhagat.sajan0073@example.com",
    description="Elastic Search Python Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bhagatsajan0073/elastipysearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
