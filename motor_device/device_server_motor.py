from controlador_motor import Motor
from numpy.random import random_sample
from tango import AttrQuality, AttrWriteType, DispLevel, DevState#, PyDsExp
from tango.server import Device, attribute, command, device_property


class DS_Motor(Device):

    max_velocity = device_property(dtype=float, default_value=21)
    max_acceleration = device_property(dtype=float, default_value=11)
    max_position = device_property(dtype=float, default_value=200)

    def init_device(self):
        self.d_motor = Motor()
        self.set_state(DevState.ON)
        self.set_status("Motor is waiting for command")
        Device.init_device(self)

    @attribute(label="Position", dtype=float, unit="m", min_value=0.0, max_value=200,
               access=AttrWriteType.READ, memorized=True)
    def position(self):
        if self.d_motor.position == self.d_motor.destination:
            self.set_state(DevState.ON)
            self.set_status("Destination reached")
        return self.d_motor.position

    @position.write
    def position(self, position):
        if self.get_state() != DevState.MOVING:
            self.d_motor.position = position
        else:
            self.set_status("Motor is moving can't write!!")

    @attribute(label="Velocity", dtype=float, unit="m/s", min_value=0.0,
               access=AttrWriteType.READ_WRITE, max_value=21, memorized=False)
    def velocity(self):
        return self.d_motor.velocity

    @velocity.write
    def velocity(self, velocity):
        if self.get_state() != DevState.MOVING:
            self.d_motor.velocity = velocity
        else:
            self.set_status("Motor is moving can't write!!")

    @attribute(label="acceleration", dtype=float, unit="m/s**2", min_value=0.0,
               access=AttrWriteType.READ_WRITE, max_value=11, memorized=False)
    def acceleration(self):
        return self.d_motor.acceleration

    @acceleration.write
    def acceleration(self, acceleration):
        if self.get_state() != DevState.MOVING:
            self.d_motor.acceleration = acceleration
        else:
            self.set_status("Motor is moving can't write!!")

    @command(dtype_in=float)
    def start_move(self, destination):
        if self.get_state() != DevState.MOVING:
            if destination == self.d_motor.position:
                self.set_state(DevState.ON)
                self.set_status("Already on position")
            elif self.d_motor.velocity != 0.0 and self.d_motor.acceleration != 0.0:
                self.d_motor.start_time = None
                self.d_motor.destination = destination
                try:
                    self.d_motor.start_move()
                    self.set_state(DevState.MOVING)
                    self.set_status("Motor is moving")
                except ValueError:
                    self.set_state(DevState.FAULT)
                    self.set_status("ERROR: Invalid position")
                except RuntimeError:
                    self.set_state(DevState.FAULT)
                    self.set_status("Acceleration too slow")
            else:
                self.set_state(DevState.FAULT)
                self.set_status("ERROR: Invalid acceleration or velocity")
        else:
            self.set_status("Motor already moving, please wait for movement to end")

    @command()
    def stop_move(self):
        self.d_motor.start_time = None
        self.set_state(DevState.ON)
        self.set_status("Motor stopped")

    @command()
    def reset(self):
        self.init_device()


if __name__ == "__main__":
    DS_Motor.run_server()
