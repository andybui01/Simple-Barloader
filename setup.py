import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='simple_barloader',  
     version='1.0.1',
     scripts=['simple_barloader'] ,
     author="Andy Bui",
     author_email="andy.bui2001@gmail.com",
     description="Bar loading graphic generator",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/andybui01/simple_barloader/",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )