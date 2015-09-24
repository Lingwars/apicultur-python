apicultur.io
============

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

* FreelingNER_: reconocimiento de entidades. Devuelve todas las entidades con nombre propio (lugares,
  personas, organizaciones, instituciones, etc,..) que aparecen en un texto en español.

.. _FreelingNER: https://apicultur.io/apis/info?name=NamedEntityRecognition_Freeling_es&version=1.0.0&provider=TheLinguist

    .. code::

        >>> apiio.ner_es(texto=u"Ana sabe un secreto que no sabe nadie.")
        [{'entidades': [{'lema': 'ana', 'categoria': 'NP00000'}], 'palabra': 'Ana'}]

* FreelingNumerical_: extractor de cantidades, fechas y monedas. Devuelve los valores que aparecen en un
  texto en español. Identifica expresiones escritas como número y expresiones en palabras.

.. _FreelingNumerical: https://apicultur.io/apis/info?name=NumericalExpressionRecognition_Freeling_es&version=1.0.0&provider=TheLinguist

    .. code::

        >>> apiio.quantities_es(texto=u"Los dos perros se comieron 25 salchichas.")
        [{'entidades': [{'lema': '2', 'categoria': 'numero'}], 'expresion': 'dos'}, {'entidades': [{'lema': '25', 'categoria': 'numero'}], 'expresion': '25'}]

* FreelingParser_: Chunking & full parsing API (Spanish): This API returns the constituents (phrases)
  of a given sentence. It also provides its internal structure and components.

