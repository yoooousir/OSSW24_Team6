# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme

# Project information
project = 'ossw24_team6'
copyright = '2024, Chae-young KIM'
author = 'Chae-young KIM'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

# Language settings
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False
gettext_uuid = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'display_version': True,
    'style_external_links': True,
    'prev_next_buttons_location': 'both',
    # Add your Jekyll site URL here
    'extra_nav_links': {
        'Project Website': 'https://ossw24_team6.github.io'
    }
}
