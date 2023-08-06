import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scd30", 
    version="0.0.3",
    author="Laurenz Gamper",
    author_email="laurenzgamper@gmail.com",
    description="Python 3 library for the Sensirion SCD30 sensor",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/laurenzgamper/scd30",
    packages=['scd30'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pigpio',
        'crcmod',
    ],
    python_requires='>=3.6',
)
