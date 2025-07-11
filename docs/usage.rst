Usage Guide
===========

Running Programs
----------------

Save your code in a file, e.g., ``example.modilang``, then run it with:

.. code-block:: bash

   python -m modilang example.modilang


Project Structure
-----------------

- ``interpreter.py``: Evaluates and executes code.
- ``parser.py``: Converts code into an AST.
- ``types.py``: Type system and validation.
- ``ast_nodes.py``: AST data model.
- ``cli.py``: Command-line runner.


Requirements
------------

Install dependencies:

.. code-block:: bash

   pip install -r requirements.txt
