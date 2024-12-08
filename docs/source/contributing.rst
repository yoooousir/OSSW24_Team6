Contributing
===========

How to Contribute
----------------

1. Fork the Repository
   
   * Visit the GitHub repository
   * Click the "Fork" button
   * Clone your fork locally

2. Set Up Development Environment

   .. code-block:: bash

      git clone https://github.com/yoooousir/ReadTheDocs.git
      cd ReadTheDocs
      python -m venv docs_env
      source docs_env/bin/activate  # Windows: docs_env\Scripts\activate
      pip install -r docs/requirements.txt

3. Create a New Branch

   .. code-block:: bash

      git checkout -b feature/your-feature-name

4. Make Changes
   
   * Write your code
   * Add tests if needed
   * Update documentation

5. Submit Changes

   .. code-block:: bash

      git add .
      git commit -m "Description of changes"
      git push origin feature/your-feature-name

6. Create Pull Request
   
   * Go to GitHub
   * Click "New Pull Request"
   * Describe your changes

Code Style Guidelines
-------------------

* Follow PEP 8 guidelines
* Use meaningful variable names
* Add docstrings to functions
* Keep functions focused and small
