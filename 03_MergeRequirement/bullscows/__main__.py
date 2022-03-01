from bullscows import gameplay
import urllib.request
from sys import argv



def ask(prompt: str, valid: list[str] = None) -> str:
    # TODO: rewrite to walrus?
    input_word = input(prompt)
    if valid is not None:
        while input_word not in valid:
            input_word = input('Нет в словаре такого слова! ' + prompt)
    return input_word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


if len(argv) == 3:
    dict_url, words_len = argv[1:]
elif len(argv) == 2:
    dict_url, words_len = argv[-1], 5
else:
    raise Exception('incorrect number of arguments!')

if dict_url.startswith('https://'):
    with urllib.request.urlopen(dict_url) as opened_url:
        words_dict = opened_url.read().decode('utf-8').split()
else:
    with open(dict_url, 'r') as opened_file:
        words_dict = opened_file.read().split()

lengthed_words = list(filter(lambda x: len(x) == words_len, words_dict))

score = gameplay(ask, inform, lengthed_words)
print()
