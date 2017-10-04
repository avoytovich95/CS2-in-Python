from SimpleThings.Triangle import Triangle


def main():
    edward = Triangle(10)
    print edward

    iris = Triangle(3, 4, 5)
    print iris

    print "Perimeter of equalateral = %d" % edward.perimeter()
    print "Perimeter of iris = %d" % iris.perimeter()
    print "Area of equalateral = %d" % edward.area()
    print "Area of iris = %d" % iris.area()


if __name__ == "__main__":
    main()