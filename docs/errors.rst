Error Messages and Troubleshooting
==================================

ModiLang uses some **intereresting** error messages, and here's what they mean(for the non indians out there):

.. list-table::
   :header-rows: 1
   :widths: 20 40 20 40

   * - Error Type
     - Message
     - Source
     - Explanation

   * - SyntaxError
     - Program must start with 'Bhaiyon aur Beheno'
     - parser.py
     - First line is not the expected opening statement

   * - SyntaxError
     - Program must end with 'Acche din aa gaye hai'
     - parser.py
     - Last line must be the official closing phrase

   * - SyntaxError
     - Congressi variable declaration
     - parser.py
     - Invalid format for variable declaration

   * - SyntaxError
     - Congressi SchemeLaunch syntax
     - parser.py
     - Malformed SchemeLaunch API call

   * - SyntaxError
     - Congressi statement: <line>
     - parser.py
     - Line did not match any known language construct

   * - TypeError
     - Variable '<name>' umeed <type>
     - interpreter.py
     - Mismatched type in variable declaration

   * - TypeError
     - Argument '<name>' umeed <type>
     - interpreter.py
     - Function argument did not match declared type

   * - TypeError
     - Unknown type: <type>
     - types.py
     - Unsupported type name

   * - NameError
     - Function <name> saala congressi
     - interpreter.py
     - Function is called but not defined

   * - ValueError
     - Argument count congressi
     - interpreter.py
     - Number of arguments does not match function definition

   * - ValueError
     - Congressi method <method>
     - interpreter.py
     - Invalid HTTP method in SchemeLaunch

   * - TypeError
     - Loop count must be int
     - interpreter.py
     - Non-integer expression given to loop

   * - SyntaxError
     - Invalid Agar / Desh ke liye syntax
     - parser.py
     - Conditional or loop body incorrectly formatted
