# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Gesundai'
copyright = '2024, Gesundai'
author = 'Gesundai'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os 
import sys
print(sys.path)
sys.path.insert(0, os.path.abspath("./code"))

version = '0.3.17'  # Current version of your project
release = '1.0.0'  # Full release version, including alpha/beta/rc tags


extensions = ['myst_parser', 'sphinx.ext.autodoc', 'sphinx.ext.duration', 'sphinx.ext.autosummary', "sphinx_changelog", "sphinxcontrib.versioning"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
