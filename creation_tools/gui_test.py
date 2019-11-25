import sys
from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication

if __name__ == '__main__':
    pass

    app = TaurusApplication(sys.argv, cmd_line_parser=None,)
    panel = Qt.QWidget()
    layout = Qt.QHBoxLayout()
    panel.setLayout(layout)

    commands = Qt.QWidget()
    layout2 = Qt.QHBoxLayout()
    commands.setLayout(layout2)
    # Header

    from taurus.qt.qtgui.panel import TaurusForm, TaurusCommandsForm
    from taurus.qt.qtgui.display import TaurusLabel
    from taurus.qt.qtgui.button import TaurusCommandButton


    panel = TaurusForm()
    props = ['state', 'status', 'position', 'velocity', 'acceleration']
    model = ['x/foo/motor/%s' % p for p in props]
    panel.setModel(model)
    panel[0].readWidgetClass = TaurusLabel
    """
    start_move = TaurusCommandButton(command = 'start_move', parameters=['2+2'],icon='actions:media_playback_start.svg')
    stop_move = TaurusCommandButton(command='stop_move', icon='actions:media_playback_stop_green.svg')
    reset = TaurusCommandButton(command='reset', icon='logos:actions:stop.svg')
    command_list = [start_move, stop_move, reset]
    """
    commands = TaurusCommandsForm()
    commands.setModel('x/foo/motor')

    """
    button =  TaurusCommandButton(command = 'start_move', parameters=['2+2'],icon='logos:taurus.png')
    button.setModel('x/foo/motor')
    """

    props = ['start_move', 'stop_move', 'reset']
    commands = TaurusCommandsForm()
    commands.setModel('x/foo/motor')
    config = commands.createConfig()
    print(config)
    # Footer

    #panel.show()
    commands.show()
    sys.exit(app.exec_())

