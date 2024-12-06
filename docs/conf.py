# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pubpypack-harmony-ricardo-zambrano'
copyright = '2024, Ricardo Zambrano'
author = 'Ricardo Zambrano'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#> RZ: These extensions for sphinx-apidoc are not enabled by default [p. 139]
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
    'sphinx.ext.napoleon',  # For Google or NumPy-style docstrings
    # "sphinx.ext.viewcode",  # Optional, but helpful to show source code
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

#> Not from the book:

# Autodoc configuration
autodoc_typehints = "description"  # Place type hints in the description
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
