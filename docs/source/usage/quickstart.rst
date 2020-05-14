Quickstart
**********

Structure
=========

Basic specification structure:

.. code-block:: none

   spec:
       [Any operation here applies to all test cases below]
       domain <arguments>:
           [Operations declared here apply to this particular test case]
           results <expected result>

Let's see what all of this means:

* **spec** - indicates start of specification.
* **domain** - indicates single test case. Domain statement is followed by arguments passed to the tested function.
* **results** - specifies the expected result of test case.

Ordinal data
============

Tests shall be simple. As simple as saying "if I provide you with arguments X I expect the result Y". So let's try to implement function that provided with negative value returns 0. Otherwise the function returns its input.

.. literalinclude:: ../../../examples/domain_types/ordinal.py

Test cases can include plain values or sets of values as arguments. That is why the keyword is called `domain` rather than `arguments`. `interval` is used to specify input ranges in which function has constant output. Additionally `Infinity` is a special value that indicates no upper boundary of range (`-Infinity` means no lower boundary).

.. warning::
   Interval is mechanism of specyfing tests declaratively. Under the hood argument contained within specified range is randomly generated. The language **does not** prove the statement is true for all possible combinations of arguments by any means.

Running tests
=============

To run tests use command:

.. code-block:: bash

   takathon <path-to-file-or-directory>

Additionaly if you want more detailed output you can use:

.. code-block:: bash

   takathon -v info <path-to-file-or-directory>

Nominal data
============

For unordered test data you can use `any_of` to indicate that the result is constant for specified objects. 

.. literalinclude:: ../../../examples/domain_types/nominal.py

Python features
===============

Plain Python imports works out of the box so you can bring anything to test scope. No need to bloat the module itself. Python style comments are also supported.
