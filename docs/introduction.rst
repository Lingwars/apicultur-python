
Introducción
============
**Apicultur** es una biblioteca de Python preparada para acceder a un conjunto
de APIs con utilidades de procesamiento de lenguaje natural que se encuentran
disponibles en el proyecto del mismo nombre Apicultur_.

.. _Apicultur: http://apicultur.com/


Quickstart
----------
La biblioteca está disponible en Pypi, así que para instalarla bastará con:

.. code:: bash

    pip install apicultur

y ya puedes empezar a utilizarla:

.. code:: python

    >>> from apicultur import Apicultur
    >>> from secret import ACCESS_TOKEN  # Clave de acceso obtenida en http://store.apicultur.com
    >>> api = Apicultur(ACCESS_TOKEN)
    >>> api.list_services()
    IDENTIFIER              DATA
    ==========              ====
    [...] Se listarán todos los servicios disponibles
    >>> api.lematiza2(word='meses')
    {'lemas': [{'lema': 'mes', 'categoria': 'NCMP000'}, {'lema': 'mesar', 'categoria': 'VMSP2S0'}], 'palabra': 'meses'}
    >>>

También puedes consultar otros ejemplos disponibles `aquí <https://github.com/Lingwars/apicultur-examples>`__.


Access_token
------------
En la ejecución del ejemplo anterior se hace uso de una variable `ACCESS_TOKEN` que
identifica al usuario que realiza las llamadas a Apicultur_. Para conseguir tu
`access_token` deberás acudir a la web, registrarte y suscribir una aplicación a las APIs
que vayas a utilizar.