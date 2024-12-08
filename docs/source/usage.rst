Usage
=====

Building Documentation
--------------------

To build the documentation:

1. Activate your virtual environment:

   .. code-block:: bash

      source docs_env/bin/activate  # On Windows: docs_env\Scripts\activate

2. Navigate to the docs directory:

   .. code-block:: bash

      cd docs

3. Build the HTML:

   .. code-block:: bash

      make html

The built documentation will be in ``_build/html/``.

Updating Documentation
--------------------

1. Edit the relevant .rst files
2. Rebuild the documentation:

   .. code-block:: bash

      make clean
      make html

3. View your changes in ``_build/html/index.html``
