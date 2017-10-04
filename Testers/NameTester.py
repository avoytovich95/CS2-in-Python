from SimpleThings.Name import Name


def main():
    n = Name("Cleo", "White")
    print "First Name = " + n.first()
    print "Last Name = " + n.last()
    print "Natural Name = " + n.natural()
    print "Formal Name = " + n.formal()
    if n.check('C', 'W'):
        print "Initials of " + n.natural() + " are CW"
    else:
        print "Initials of " + n.natural() + " are not CW"

    if n.check('W', 'C'):
        print "Initials of " + n.natural() + " are WC"
    else:
        print "Initials of " + n.natural() + " are not WC"


if __name__ == "__main__":
    main()
