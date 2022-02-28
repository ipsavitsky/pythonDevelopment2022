import textdistance as td

def bullscows(guess: str, secret: str) -> tuple[int, int]:
    # TODO: sorensen bad????
    hamming_len = td.Hamming().similarity(guess, secret)
    bag_len = td.Bag().similarity(guess, secret)
    return (hamming_len, bag_len)

