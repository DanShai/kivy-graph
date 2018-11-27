'''


@author: dan
'''
from kivy.config import Config
from kivy.base import EventLoop
from kivy.uix.codeinput import CodeInput

Config.set('input', 'mouse', 'mouse,disable_multitouch')


class MCodeInput(CodeInput):

    def on_touch_down(self, touch):

        super(MCodeInput, self).on_touch_down(touch)

        if 'button' in touch.profile and touch.button == 'right':
            pos = super(MCodeInput, self).to_local(
                *self._long_touch_pos, relative=True)
            self._show_cut_copy_paste(pos, EventLoop.window, mode='paste')
