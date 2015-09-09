
Introducción
============

**Apicultur** es una biblioteca de Python preparada para acceder a un conjunto
de APIs con utilidades de procesamiento de lenguaje natural.


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
    ==========              ===
    [...] Se listarán todos los servicios disponibles
    >>> api.lematiza2(word='meses')
    {'lemas': [{'lema': 'mes', 'categoria': 'NCMP000'}, {'lema': 'mesar', 'categoria': 'VMSP2S0'}], 'palabra': 'meses'}
    >>>

También puedes consultar otros ejemplos disponibles `aquí <https://github.com/Lingwars/apicultur-examples>`__