# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['static_vars']
setup_kwargs = {
    'name': 'static-vars',
    'version': '0.1.0',
    'description': '<Enter a one-sentence description of this project here.>',
    'long_description': '===========\nstatic_vars\n===========\n\nA decorator for adding static variables to a method.\n\nTypical use:\n\n.. code-block:: python\n\n    from static_vars import static_vars\n\n    @static_vars(counter=0)\n    def foo():\n        foo.counter += 1\n\n    foo()\n    foo()\n    assert foo.counter==2\n    foo.counter = 0\n    foo()\n    assert foo.counter==1\n\n* Free software: MIT license\n* Documentation: https://static-vars.readthedocs.io.\n\n',
    'author': 'Engelbert Tijskens',
    'author_email': 'engelbert.tijskens@uantwerpen.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/etijskens/static_vars',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