.. _FreelingParser: https://apicultur.io/apis/info?name=Parser_Freeling_es&version=1.0.0&provider=TheLinguist

    .. code::

        >>> r = apiio.parse_es(texto=u"Los dos perros se comieron 25 salchichas.")
        >>> pprint(r)
        [{'level': 0, 'parent': 'ROOT', 'tag': 'S'},
         {'level': 1, 'parent': 'S', 'tag': 'sn'},
         {'level': 2, 'parent': 'sn', 'tag': 'espec-mp'},
         {'level': 3, 'parent': 'espec-mp', 'tag': 'grup-complex-spec-mp'},
         {'level': 4, 'parent': 'grup-complex-spec-mp', 'tag': 'j-mp'},
         {'lemma': 'el', 'level': 5, 'parent': 'j-mp', 'tag': 'DA0MP0', 'text': 'Los
         {'level': 4, 'parent': 'grup-complex-spec-mp', 'tag': 'num-mp'},
         {'lemma': '2', 'level': 5, 'parent': 'num-mp', 'tag': 'Z', 'text': 'dos'},
         {'level': 2, 'parent': 'sn', 'tag': 'grup-nom-mp'},
         {'level': 3, 'parent': 'grup-nom-mp', 'tag': 'n-mp'},
         {'lemma': 'perro',
          'level': 4,
          'parent': 'n-mp',
          'tag': 'NCMP000',
          'text': 'perros'},
         {'level': 1, 'parent': 'S', 'tag': 'grup-verb'},
         {'level': 2, 'parent': 'grup-verb', 'tag': 'morfema-verbal'},
         {'lemma': 'se',
          'level': 3,
          'parent': 'morfema-verbal',
          'tag': 'P00CN000',
          'text': 'se'},
         {'level': 2, 'parent': 'grup-verb', 'tag': 'grup-verb'},
         {'level': 3, 'parent': 'grup-verb', 'tag': 'verb'},
         {'lemma': 'comer',
          'level': 4,
          'parent': 'verb',
          'tag': 'VMIS3P0',
          'text': 'comieron'},
         {'level': 1, 'parent': 'S', 'tag': 'sn'},
         {'level': 2, 'parent': 'sn', 'tag': 'numero-nopart'},
         {'lemma': '25',
          'level': 3,
          'parent': 'numero-nopart',
          'tag': 'Z',
          'text': '25'},
         {'level': 2, 'parent': 'sn', 'tag': 'grup-nom-fp'},
         {'level': 3, 'parent': 'grup-nom-fp', 'tag': 'n-fp'},
         {'lemma': 'salchicha',
          'level': 4,
          'parent': 'n-fp',
          'tag': 'NCFP000',
          'text': 'salchichas'},
         {'level': 1, 'parent': 'S', 'tag': 'F-term'},
         {'lemma': '.', 'level': 2, 'parent': 'F-term', 'tag': 'Fp', 'text': '.'}]

* FreelingSemanticTagger_: Semantic tagger & POS tagger & Lemmatizer API (Spanish): Given a text in Spanish,
  the API provides the lemma, part of speech tag and semantic code from Wordnet for every word in the text.

.. _FreelingSemanticTagger: https://apicultur.io/apis/info?name=SemanticTagger_Freeling_es&version=1.0.0&provider=TheLinguist

    .. code::

        >>> r = apiio.semantic_tagger_es(texto=u"Los dos perros se comieron 25 salchichas.")
        >>> pprint(r)
        [{'lemas': [{'categoria': 'DA0MP0', 'lema': 'el'}],
          'palabra': 'Los',
          'synsets': ['']},
         {'lemas': [{'categoria': 'Z', 'lema': '2'}],
          'palabra': 'dos',
          'synsets': ['']},
         {'lemas': [{'categoria': 'NCMP000', 'lema': 'perro'}],
          'palabra': 'perros',
          'synsets': ['02084071-n', '10539715-n']},
         {'lemas': [{'categoria': 'P00CN000', 'lema': 'se'}],
          'palabra': 'se',
          'synsets': ['']},
         {'lemas': [{'categoria': 'VMIS3P0', 'lema': 'comer'}],
          'palabra': 'comieron',
          'synsets': ['01166351-v', '01168468-v', '01185304-v']},
         {'lemas': [{'categoria': 'Z', 'lema': '25'}],
          'palabra': '25',
          'synsets': ['']},
         {'lemas': [{'categoria': 'NCFP000', 'lema': 'salchicha'}],
          'palabra': 'salchichas',
          'synsets': ['07675627-n']},
         {'lemas': [{'categoria': 'Fp', 'lema': '.'}],
          'palabra': '.',
          'synsets': ['']}]

* FreelingSentenceSplitter_: Sentence splitter API (Spanish): This API splits a given text into sentences
  taking into account Spanish rules for punctuation marks.

.. _FreelingSentenceSplitter: https://apicultur.io/apis/info?name=SenteceSplitter_Freeling_es&version=1.0.0&provider=TheLinguist

    .. code::

        >>> apiio.sentence_splitter_es(texto=u"¿Qué es poesía? ¿Y tú me lo preguntas? Poesía... eres tú.")
        [{'oracion': '¿ Qué es poesía ?'}, {'oracion': '¿ Y tú me lo preguntas ?'}, {'oracion': 'Poesía ... eres tú .'}]

* FreelingSyntaxAnalysis_: Syntax analysis API (Spanish): This API returns the syntax analysis
  (chunks, phrases and dependency relations between components) of a given sentence.

.. _FreelingSyntaxAnalysis: https://apicultur.io/apis/info?name=SyntaxAnalysis_Freeling_es&version=1.0.0&provider=TheLinguist

    .. code::

        >>> r = apiio.syntax_analysis_es(texto=u"¿Qué es poesía? ¿Y tú me lo preguntas? Poesía... eres tú.")
        >>> pprint(r)
        [{'label': 'grup-verb',
          'lemma': 'ser',
          'parent': None,
          'rel': 'top',
          'tag': 'VSIP3S0',
          'text': 'es'},
         {'label': 'F-no-c',
          'lemma': '¿',
          'parent': 'top',
          'rel': 'term',
          'tag': 'Fia',
          'text': '¿'},
         {'label': 'sn',
          'lemma': 'qué',
          'parent': 'top',
          'rel': 'subj',
          'tag': 'PT0CN000',
          'text': 'Qué'},
         {'label': 'sn',
          'lemma': 'poesía',
          'parent': 'top',
          'rel': 'att',
          'tag': 'NCFS000',
          'text': 'poesía'},
         {'label': 'F-term',
          'lemma': '?',
          'parent': 'top',
          'rel': 'term',
          'tag': 'Fit',
          'text': '?'},
         {'label': 'F-no-c',
          'lemma': '¿',
          'parent': None,
          'rel': 'top',
          'tag': 'Fia',
          'text': '¿'},
         {'label': 'coor-n',
          'lemma': 'y',
          'parent': 'top',
          'rel': 'modnorule',
          'tag': 'CC',
          'text': 'Y'},
         {'label': 'sn',
          'lemma': 'tú',
          'parent': 'modnorule',
          'rel': 'co-n',
          'tag': 'PP2CSN00',
          'text': 'tú'},
         {'label': 'patons',
          'lemma': 'me',
          'parent': 'top',
          'rel': 'modnorule',
          'tag': 'PP1CS000',
          'text': 'me'},
         {'label': 'patons',
          'lemma': 'lo',
          'parent': 'top',
          'rel': 'modnorule',
          'tag': 'PP3CNA00',
          'text': 'lo'},
         {'label': 'sn',
          'lemma': 'pregunta',
          'parent': 'top',
          'rel': 'modnorule',
          'tag': 'NCFP000',
          'text': 'preguntas'},
         {'label': 'F-term',
          'lemma': '?',
          'parent': 'modnorule',
          'rel': 'term',
          'tag': 'Fit',
          'text': '?'},
         {'label': 'grup-verb',
          'lemma': 'ser',
          'parent': None,
          'rel': 'top',
          'tag': 'VSIP2S0',
          'text': 'eres'},
         {'label': 'sn',
          'lemma': 'poesía',
          'parent': 'top',
          'rel': 'subj',
          'tag': 'NP00000',
          'text': 'Poesía'},
         {'label': 'F-no-c',
          'lemma': '...',
          'parent': 'subj',
          'rel': 'modnomatch',
          'tag': 'Fs',
          'text': '...'},
         {'label': 'sn',
          'lemma': 'tú',
          'parent': 'top',
          'rel': 'att',
          'tag': 'PP2CSN00',
          'text': 'tú'},
         {'label': 'F-term',
          'lemma': '.',
          'parent': 'top',
          'rel': 'term',
          'tag': 'Fp',
          'text': '.'}]

* FreelingTokenizer_: Tokenizer API: This API divides a given text in Spanish into of words.

.. _FreelingTokenizer: https://apicultur.io/apis/info?name=Tokenizer_Freeling_es&version=1.0.0&provider=TheLinguist

    .. code::

        >>> r = apiio.tokenize_es(texto=u"¿Qué es poesía? ¿Y tú me lo preguntas? Poesía... eres tú.")
        >>> pprint(r)
        [{'oracion': ['¿', 'Qué', 'es', 'poesía', '?']},
         {'oracion': ['¿', 'Y', 'tú', 'me', 'lo', 'preguntas', '?']},
         {'oracion': ['Poesía', '...', 'eres', 'tú', '.']}]

* TransitiveVerb_: Spanish verb conjugator API: Given a verb in infinitive, the API provides information
  concerning its transitive status. 1-Never, 2-Depends on meaning, 3-Always.

.. _TransitiveVerb: http://apicultur.io/apis/info?name=VerbTransitive_Onoma_es&version=1.0.0&provider=molinodeideas

    .. code::

        >>> apiio.transitive_verb(infinitivo=u"Querer"))
        {'response': [{'pronominal': 1}]}
        >>> apiio.transitive_verb(infinitivo=u"Correr"))
        {'response': [{'pronominal': 2}]}



