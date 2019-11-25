import ej4


def test():
    # start = 0
    # limit = 200
    # run(destination, velocity, acceleration)

    m1 = ej4.motor()

    print("\nMOVE FORWARD")
    if not ej4.run(m1, 100, 10, 5):
        print("Destination reached")
    else:
        print("TEST BENCH ERROR!!!")
    print("\nMOVE BACKWARDS")
    if not ej4.run(m1, 10, 10, 5):
        print("Destination reached")
    else:
        print("TEST BENCH ERROR")
    print("\nPROOF LIMIT")
    if not ej4.run(m1, 200, 10, 5):
        print("Destination reached")
    else:
        print("TEST BENCH ERROR")
    print("\nBREAK LIMIT")
    if ej4.run(m1, 222, 10, 5):
        print("Limit not broken")
    else:
        print("TEST BENCH ERROR")
    print("\nRETURN TO START")
    if not ej4.run(m1, 0, 10, 5):
        print("Destination reached")
    else:
        print("TEST BENCH ERROR")
    print("\nBREAK START")
    if ej4.run(m1, -10, 10, 5):
        print("start not broken")
    else:
        print("TEST BENCH ERROR")


if __name__ == "__main__":
    test()
