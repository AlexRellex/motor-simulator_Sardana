"""
This file was autogenerated by taurusgui --new-gui.
"""

from __future__ import absolute_import

import click
from .config import *

@click.command("motor_gui")
@click.pass_context
@click.option('--safe-mode', 'safe_mode', is_flag=True, default=False,
              help=('launch in safe mode (it prevents potentially problematic '
                    'configs from being loaded)')
              )
def run(ctx, safe_mode):
    from taurus.qt.qtgui.taurusgui.taurusgui import gui_cmd
    ctx.invoke(gui_cmd, confname="tgconf_motor_gui", safe_mode=safe_mode)
