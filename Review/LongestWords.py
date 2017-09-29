def main():
    words = raw_input("Enter a sentence: ")
    word = longest(words)
    print "The longest word..."
    print word


def longest(words):
    max__ = 0
    list__ = words.split()
    for s in list__:
        if len(s) > max__:
            max__ = len(s)
            long__word = s
    return long__word


if __name__ == "__main__":
    main()
