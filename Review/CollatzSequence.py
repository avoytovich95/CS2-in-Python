import sys


def main():
    count = 0
    num = input("The positive integer? ")

    sys.stdout.write("%d " % num)

    while num is not 1:

        if num % 2 is 0:
            num = num / 2
            sys.stdout.write("%d " % num)
            count = format__count(count)
        else:
            num = num * 3 + 1
            sys.stdout.write("%d " % num)
            count = format__count(count)

    print


def format__count(count):
    count += 1
    if (count + 1) % 10 is 0:
        print
    return count


if __name__ == "__main__":
    main()
