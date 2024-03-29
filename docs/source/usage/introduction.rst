Introduction
************

A test can be separated into three phases:

* **Test preparation** - configuration, environment setup, mocking, creating objects, preparing arguments etc.
* **Invocation** - execution of the code under test
* **Assertion** - a single assertion or series of assertions, often one-liner

Usually test preparation is the most complicated phase. Due to this fact the core point of test is often foggy.

Declarative tests
=================

Pytest_ does a great job in managing separation between test preparation(fixtures) and actual tests. But there is more to it. Tests are kind of examples which are always up to date - actually that's what doctest_ do.

.. _Pytest: http://pytest.org
.. _doctest: https://docs.python.org/3/library/doctest.html


**So why?**

There is a huge amount of informations that can be extracted from tests, not only usage examples. Pytest and doctest are hard to parse both by people and software. That's where declarative tests and domain specific languages come in.

**Examples**

Consider statement *Function foo takes 3 as an argument and returns 5*. From this simple statement we can deduce that function has type of `Int -> Int`. This process is called `type inference`_.

.. _type inference: https://en.wikipedia.org/wiki/Type_inference

By analyzing what is being mocked by particular test we can also deduce if the object being tested is a pure function or a procedure. In other words by analyzing test's mocks you can find tested procedure's dependencies.

**Tests are a description of code very much like type system is.** Tests describe an interface to function, function domain(reasonable arguments that was predicted by author and tested against) and dependencies. While using plain Python tests this data is basically unavailable. Due to these properties of declarative tests it is preferred to call it specification which function is tested against rather than tests.
