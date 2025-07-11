Syntax Overview
===============

Program Structure
-----------------

- Start your program with::

    Bhaiyon aur Beheno

- End it with::

    Acche din aa gaye hai


Variable Declaration
--------------------
::

  Vikas hai <name>: <type> ka <value>

Example::

  Vikas hai desh: str ka "India"
  Vikas hai gdp: float ka 5.4


Printing
--------
::

  Mitron! boliye <expression>

Example::

  Mitron! boliye "Jai Hind"
  Mitron! boliye desh


Functions
---------
Definition::

  Yojana <name>(arg: type, ...) -> <type>:
      ...
      Wapas dijiye <expression>

Calling::

  Yojana se labh lein <name>(args)

Example::

  Yojana badhao(x: int, y: int) -> int:
      Wapas dijiye x + y

  Yojana se labh lein badhao(2, 3)
  Mitron! boliye _


Conditionals
------------
::

  Agar <condition> toh:
      ...
  Nahi toh:
      ...

Example::

  Agar desh == "India" toh:
      Mitron! boliye "Jai Hind"
  Nahi toh:
      Mitron! boliye "Desh nahi mila"


Loops
-----
::

  Desh ke liye N baar(<int_expr>):
      ...

Example::

  Desh ke liye N baar(3):
      Mitron! boliye "Kaam chalu hai"


API Requests
------------
::

  SchemeLaunch <url_expr> se GET karo
  SchemeLaunch <url_expr> se POST karo <data_expr>

Example::

  Vikas hai url: str ka "https://httpbin.org/get"
  SchemeLaunch url se GET karo
  Mitron! boliye response
