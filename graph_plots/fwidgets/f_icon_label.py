'''


@author: dan
'''
from f_widget import FWidget
from kivy.uix.label import Label
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.button import Button


from kivy.lang import Builder
from f_button import FButton
from utils import get_icon_char, get_rgba_color
from f_scalable import ScalableBehaviour

Builder.load_string('''

<FIconLabel>:

    
    Label:
        id: licon
        font_name: './graph_plots/fwidgets/data/font/fontawesome-webfont.ttf'
        pos: root.pos
        size: root.size
        font_size: root.font_size
        text: root.get_icon(root.icon) if root.icon else ''
        color: root.get_color(root.txt_color)
        
            
      
''')


class FIconLabel(Button, FWidget, ScalableBehaviour):

    icon = StringProperty('')
    get_icon = ObjectProperty(get_icon_char)
    txt_color = ListProperty(['Orange', '100'])
    n_txt_color = ListProperty(['Orange', '100'])
    d_txt_color = ListProperty(['Orange', '400'])

    def __init__(self, **kwargs):

        super(FIconLabel, self).__init__(**kwargs)

        self.get_icon = get_icon_char
        self.background_color = (1, 1, 1, 0)
        self.markup = True
        self.halign = 'center'
        self.valign = 'middle'
        self.color = self.get_color(self.txt_color)
        self.size_hint = 1, 1
        self.font_size = self.height * .8
        self.p_width = 0
        self.txt_color = self.n_txt_color

    def on_txt_color(self, widget, txt_color):
        widget.color = self.get_color(txt_color)
        widget.ids.licon.color = self.get_color(txt_color)

    def on_size(self, widget, size):
        self.size = size
        self.font_size = self.height * .8

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.txt_color = self.d_txt_color
        return super(FIconLabel, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.txt_color = self.n_txt_color
        return super(FIconLabel, self).on_touch_up(touch)
