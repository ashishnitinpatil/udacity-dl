#!/usr/bin/env python

from setuptools import setup

setup(
    name = "udacity-dl",
    version = "1.1.5",
    description = "Download udacity course videos and resources",
    long_description = open("README.md").read(),
    author = "Ashish Patil (original author Ritesh Pradhan)",
    author_email = "ashishnitinpatil@gmail.com",
    url = "https://github.com/ashishnitinpatil/udacity-dl",
    packages = ["udacitydl"],
    entry_points = {"console_scripts":
                            ["udacity-dl = udacitydl.udacitydl:main"]},
    install_requires = ["mechanize", "beautifulsoup4", "argparse"],
)
