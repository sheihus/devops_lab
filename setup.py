import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='monitor',
                 version='0.1',
                 scripts=['monitor'],
                 author="Andrei Sheihus",
                 author_email="sheihus@gmail.com",
                 description="Monitor utility package",
                 long_description=long_description,
                 url="https://github.com/sheihus/monitor",
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent"],)
