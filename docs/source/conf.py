# -*- coding: utf-8 -*-
# pylint: skip-file
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
import pathlib
from datetime import datetime

sys.path.insert(0, os.path.abspath("../.."))  # nopep8
sys.path.insert(0, os.path.abspath("../../spydrnet_physical"))  # nopep8
sys.path.insert(0, os.path.abspath("./extensions"))  # nopep8
import spydrnet as sdn
import spydrnet_physical as sdnphy
from sphinx_gallery.sorting import ExplicitOrder
from sphinx_gallery.sorting import FileNameSortKey


# -- Project information -----------------------------------------------------

project = "SpyDrNet-Physical"
copyright = "2021, University of Utah"
author = "The Laboratory for NanoIntegrated Systems (LNIS)"

# The short X.Y version
version = sdnphy.__version__
# The full version, including alpha/beta/rc tags
release = sdnphy.__release__

numfig = True


# -- General configuration --

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.programoutput",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.graphviz",
    "sphinx.ext.githubpages",
    "sphinxcontrib_hdl_diagrams",
    "sphinx_gallery.gen_gallery",
    "autodocsumm",
    # 'helloworld',
    # 'sphinxcontrib.needs',
    # 'sphinxcontrib.test_reports',
    # 'sphinxcontrib.plantuml',
]


html_theme_options = {
    "light_css_variables": {
        "font-stack": "Lato, sans-serif",
        "font-stack--monospace": "Consolas, monospace",
        "code-font-size": "87.25%",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/ganeshgore/spydrnet-physical",
            "html": f"""
            <div>Last updated {datetime.now().strftime("%d/%m/%y %H:%M")}</div>
            <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
            </svg>
        """,
            "class": "",
        },
    ],
}


# generate autosummary pages
autosummary_generate = True
autodoc_member_order = "bysource"
autodoc_default_options = {
    "autosummary": True,
}

graphviz_output_format = "svg"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of prefixs that are ignored when creating the module index. (new in Sphinx 0.6)
modindex_common_prefix = ["spydrnet_physical."]

# doctest_global_setup = "import spydrnet_physical as sdnphy"

# treat ``x, y : type`` as vars x and y instead of default ``y(x,) : type``
napoleon_use_param = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = "furo"


# Adding custom CSS stylesheet
html_css_files = [
    "custom.css",
]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
    "navigation_with_keys": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "SpyDrNet-Physical"
verilog_diagram_yosys = "system"


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    "papersize": "letterpaper",
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    "figure_align": "H",
    # Oneside (remove blank pages)
    #
    "extraclassoptions": "openany,oneside",
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "reference/index",
        "spydrnet_reference.tex",
        "SpyDrNet Reference",
        "BYU Configurable Computing Lab",
        "manual",
    ),
]

latex_appendices = ["tutorial"]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "spydrnet", "SpyDrNet Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
# texinfo_documents = [
#     (master_doc, 'SpyDrNet', 'SpyDrNet-Physical Documentation',
#     author, 'SpyDrNet-Physical', 'One line description of project.',
#      'Miscellaneous'),
# ]


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
epub_exclude_files = ["search.html"]

rst_epilog = f"""
.. |sdnphy| replace:: SpyDrNet-Physical
"""

sphinx_gallery_conf = {
    # path to your example scripts
    "examples_dirs": [
        os.path.join("..", "..", "examples", "basic"),
        os.path.join("..", "..", "examples", "sdnphy_mib"),
        os.path.join("..", "..", "examples", "OpenFPGA_basic"),
        os.path.join("..", "..", "examples", "OpenFPGA_Floorplanning"),
        os.path.join("..", "..", "examples", "OpenFPGA_clock_tree"),
        os.path.join("..", "..", "examples", "OpenFPGA_tiling"),
        os.path.join("..", "..", "examples", "OpenFPGA_rendering"),
        os.path.join("..", "..", "examples", "OpenFPGA_config"),
        os.path.join("..", "..", "examples", "circuit_builder"),
    ],
    # path to where to save gallery generated output
    "gallery_dirs": [
        "auto_basic",
        "auto_sdnphy_mib",
        "auto_openfpga_basic",
        "auto_openfpga_floorplanning",
        "auto_openfpga_clock_tree",
        "auto_openfpga_tiling",
        "auto_openfpga_rendering",
        "auto_openfpga_config",
        "auto_circuit_builder",
    ],
    "remove_config_comments": True,
    "filename_pattern": "/*.py",
    "capture_repr": (),
    "within_subsection_order": FileNameSortKey,
}


def CollectRst():
    verilog_dir = os.path.join(
        "..", "..", "spydrnet_physical", "support_files", "sample_verilog"
    )
    out_dir = os.path.join("auto_sample_verilog")
    pathlib.Path(out_dir).mkdir(parents=True, exist_ok=True)
    index_fp = open(os.path.join(out_dir, "index.rst"), "w")
    index_fp.write(
        "Sample Verilog Netlists\n======================="
        + "\n\n.. toctree::\n   :glob:\n   :maxdepth: 2\n\n   ./*"
    )
    for subdir, dirs, files in os.walk(verilog_dir):
        for file in files:
            if "std_genlib" in file:
                continue
            if file.endswith(".v"):
                basename = os.path.splitext(os.path.basename(file))[0]
                filename = os.path.join(subdir, file)
                # print(f"subdir {subdir}")
                # print(f"file {file}")
                # print(f"basename {basename}")
                # print(f"out_dir {out_dir}")
                # print(f"filename {filename}")
                # print(os.path.join(out_dir, file+".rst"))
                # print()
                with open(os.path.join(out_dir, basename + ".rst"), "w") as fp:
                    fp.write(
                        f'.. _sample_verilog_{basename.replace(" ","_")}:\n'
                        + f"\n"
                        + f"{basename}\n"
                        + f"=================\n\n"
                        + f".. hdl-diagram:: ../{filename}\n"
                        + f"   :type: netlistsvg\n"
                        + f"   :align: center\n"
                        + f"\n\n"
                        + f".. literalinclude:: ../{filename}\n"
                        + f"   :language: verilog\n"
                    )
    index_fp.close()


SDN_DOC_SOURCE = os.path.dirname(sdn.__file__) + "/../docs/source/"
try:
    os.symlink(SDN_DOC_SOURCE, "_SDN_DOC_SOURCE")
except:
    pass
exclude_patterns.append("_SDN_DOC_SOURCE/**")

CollectRst()


# ========
# Headings
# ========
#
# Headings
# ========
#
# Heading 3
# ---------
#
# Heading 4
# ^^^^^^^^^
#
# Heading 5
# ~~~~~~~~~
#
# Heading 6
# *********
