============
File Structure
-------------

The project has the following structure::

    jekyll-blog-repository/
    ├── _data/
    ├── _includes/
    ├── _layouts/
    ├── _posts/
    ├── _sass/
    ├── assets/
    ├── docs/
    │   ├── source/
    │   │   ├── conf.py
    │   │   ├── index.rst
    │   │   ├── about.rst
    │   │   └── ...
    │   ├── Makefile
    │   └── make.bat
    ├── docs_env/
    ├── _config.yml
    ├── about.md
    ├── categories.md
    ├── community.md
    ├── contact-successful.md
    ├── contact.md
    ├── index.html
    ├── Gemfile
    ├── jekyll-yamt.gemspec
    ├── utterances.json
    ├── .gitignore
    ├── .gitattributes
    ├── README.md
    ├── ISSUE_TEMPLATE.md
    ├── PULL_REQUEST_TEMPLATE.md
    ├── CODE_OF_CONDUCT.md
    └── ...

Configuration Options
-------------------

In ``_config.yml``, you can configure:
- **Site settings**: Title, description, base URL, and more.
- **Theme settings**: Specify the theme (e.g., "Jekyll-YAMT") and its options.
- **Plugins**: Add or configure Jekyll plugins for extended functionality.
- **Collections and data**: Define custom collections or provide site data.

In ``conf.py``, you can configure:
- **Project information**: Set the title, author, and version for your documentation.
- **Extensions**: Enable or disable Sphinx extensions for documentation features.
- **HTML theme**: Choose a theme for the ReadTheDocs-hosted site.
- **Paths**: Specify the location of templates and static files.


Project Information
^^^^^^^^^^^^^^^^^
.. code-block:: python

    project = 'OSSW24_Team6'
    copyright = '2024, Team6'
    author = 'Chaeyoung KIM, Min YOO, Beomjun KIM'
    version = '0.1'
    release = '0.1.0'
