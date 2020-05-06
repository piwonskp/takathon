Documentation
*************

Apart from comments in specification there are two additional keywords which are preferred to document the object and describe test cases. These are:

* title
* description


Short summary
=============

**title** is used to present test results to the user.

When used on specification level `title` is a short summary of object's goal.

`title` on test case level indicates test case goal.

When `title` is missing user will be presented with function name(specification level) or domain(test case level).

Long description
================

**description** contains actual documentation for programmers.


When used on specification level `description` is a documentation for object itself.

`description` on test case level helps understand reasons of particular test and it's quirks.

Examples
========

Specification level documentation
---------------------------------

Note that example below is syntactically correct and will compile without any error. You can preserve TDD workflow without any additional action or jumping between files. You also are not required to have any test cases in specification.

.. literalinclude:: ../../../examples/docs/unimplemented_function.py

Test case level documentation
-----------------------------

.. literalinclude:: ../../../examples/docs/test_case_docs.py
