from django.shortcuts import render
from PyDictionary import PyDictionary


def homeView(request):
    return render(request, 'dictionary/home.html')


def searchView(request):
    word = request.GET.get('search')

    dictionary = PyDictionary()

    meanings = dictionary.meaning(word)

    synonyms = dictionary.synonym(word)
    antonyms = dictionary.antonym(word)
    # bundling all the variables in the context
    context = {
        'word': word,
        'meanings': meanings,
        'synonyms': synonyms,
        'antonoyms': antonyms
    }
    return render(request, 'dictionary/search.html')
