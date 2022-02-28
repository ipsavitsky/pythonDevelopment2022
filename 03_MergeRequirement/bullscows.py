import textdistance as td
from random import choice


def bullscows(guess: str, secret: str) -> tuple[int, int]:
    hamming_len = td.Hamming().similarity(guess, secret)
    bag_len = td.Bag().similarity(guess, secret)
    return (hamming_len, bag_len)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = choice(words)
    while (curword := ask('Введите слово: ', words)) != secret:
        inform('Быки: {}, Коровы: {}', *bullscows(curword, secret))
    # what to do here?!?!?
    print(123)


def ask(prompt: str, valid: list[str] = None) -> str:
    # TODO: rewrite to walrus?
    input_word = input(prompt)
    while True:
        if valid is not None and input_word not in valid:
            input_word = input(prompt)
        else:
            break    
    return input_word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))
