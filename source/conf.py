# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Resignar-se ao Real'
copyright = '2023, Gustavo Costa'
author = 'Gustavo Costa'
release = '1.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

epub_show_urls = 'footnote'

# https://alabaster.readthedocs.io/en/latest/customization.html#theme-options
html_theme_options = {
    'logo': 'logo.png',
    'github_user': 'noah-art3mis',
    'github_repo': 'alabaster',
    'description': 'Text blurb about your project, to appear under the logo.',
    'fixed_sidebar': 'true',
}
