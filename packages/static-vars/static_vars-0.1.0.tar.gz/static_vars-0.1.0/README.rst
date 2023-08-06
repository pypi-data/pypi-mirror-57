===========
static_vars
===========

A decorator for adding static variables to a method.

Typical use:

.. code-block:: python

    from static_vars import static_vars

    @static_vars(counter=0)
    def foo():
        foo.counter += 1

    foo()
    foo()
    assert foo.counter==2
    foo.counter = 0
    foo()
    assert foo.counter==1

* Free software: MIT license
* Documentation: https://static-vars.readthedocs.io.

