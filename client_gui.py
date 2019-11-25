from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.panel import TaurusForm, TaurusCommandsForm
from taurus.qt.qtgui.display import TaurusLabel

class MotorGUI(Qt.QMainWindow):
    def __init__(self, parent=None):
        Qt.QMainWindow.__init__(self, parent)
        self.panel = Qt.QWidget()
        self.layout = Qt.QHBoxLayout()
        self.panel.setLayout(self.layout)

    def add_attributes(self):
        form = TaurusForm()
        props = ['state', 'status', 'position', 'velocity', 'acceleration']
        model = ['x/foo/motor/%s' % p for p in props]
        form.addModels(model)
        form[0].readWidgetClass = TaurusLabel
        self.layout.addWidget(form)

    def add_commands(self):
        props = ['start_move', 'stop_move', 'reset']
        commands = TaurusCommandsForm()
        commands.setModel('x/foo/motor')
        self.layout.addWidget(commands)

    def show_GUI(self):
        self.panel.show()


if __name__ == "__main__":
    import sys
    app = TaurusApplication(cmd_line_parser=None)
    gui = MotorGUI()
    gui.add_attributes()
    gui.add_commands()
    gui.show_GUI()
    sys.exit(app.exec_())
