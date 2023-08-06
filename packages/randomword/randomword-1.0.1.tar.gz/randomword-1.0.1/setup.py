import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    

setuptools.setup(
    name='randomword',
    version='1.0.1',
    description='A simple python library that gives you a certain amount of random words.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Hexiro/randomword/',
    author='Hexiro',
    author_email='realhexiro@gmail.com',
    packages=setuptools.find_packages(),
    license='MIT',
    python_requires='>=3.6',
    )
