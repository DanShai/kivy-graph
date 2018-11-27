'''


@author: dan
'''
from kivy.uix.widget import Widget
from kivy.lang import Builder


from kivy.properties import ListProperty, ObjectProperty, NumericProperty

from utils import get_rgba_color

Builder.load_string('''
<CWidget>:
    canvas.before:
        Color:
            rgba: self.get_color(self.bg_color,self.balpha)

        Ellipse:
            pos: self.center_x - self.radius, self.center_y - self.radius
            size: self.radius * 2, self.radius * 2
            angle_start: self.start_angle
            angle_end: self.circle_progress * self.end_angle * self.creation_direction
        
        Color:
            rgba: self.get_color(self.outline_color,self.balpha)
        Line:
            circle:
                (
                self.center_x, self.center_y,
                self.radius, self.start_angle,
                self.circle_progress * self.end_angle * self.creation_direction
                )
            width: self.line_width


            
''')


class CWidget(Widget):

    get_color = ObjectProperty(get_rgba_color)
    bg_color = ListProperty(['Orange', '300'])
    line_width = NumericProperty(2)
    outline_color = ListProperty(['Orange', '300'])
    balpha = NumericProperty(1)
    radius = NumericProperty(200)
    start_angle = NumericProperty(0)
    end_angle = NumericProperty(360)
    circle_progress = NumericProperty(1)
    creation_direction = NumericProperty(1)

    def __init__(self, **kwargs):
        super(CWidget, self).__init__(**kwargs)
