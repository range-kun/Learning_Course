from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    assert type(value) == str
    list_of_words = value.split()
    for word in list_of_words:
        if word.lower() in ['хуй', 'пизда', 'ебать', 'блять']:
            index = list_of_words.index(word)
            list_of_words[index] = '#' + word[1:-1] + '%'

    return ' '.join(list_of_words)

