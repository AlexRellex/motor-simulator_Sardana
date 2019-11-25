from client_motor import Motor_Client
import tango as tn
from sardana.pool.controller import MotorController

class BaseMotorController(MotorController):

    MaxDevice = 128

    def __init__(self, inst, props, *args, **kwargs):
        """Constructor"""
        super(BaseMotorController, self).__init__(inst, props, *args, **kwargs)
        self.motor_sim = Motor_Client()

    def ReadOne(self, axis):
        """Get the specified motor position"""
        return self.motor_sim.position

    def StateOne(self, axis):
        """Get the specified motor state"""
        return self.motor_sim.state, self.motor_sim.status

    def StartOne(self, axis, position):
        """Move the specified motor to the specified position"""
        self.motor_sim.move_to(position)

    def StopOne(self, axis):
        """Stop the specified motor"""
        self.motor_sim.stop()

    def AbortOne(self, axis):
        self.motor_sim.reset()

    def GetAxisPar(self, axis, name):
        name = name.lower()
        if name == "acceleration":
            v = self.motor_sim.velocity / self.motor_sim.acceleration
        elif name == "deceleration":
            v = self.motor_sim.velocity / self.motor_sim.acceleration
        # elif name == "base_rate":
        #     v = None
        elif name == "velocity":
            v = self.motor_sim.velocity
        # elif name == "step_per_unit":
        #     v = None
        return v

    def SetAxisPar(self, axis, name, value):
        name = name.lower()
        if name == "acceleration":
            acceleration = self.motor_sim.velocity / value
            self.motor_sim.acceleration = acceleration
        elif name == "deceleration":
            acceleration = self.motor_sim.velocity / value
            self.motor_sim.acceleration = acceleration
        # elif name == "base_rate":
        #     # springfield.setMinVelocity(axis, value)
        #     pass
        elif name == "velocity":
            acc_time = self.motor_sim.velocity / self.motor_sim.acceleration
            self.motor_sim.velocity = value
            self.motor_sim.acceleration = self.motor_sim.velocity / acc_time
        # elif name == "step_per_unit":
        #     # springfield.setStepPerUnit(axis, value)
        #     pass

    def DefinePosition(self, axis, position):
        self.motor_sim.position = position