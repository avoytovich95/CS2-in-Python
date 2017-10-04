from SimpleThings.Name import Name
from SimpleThings.Triangle import Triangle


def main():
    # Part 1: creation of lists
    songs = create__songs()
    display("The songs... ", songs)
    actors = create__actors()
    display("The actors... ", actors)
    triangles = create__triangles()
    display("The triangles...", triangles)

    # Part 2: User the lists
    display__lengths(songs)
    display__intials(actors)
    display__areas(triangles)


def create__songs():
    songs = []
    songs += ["Happy"]
    songs += ["Dog Days are Over"]
    songs += ["Budapest"]
    songs += ["Give Me Your Eyes"]
    songs += ["Castle of Glass"]
    songs += ["Heralds"]
    songs += ["No Rest for the Wicked"]
    songs += ["Death from Above"]
    return songs


def create__actors():
    actors = []
    actors += [Name("Ryan", "Reynolds")]
    actors += [Name("Hugh", "Jackman")]
    actors += [Name("Zach", "Braff")]
    actors += [Name("Bradley", "Cooper")]
    actors += [Name("Halle", "Berry")]
    actors += [Name("Kate", "Mara")]
    actors += [Name("Kevin", "Spacey")]
    return actors


def create__triangles():
    triangles = []
    triangles += [Triangle(30)]
    triangles += [Triangle(6, 12, 9)]
    triangles += [Triangle(3, 4, 5)]
    triangles += [Triangle(10)]
    triangles += [Triangle(12)]
    triangles += [Triangle(12, 13, 14)]
    return triangles


def display(text, items):
    print "\n" + text
    for s in items:
        print s


def display__lengths(songs):
    print "\nThe Song Lengths..."
    for s in songs:
        print "%d" % len(s)


def display__intials(actors):
    print "\nThe Initials"
    for s in actors:
        print s.initials()


def display__areas(triangles):
    print "\nThe Areas"
    for s in triangles:
        print s.area()


if __name__ == "__main__":
    main()
