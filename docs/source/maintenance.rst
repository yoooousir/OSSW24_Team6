Maintenance
==========

Documentation Updates
-------------------

Regular Updates
^^^^^^^^^^^^^
* Review documentation monthly
* Update version numbers
* Check for broken links
* Verify code examples
* Update screenshots if needed

Version Control
-------------

Git Commands
^^^^^^^^^^
.. code-block:: bash

    # Update documentation
    git add .
    git commit -m "Update documentation: [describe changes]"
    git push origin main

Build Verification
----------------

Always test your documentation locally before pushing:

.. code-block:: bash

    make clean
    make html
    # Check _build/html/index.html in your browser
