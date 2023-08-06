import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sps30",
    version="0.1.4",
    scripts=['sps30/__main__.py', 'sps30.py'],
    author="Feyzi Kesim",
    author_email="feyzikesim@gmail.com",
    description="Python3 I2C Driver & Application for SPS30 PM Sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feyzikesim/sps30",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
