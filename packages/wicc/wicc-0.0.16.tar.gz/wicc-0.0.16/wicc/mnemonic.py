#!/usr/bin/python
# -*- coding: utf-8 -*-

from cryptos import *
from wicc.language import Language


def random_words(language: Language=Language.English.name):
    if language == Language.French.name:
        from wicc.cryptos.words_fr import words_list
        return entropy_to_words(os.urandom(16), words_list)
    elif language == Language.Spanish.name:
        from wicc.cryptos.words_es import words_list
        return entropy_to_words(os.urandom(16), words_list)
    elif language == Language.Italian.name:
        from wicc.cryptos.words_it import words_list
        return entropy_to_words(os.urandom(16), words_list)
    elif language == Language.Korean.name:
        from wicc.cryptos.words_ko import words_list
        return entropy_to_words(os.urandom(16), words_list)
    elif language == Language.Japanese.name:
        from wicc.cryptos.words_jp import words_list
        return entropy_to_words(os.urandom(16), words_list)
    elif language == Language.Simplified_Chinese.name:
        from wicc.cryptos.words_zh_hans import words_list
        return entropy_to_words(os.urandom(16), words_list)
    else:
        from wicc.cryptos.words_en import words_list
        return entropy_to_words(os.urandom(16), words_list)