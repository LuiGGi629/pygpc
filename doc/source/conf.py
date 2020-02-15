# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
import pygpc
sys.path.insert(0, os.path.abspath('../../'))
sys.path.append(os.path.abspath('sphinxext'))

# -- Project information -----------------------------------------------------

project = u'pygpc'
# copyright = u'2018, Konstantin Weise, Benjamin Kalloch, Lucas Possner'
copyright = u'2020, Konstantin Weise'
# author = u'Konstantin Weise, Benjamin Kalloch, Lucas Possner'
author = u'Konstantin Weise'

# The short X.Y version
version = u'0.27.1.'

# The full version, including alpha/beta/rc tags
release = u'2020'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.imgmath',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_gallery.gen_gallery'
]

# configuration of sphinx gallery
sphinx_gallery_conf = {
    'examples_dirs': ['../../examples/introduction', '../../examples/gpc', '../../examples/algorithms', '../../examples/features'],   # path to your example scripts
    'gallery_dirs': ['auto_introduction', 'auto_gpc', 'auto_algorithms', 'auto_features']  # path to where to save gallery generated output

} #'default_thumb_file': '../../../pckg/media/pygpc_logo_git.png',

# 'IPython.sphinxext.ipython_directive',
# 'IPython.sphinxext.ipython_console_highlighting',
# 'sphinx.ext.intersphinx',

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

html_theme = 'scipy' #'sphinx_rtd_theme'
html_theme_path = ['_theme']
html_static_path = ['_static']

html_theme_options = {
    "edit_link": "true",
    "sidebar": "right",
    "pygpc_logo": "true",
    "rootlinks": [],
    "body_max_width": "1000"
}

pngmath_latex_preamble = r"""
\usepackage{color}
\definecolor{textgray}{RGB}{51,51,51}
\color{textgray}
"""
pngmath_use_preview = True
pngmath_dvipng_args = ['-gamma 1.5', '-D 96', '-bg Transparent']
html_short_title = 'pygpc'
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'pygpc_doc'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pygpcdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'extraclassoptions': 'openany,oneside',
    'babel': '\\usepackage[shorthands=off]{babel}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).

# latex_documents = [
    # (master_doc, 'pygpc.tex', u'pygpc Documentation',
     # u'Konstantin Weise, Benjamin Kalloch, Lucas Possner', 'manual'),
# ]

latex_documents = [
    (master_doc, 'pygpc.tex', u'Documentation of the pygpc package',
     u'Konstantin Weise', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

# man_pages = [
    # (master_doc, 'pygpc', u'pygpc Documentation',
     # [author], 1)
# ]

man_pages = [
    (master_doc, 'pygpc', u'Documentation of the pygpc package',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pygpc', u'Documentation of the pygpc package',
     author, 'pygpc', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
