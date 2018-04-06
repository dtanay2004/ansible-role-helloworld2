=============
Hello World 2
=============


This project is a Flask app to practice config management against.


* Free software: BSD license

Environment Variables
---------------------

Two runtime config variables are available:

* DEBUG - set to "true" to enable debug logging
* CONFIG_PATH - set to path of a `config.yml` file.


config.yml
----------

* Major keys are `name` and `timezone`.
* Optional keys are `title` and `salutation`.

Example:

    ---
    name: 'Jim Bob'
    timezone: 'America/Vancouver'
    title: 'Esquire'
    salutation: 'Dr.'


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
