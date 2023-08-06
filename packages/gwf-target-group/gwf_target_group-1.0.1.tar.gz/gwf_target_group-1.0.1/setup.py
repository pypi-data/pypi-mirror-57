
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gwf_target_group",
    version="1.0.1",
    author="Jörn Bethune",
    description="A wrapper for gwf for easy generation of output file paths",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jbethune/gwf_target_group",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['gwf>=1.6.0'],
)
