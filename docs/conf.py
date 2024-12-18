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

from importlib import metadata

PACKAGE_VERSION = metadata.version('pubpypack-harmony-ricardo-zambrano')
version = release = PACKAGE_VERSION

import os

if os.environ.get("READTHEDOCS") == "True":
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).parent.parent
    PACKAGE_ROOT = PROJECT_ROOT / "src" / "imppkg"

    def run_apidoc(_):
        from sphinx.ext import apidoc
        apidoc.main([
            "--force",
            "--implicit-namespaces",
            "--module-first",
            "--separate",
            "-o",
            str(PROJECT_ROOT / "docs" / "reference"),
            str(PACKAGE_ROOT),
            str(PACKAGE_ROOT / "*.c"),
            str(PACKAGE_ROOT / "*.so"),
        ])
    
    def setup(app):
        app.connect('builder-inited', run_apidoc)