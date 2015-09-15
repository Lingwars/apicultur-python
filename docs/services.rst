
Servicios
=========
La librería cuenta con un número de servicios en continuo crecimiento
que están directamente relacionados con los que están disponibles en
la web.

El acceso a estos servicios se realiza a través de funciones miembro de
la clase :code:`Apicultur`. Todos los servicios disponibles pueden listarse
utilizando la función :code:`list_services`.


store.apicultur.com
-------------------
Actualmente se encuentran disponibles los siguientes *endpoints* en `store.apicultur.com`_:

.. _store.apicultur.com: http://store.apicultur.com/

.. code:: python

    from apicultur import Apicultur
    api = Apicultur('access_token')
    api.list_services()

* NivelCervantes_: dada una palabra te devuelve su catalogación según el nivel de dificultad tomando como
  referente los niveles del Marco Europeo de Referencia para las Lenguas y las directrices del
  Instituto Cervantes.

.. _NivelCervantes: https://store.apicultur.com/apis/info?name=NivelCervantes&version=1.0.0&provider=MolinodeIdeas

    .. code::

        >>> api.damenivel(word='imperturbabilidad')
        {'valor': 4}

* SilabeadorOrtografico_: separa en sílabas la palabra introducida.

.. _SilabeadorOrtografico: http://store.apicultur.com/apis/info?name=SilabeadorOrtografico&version=1.0.0&provider=MolinodeIdeas

    .. code::

        >>> api.silabeame(word='hiato')
        {'palabraSilabeada': 'hia=to', 'numeroSilabas': 2, 'silabaTonica': 'hia', 'posSilabaTonica': 2}

* EtiquetadorMorfologico_: dado un texto, devuelve los lemas y la categoría gramatical de cada palabra del
  texto. El contenido de esta API está basado en la plataforma Freeling.

.. _EtiquetadorMorfologico:  https://store.apicultur.com/apis/info?name=EtiquetadorMorfologico&version=1.0.0&provider=MolinodeIdeas

    .. code::

        >>> r = api.etiqueta(texto="Entre el dolor y la nada, elegí el dolor.")
        >>> pprint(r)
        [{'lemas': [{'categoria': 'SPS00', 'lema': 'entre'}], 'palabra': 'Entre'},
        {'lemas': [{'categoria': 'DA0MS0', 'lema': 'el'}], 'palabra': 'el'},
        {'lemas': [{'categoria': 'NCMS000', 'lema': 'dolor'}], 'palabra': 'dolor'},
        {'lemas': [{'categoria': 'CC', 'lema': 'y'}], 'palabra': 'y'},
        {'lemas': [{'categoria': 'DA0FS0', 'lema': 'el'}], 'palabra': 'la'},
        {'lemas': [{'categoria': 'PI0CS000', 'lema': 'nada'}], 'palabra': 'nada'},
        {'lemas': [{'categoria': 'Fc', 'lema': ','}], 'palabra': ','},
        {'lemas': [{'categoria': 'VMIS1S0', 'lema': 'elegir'}], 'palabra': 'elegí'},
        {'lemas': [{'categoria': 'DA0MS0', 'lema': 'el'}], 'palabra': 'el'},
        {'lemas': [{'categoria': 'NCMS000', 'lema': 'dolor'}], 'palabra': 'dolor'},
        {'lemas': [{'categoria': 'Fp', 'lema': '.'}], 'palabra': '.'}]

* SegmentaTextos_: API de segmentación de frases (*sentence splitter*). Dado un texto, devuelve las
  frases de las que está compuesto (la segmentación se hace teniendo en cuenta los signos de
  puntuación). El contenido de esta API está basado en la plataforma Freeling.

.. _SegmentaTextos: https://store.apicultur.com/apis/info?name=SegmentadorDeTextos&version=1.0.0&provider=MolinodeIdeas

    .. code::

        >>> api.segmentatextos(texto="¿Qué es poesía? ¿Y tú me lo preguntas? Poesía... eres tú.")
        [{'oracion': '¿ Qué es poesía ?'}, {'oracion': '¿ Y tú me lo preguntas ?'}, {'oracion': 'Poesía ... eres tú .'}]

* Lematizador2_: dada una palabra, devuelve todos los lemas posibles y su categoría gramatical y análisis
  morfológico, siguiendo la nomenclatura de las etiquetas EAGLES.

.. _Lematizador2: http://store.apicultur.com/apis/info?name=Lematizador2&version=1.0.0&provider=MolinodeIdeas

    .. code::

        >>> api.lematiza2(word="meses")
        {'lemas': [{'categoria': 'NCMP000', 'lema': 'mes'}, {'categoria': 'VMSP2S0', 'lema': 'mesar'}], 'palabra': 'meses'}

