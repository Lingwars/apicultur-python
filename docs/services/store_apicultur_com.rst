store.apicultur.com
===================

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

* Acentuador_: Dadas las lílabas y la posición de la sílaba tónica devuelve la palabra correctamente acentuada.

.. _Acentuador: http://store.apicultur.com/apis/info?name=Acentuador&version=1.0.0&provider=molinodeideas

    .. code::

        >>> apistore.acentua(syllabicatedWord=u"ri-e", stressedSyllablePosition="2")
        {'error': 2, 'palabra': 'ríe', 'tipo': 'llana'}
        >>> apistore.acentua(syllabicatedWord=u"pan-ta-lon", stressedSyllablePosition="1")
        {'error': 1, 'palabra': 'pantalón', 'tipo': 'aguda'}
