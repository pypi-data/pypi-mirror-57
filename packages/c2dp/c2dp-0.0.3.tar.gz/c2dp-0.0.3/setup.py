# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:59:16 2019

@author: bernsteind
"""

import setuptools

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
#files = ["things/*"]

setuptools.setup(
    name = "c2dp",
    version = "0.0.3",
    description = "a library for the civil court data project",
    author = "Dan Bernstein",
    author_email = "danbernstein94@gmail.com",
    #url = "",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = setuptools.find_packages()
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
   # package_data = {'package' : files },
    #'runner' is in the root.
   # scripts = ["runner"]
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 
