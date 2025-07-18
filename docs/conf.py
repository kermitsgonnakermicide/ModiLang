import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'ModiLang'
author = 'Daksh Vohra'
release = '1.0'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
