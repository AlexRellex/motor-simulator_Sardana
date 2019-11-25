import tango as tn


class Motor_Client():
    def __init__(self):
        self.motor_device = tn.DeviceProxy("x/foo/motor")
        # self.motor_device.velocity = self.motor_device.max_velocity
        # self.motor_device.acceleration = self.motor_device.max_acceleration
        self.motor_device.velocity = 20
        self.motor_device.acceleration = 10

    @property
    def velocity(self):
        return self.motor_device.velocity

    @velocity.setter
    def velocity(self, value):
        self.motor_device.velocity = value

    @property
    def acceleration(self):
        return self.motor_device.acceleration

    @acceleration.setter
    def acceleration(self, value):
        self.motor_device.acceleration = value

    @property
    def position(self):
        return self.motor_device.position

    @position.setter
    def position(self, value):
        self.motor_device.position = value

    @property
    def state(self):
        return self.motor_device.state()

    @property
    def status(self):
        return self.motor_device.status()

    def move_to(self, destination):
        self.motor_device.start_move(destination)

    def stop(self):
        self.motor_device.stop_move()

    def reset(self):
        self.motor_device.reset()


def main():
    MC = Motor_Client()
    flag = 1

    print("\n", MC.status)
    print("Current state: ", MC.state)
    print("\nStarting at position: ", MC.position)

    while True:
        while flag == 1:

            destination = float(input("Input position: "))
            MC.velocity = float(input("Input velocity: "))
            MC.acceleration = float(input("Input acceleration: "))

            MC.move_to(destination)
            print("\n", MC.status)
            print("Current state: ", MC.state)
            flag = 0
            if MC.state == "FAULT":
                print(MC.status)
                print("Current state: ", MC.state)
                flag = 1

        choice = int(input("\nEnter 1 to check motor position or 0 to enter new position  "))
        if choice == 1:
            flag = 0
            print("\n", MC.status)
            print("Current state: ", MC.state)
            print("Position: ", MC.position)
        elif choice == 0:
            flag = 1
        else:
            exit("Client has closed")


if __name__ == "__main__":
    main()
