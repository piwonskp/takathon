Introduction
************

Basically any test can be separated into two phases:

* **Test preparation** - configuration, environment setup, mocking, creating objects, preparing arguments
* **Actual test** - a simple assertion, often one-liner

I believe it's safe to say that usually test preparation is way more complicated than actual test. Due to this fact the core point of test is often foggy.

Declarative tests
=================

Now having that said Pytest_ does a great job in managing separation between test preparations(fixtures) and actual tests. But there is more to it. Tests are kind of examples which are always up to date - actually that's what doctest_ do.

.. _Pytest: http://pytest.org
.. _doctest: https://docs.python.org/3/library/doctest.html


**So why?**

There is a huge amount of informations that can be extracted from tests, not only usage examples. Pytest and doctest are hard to parse both by people and software. That's where declarative tests and domain specific languages come in.

**Examples**

Consider statement *Function foo takes 3 as an argument and returns 5*. From this simple statement we can deduce that function has type of `Int -> Int`. Actually this process is called `type inference`_.

.. _type inference: https://en.wikipedia.org/wiki/Type_inference

By analyzing what is being mocked by particular test we can also deduce if the object being tested is pure function or procedure. In other words by analyzing test's mocks you can find tested function's dependencies.

**Tests are description of code very much like type system is.** Tests describe an interface to function, function domain(reasonable arguments that was predicted by author and tested against) and dependencies. While using plain Python tests these data is basically unavailable. Due to these properties of declarative tests it's preferred to call it specification which function is tested against rather than actual tests.
