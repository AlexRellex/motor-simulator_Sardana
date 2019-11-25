import time


class Motor():
    def __init__(self):
        self.velocity = 0.0
        self.acceleration = 0.0
        self._position = 0
        self.max_position = 200
        self.start_time = None
        self.destination = 0
        self.t1 = 0.0
        self.t2 = 0.0
        self.t3 = 0.0
        self.x0 = 0.0
        self.x1 = 0.0
        self.x2 = 0.0
        self.sign = 1

    @property
    def position(self):
        if self.start_time == None:
            print("MOVEMENT STOPED")
            return self._position
        if self._position == self.destination:
            print("MOVEMENT STOPED")
            return self._position
        else:
            current_time = time.time() - self.start_time
            if current_time <= self.t1:
                #print("FASE 1")
                self._position = self.x0 + self.sign * (self.acceleration * (current_time ** 2)) / 2
                return self._position

            elif self.t1 < current_time < self.t2:
                #print("FASE 2")
                current_time -= self.t1
                self._position = self.x1 + self.sign * self.velocity * current_time
                return self._position

            elif self.t2 < current_time < self.t3:
                #print("FASE 3")
                current_time -= self.t2
                self._position = self.x2 + self.sign * self.velocity * current_time - self.sign * (self.acceleration * (current_time ** 2)) / 2
                return self._position

            self._position = self.destination
            print("MOVEMENT STOPED")
            return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def start_move(self):
        if self.destination > self.max_position:
            raise ValueError("ERROR: position not reachable")
            return 1
        elif self.destination < 0:
            raise ValueError("ERROR: position not reachable")
            return 1
        elif self.destination == self._position:
            print("Already on position")
            return 1
        else:
            self.sign = 1
            if self._position > self.destination:
                self.sign = -1

            self.t1 = self.velocity / self.acceleration

            self.x0 = self._position
            self.x1 = self.x0 + self.sign * self.acceleration * (self.t1 ** 2) / 2
            if self.t1 == self.t2:
                self.x2 = self.x1
            else:
                self.x2 = self.x1 + self.sign * (abs(self.x0 - self.destination) - 2 * abs(self.x0 - self.x1))

            self.t2 = self.t1 + abs(self.x2 - self.x1) / self.velocity
            self.t3 = self.t1 + self.t2
            if 2 * self.t1 > self.t3:
                raise RuntimeError("Acceleration time too slow")
                return 1

            self.start_time = time.time()

            print("times")
            print(self.t1)
            print(self.t2)
            print(self.t3)
            print("positions")
            print(self.x0)
            print(self.x1)
            print(self.x2)
            return 0

"""
def run(m1,destination, velocity, acceleration):
    print("\nStarting at position: ", m1.position)

    m1.velocity = velocity
    m1.acceleration = acceleration
    m1.destination = destination
    flag = m1.start_move()
    print("MOTOR STARTED MOVING")

    if flag == 1:
        print("\nTry again... \n")
        return 1

    while m1.position != destination:
        print("position: ", m1.position)
        time.sleep(0.2)
    print("\nFinal postion", m1.position)
    return 0


def main():
    m1 = Motor()
    run(m1,100,10,5)
    run(m1,200,10,5)
    run(m1,100,10,5)

    m1 = motor()
    flag = 1
    while True:

        while flag == 1:

            print("\nStarting at position: ")
            print(m1.position)

            m1.destination = float(input("Input position: "))
            m1.velocity = float(input("Input velocity: "))
            m1.acceleration = float(input("Input acceleration: "))
            flag = m1.start_move()

            if flag == 1:
                print("Try again... \n")
        choice = int(input("Enter 1 to check motor position or 0 to enter new position  "))
        if choice == 1:
            print(m1.position)
        else:
            flag = 1


if __name__ == "__main__":
    main()
"""
