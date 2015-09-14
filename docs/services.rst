
Servicios
=========
La librería cuenta con un número de servicios en continuo crecimiento
que están directamente relacionados con los que están disponibles en
la web.

El acceso a estos servicios se realiza a través de funciones miembro de
la clase :code:`Apicultur`. Todos los servicios disponibles pueden listarse
utilizando la función :code:`list_services`:

.. code:: python

    from apicultur import Apicultur
    api = Apicultur('access_token')
    api.list_services()


.. TODO:: Hay que hacer una buena clasificación y tener muy claros
          los métodos que se utilizan para llamar a cada uno de
          ellos y los argumentos que aceptan. Probablemente se
          pueda construir automáticamente partiendo de los datos
          de cada servicio, pero eso lo dejamos para más adelante.