from figdate import figdate

if __name__ == '__main__':
    import sys
    import locale
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    if len(sys.argv) == 3:
        print(figdate(sys.argv[2], sys.argv[1]))
    elif len(sys.argv) == 2:
        print(figdate(format=sys.argv[1]))
    else:
        raise AttributeError()