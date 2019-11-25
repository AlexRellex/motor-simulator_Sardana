from sardana.macroserver.macro import Macro, Type


class move(Macro):

    param_def = [["moveable", Type.Moveable, None, "moveable to move"],
                ["position", Type.Float, None, "absolute position"]]

    def run(self, moveable, position):
        """This macro moves a moveable to the specified position"""
        moveable.move(position)
        self.output("%s is now at %s", moveable.getName(), moveable.getPosition())

"""
class stop(Macro):

class reset(Macro):
"""