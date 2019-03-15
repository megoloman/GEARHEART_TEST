import regex as re

words_regex = re.compile('(<[^>]+?>)([^<]+)', re.IGNORECASE)
words_6_regex = re.compile('([^\p{Cyrillic}a-z_]|\A)([\p{Cyrillic}a-z]{6})([^\p{Cyrillic}a-z_]|\Z)', re.IGNORECASE)
links_regex = re.compile('(<\s*a[^>]href=")https://habrahabr.ru([^"]*)', re.IGNORECASE)


def replace_content(content):
    return _replace_words(_replace_links(content))


def _replace_6_char_words(data):
    return data[1] + words_6_regex.sub('\g<1>\g<2>™\g<3>', data[2])


def _replace_words(content):
    return words_regex.sub(_replace_6_char_words, content)


def _replace_links(content):
    return links_regex.sub('\g<1>http://localhost:8080\g<2>', content)
