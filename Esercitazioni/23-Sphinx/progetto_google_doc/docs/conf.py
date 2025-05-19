import os
import sys
sys.path.insert(0, os.path.abspath('../modulo'))
# python-2025\Esercitazioni\23-Sphinx\progetto_google_doc\modulo
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Per supportare Google-style
    'sphinx_autodoc_typehints'
]

# html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'