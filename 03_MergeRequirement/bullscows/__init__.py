import textdistance as td
from random import choice


def bullscows(guess: str, secret: str) -> tuple[int, int]:
    hamming_len = td.Hamming().similarity(guess, secret)
    bag_len = td.Bag().similarity(guess, secret)
    return (hamming_len, bag_len)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = choice(words)
    turns = 0
    print(secret)
    while (curword := ask('Введите слово: ', words)) != secret:
        bulls, cows = bullscows(curword, secret)
        inform('Быки: {}, Коровы: {}', bulls, cows)
        turns += 1
    return turns



