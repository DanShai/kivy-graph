'''


@author: dan
'''
from kivy.uix.slider import Slider
from kivy.properties import ListProperty, ObjectProperty, NumericProperty

from utils import get_icon_char, get_rgba_color
from f_scalable import ScalableBehaviour

from kivy.lang import Builder


def style_default(style_name):
    return None


def icon_default(icon_name):
    return ''


def ramp_default(ramp_group_tuple):
    return None


Builder.load_string('''
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import randint random.randint


<-FSlider>:
    ripple_color: self.get_color(self.ripple_color_tuple,1)
    canvas:
        Color:
            rgba: self.get_color(self.color_tuple,1)
        Rectangle:
            pos: (self.x + self.padding, self.center_y - sp(8)) if self.orientation == 'horizontal' else (self.center_x - sp(8), self.y + self.padding)
            size: (self.width - self.padding * 2, sp(16)) if self.orientation == 'horizontal' else (sp(16), self.height - self.padding * 2)
        Color:
            rgba: self.get_color(self.outline_color_tuple,1)
        Line:
            rounded_rectangle: [self.x + self.padding, self.center_y - sp(8), self.width - self.padding * 2, sp(16), sp(4)] if self.orientation == 'horizontal' else [self.center_x - sp(8), self.y + self.padding, sp(16), self.height - self.padding * 2, sp(4)]
            width: sp(self.sp_width)
        Color:
            rgba: self.get_color(self.slider_color_tuple,1)
        Ellipse:
            pos: (self.value_pos[0] - sp(16), self.center_y - sp(17)) if self.orientation == 'horizontal' else (self.center_x - sp(16), self.value_pos[1] - sp(16))
            size: (sp(32), sp(32))
        Color:
            rgba: self.get_color(self.slider_outline_color_tuple,1)
        Line:
            ellipse: [self.value_pos[0] - sp(16), self.center_y - sp(17), sp(32), sp(32)] if self.orientation == 'horizontal' else [self.center_x - sp(17), self.value_pos[1] - sp(16), sp(32), sp(32)]
            width: sp(self.sp_width)
''')


class FSlider(Slider):
    get_color = ObjectProperty(get_rgba_color)
    color_tuple = ListProperty(['Blue', '400'])
    slider_color_tuple = ListProperty(['Orange', '300'])
    outline_color_tuple = ListProperty(['Red', '300'])
    slider_outline_color_tuple = ListProperty(['Red', '300'])
    sp_width = NumericProperty(5)

    def __init__(self, **args):
        super(FSlider, self).__init__(**args)
