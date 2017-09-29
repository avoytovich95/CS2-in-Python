def main():
    words = raw_input("Enter a sentence: ")
    words = longer(words)
    print "The longer words..."
    print words


def longer(sent):
    longer__words = ""
    word = sent.split()
    total = 0

    for i in word:
        total += len(i)
    mean = total / len(word)

    for i in word:
        if len(i) > mean:
            longer__words += i + " "
    return longer__words


if __name__ == "__main__":
    main()
