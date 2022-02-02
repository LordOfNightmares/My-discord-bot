from random import randint, choice

from urllib3.packages.six import unichr

try:
    chr = unichr
except NameError:
    pass  # Cause we're on Python3


def zalgo(text, intensity=50):
    zalgo_threshold = intensity
    zalgo_chars = [chr(i) for i in range(0x0300, 0x036F + 1)]
    zalgo_chars.extend([u'\u0488', u'\u0489'])
    source = text
    if not _is_narrow_build:
        source = _insert_randoms(source)
    zalgoized = []
    for letter in source:
        zalgoized.append(letter)
        zalgo_num = randint(0, zalgo_threshold) + 1
        for _ in range(zalgo_num):
            zalgoized.append(choice(zalgo_chars))
    response = choice(zalgo_chars).join(zalgoized)
    return response


def _insert_randoms(text):
    random_extras = [unichr(i) for i in range(0x1D023, 0x1D045 + 1)]
    newtext = []
    for char in text:
        newtext.append(char)
        if randint(1, 5) == 1:
            newtext.append(choice(random_extras))
    return u''.join(newtext)


def _is_narrow_build():
    try:
        chr(0x10000)
    except ValueError:
        return True
    return False


def convert_zalgo(text, intensity=50, copy=False):
    input_text = u' '.join(text)
    zalgotext = zalgo(input_text, intensity)
    return zalgotext


# print(convert_zalgo("test"))
