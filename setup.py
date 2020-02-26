import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_barloader", # Replace with your own username
    version="1.1.1",
    author="Andy Bui",
    author_email="andy.bui2001@gmail.com",
    description="Simple barloading graphic generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andybui01/simple_barloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)