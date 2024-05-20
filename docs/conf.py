"""Configuration file for Sphinx.

Useful links:
configuration documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from __future__ import annotations

import os
import pathlib
import sys

# Development mode (if there are a 'DEV' environment variable)
dev_mode = "DEV_MODE" in os.environ


# #region Paths to search by modules to generate documentation

paths = [
    "../",
    "../src/",  # Require to 'examples/' be able to import this package

    # Need this line to Sphinx be able to import 'gi' module
    "/usr/lib/python3/dist-packages/",
]

for path in paths:
    resolved_path = pathlib.Path.resolve(pathlib.Path(path))
    sys.path.insert(0, str(resolved_path))

# #endregion


# #region Project information

project = "gtk_simple_loader"
copyright = "2024, Lucas Vasco"  # noqa: A001
author = "Lucas Vasco"
version = "0.0.1"
release = "0.0.1"
language = "en"

homepage = "https://github.com/LucasAVasco/gtk_simple_loader"
repository_tree_page = "https://github.com/LucasAVasco/gtk_simple_loader/tree/main"

# #endregion


# #region General configuration

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv", "venv"]

rst_prolog = ""

rst_epilog = f"""
.. _homepage: {homepage}
.. _Homepage: {homepage}
"""

# #endregion


# #region Extensions configuration

extensions = [
    # Automatic documentation generation
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",

    # Images and diagrams
    "sphinx.ext.imgconverter",
    "sphinx.ext.inheritance_diagram",

    # Documentation formatting
    "sphinx.ext.napoleon",

    # Integration with external pages
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",

    # Debug
    "sphinx.ext.coverage",

    # Others
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
]

autodoc_default_options = {
    "members": True,
    "special-members": True,
    "show-inheritance": True,
    "private-members": False,
    "inherited-members": False,
}

autodoc_typehints = "both"

autosummary_context = {
    "project_homepage": homepage,
    "project_tree_page": repository_tree_page,
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

extlinks = {
    "issue": (homepage + "/issues/%s", "issue %s"),
    "pull": (homepage + "/pull/%s", "pull %s"),
}

# #endregion


# #region HTML options

html_theme = "sphinxdoc"
html_static_path = ["_static"]

if not dev_mode:
    html_show_sourcelink = False  # If True, shows the reST source

# #endregion
