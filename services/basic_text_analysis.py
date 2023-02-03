from textstat.textstat import textstat


def words(text):
    return text.split()


def characters(text):
    characters = text.replace(' ', '')
    return characters


def sentences(text):
    sentences = text.split('. | ? | !')
    return sentences


def syllablecount(text):
    return textstat.syllable_count(text)


def basic_text_stats(context):
    return {
        'words': words(context),
        'characters': characters(context),
        'sentences': sentences(context),
        'syllablecount': syllablecount(context)
    }