* Definicion_Uno_: API del diccionario de español. Proporciona definiciones de la palabra pasada por
  parámetro.

.. _Definicion_Uno: https://store.apicultur.com/apis/info?name=DiccionariodeEspanol&version=1.0.0&provider=MolinodeIdeas

    .. code::

        >>> api.definicion_10(word="poesía")
        {'lema': 'poesía', 'definicion': 'Manifestación de la belleza o del sentimiento estético por medio de la palabra, en verso o en prosa.'}

* CalculadorFrecuencia_: obtiene la frecuencia de uso o aparición en textos de una palabra. Calcula el
  número de veces que aparece dicha palabra por cada millón de palabras empleadas.

.. _CalculadorFrecuencia: https://store.apicultur.com/apis/info?name=CalculadorFrecuencia&version=1.0.0&provider=MolinodeIdeas

    .. code::

        >>> api.CalculaFrecuenciaPorMillon(word="imperturbabilidad")
        {'valor': 0.13, 'palabra': 'imperturbabilidad'}


apicultur.io
------------
En `apicultur.io`_ son accesibles otro conjunto de servicios diferente:

.. _apicultur.io: https://apicultur.io/

.. code:: python

    >>> from apicultur import Apicultur
    >>> apiio = Apicultur('access_token', cfg_data='apicultur.io')
    >>> apiio.list_services()


* EnglishToPhone_: dada una palabra escrita en inglés devuelve la escritura de dicha palabra en *phonenglish*.

.. _EnglishToPhone: https://apicultur.io/apis/info?name=Phonenglis_english_to_phonenglish&version=1.0&provider=MolinodeIdeas

    .. code::

        >>> apiio.english_to_phone(word='book')
        {'response': [{'phonenglish': 'buk', 'ingles': 'BOOK'}]}


* PhoneToEnglish_: devuelve la escritura en inglés tradicional de una palabra escrita en *phonenglish*.

.. _PhoneToEnglish: https://apicultur.io/apis/info?name=Ponenglish_phonenglish_to_english&version=1.0&provider=MolinodeIdeas

    .. code::

        >>> apiio.phone_to_english(word='buk')
        {'response': [{'phonenglish': 'buk', 'ingles': 'BOOK'}]}

* AleatoriasNivel_: esta API devuelve 12 palabras (sustantivos) en español según el nivel de frecuencia.

.. _AleatoriasNivel: http://apicultur.io/apis/info?name=WordsbyFreq_Word_Molino_es&version=1.0.0&provider=MolinodeIdeas

    .. code::

        >>> apiio.aleatorias_nivel(frecuencia=2)
        {'response': [{'lema': 'retroactividad'}, {'lema': 'papado'}, ..., {'lema': 'rotación'}]}

* FreelingPOSTagger_: etiquetador sintáctico y lematizador, dado un texto en español devuelve el lema
  y la función gramatical de cada palabra. La desambiguación morfosintáctica se realiza a través del contexto.

.. _FreelingPOSTagger: https://apicultur.io/apis/info?name=POStagger_Freeling_es&version=1.0.0&provider=TheLinguist

    .. code::

        >>> r = apiio.pos_tagger_es(texto="Entre el dolor y la nada elegí el dolor.")
        >>> pprint(r)
        [{'lemas': [{'categoria': 'SPS00', 'lema': 'entre'}], 'palabra': 'Entre'},
        {'lemas': [{'categoria': 'DA0MS0', 'lema': 'el'}], 'palabra': 'el'},
        {'lemas': [{'categoria': 'NCMS000', 'lema': 'dolor'}], 'palabra': 'dolor'},
        {'lemas': [{'categoria': 'CC', 'lema': 'y'}], 'palabra': 'y'},
        {'lemas': [{'categoria': 'DA0FS0', 'lema': 'el'}], 'palabra': 'la'},
        {'lemas': [{'categoria': 'PI0CS000', 'lema': 'nada'}], 'palabra': 'nada'},
        {'lemas': [{'categoria': 'VMIS1S0', 'lema': 'elegir'}], 'palabra': 'elegí'},
        {'lemas': [{'categoria': 'DA0MS0', 'lema': 'el'}], 'palabra': 'el'},
        {'lemas': [{'categoria': 'NCMS000', 'lema': 'dolor'}], 'palabra': 'dolor'},
        {'lemas': [{'categoria': 'Fp', 'lema': '.'}], 'palabra': '.'}]


