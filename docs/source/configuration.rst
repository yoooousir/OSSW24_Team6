Configuration
============

File Structure
-------------

The documentation project has the following structure::

    docs/
    ├── source/
    │   ├── conf.py
    │   ├── index.rst
    │   ├── about.rst
    │   └── ...
    ├── Makefile
    └── make.bat

Configuration Options
-------------------

In ``conf.py``, you can configure:

Theme Settings
^^^^^^^^^^^^^
.. code-block:: python

    html_theme = 'sphinx_rtd_theme'
    html_theme_options = {
        'navigation_depth': 4,
        'collapse_navigation': False,
        'sticky_navigation': True
    }

Project Information
^^^^^^^^^^^^^^^^^
.. code-block:: python

    project = 'OSSW24_Team6'
    copyright = '2024, Chaeyoung KIM'
    author = 'Chaeyoung KIM'
    version = '0.1'
    release = '0.1.0'
