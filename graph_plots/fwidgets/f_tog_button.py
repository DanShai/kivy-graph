'''

@author: dan
'''
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Rectangle, Color, Ellipse
from utils import get_icon_char, get_rgba_color
from f_scalable import ScalableBehaviour

Builder.load_string('''


<FTogButton>:
    font_name: './graph_plots/fwidgets/data/font/fsix.ttf'

    canvas.before:
        Color:
            rgba: self.get_color(self.n_color,self.balpha) if self.state == 'normal' else self.get_color(self.d_color,self.balpha)
        Rectangle:
            pos: self.pos[0],self.pos[1]
            size: self.width,self.height
        Color:
            rgba: self.get_color(self.outline_color,self.balpha)
        Line:
            rounded_rectangle: [self.x , self.y, self.width , self.height, sp(self.sp_round)]
            width: sp(self.sp_width) if self.sp_width else sp(1)
    Label:
        id: micon
        font_name:'./graph_plots/fwidgets/data/font/fontawesome-webfont.ttf'
        pos: root.pos[0]+root.width - self.width, root.pos[1]+root.height-self.height
        #pos: root.pos[0]+root.width-20,root.pos[1]+root.height-20
        size: 40,40
        font_size: self.height * .75
        text: root.get_icon(root.icon) if root.icon else ''
        color: root.get_color(root.txt_color)
        
        

''')


class FTogButton(ToggleButton, ScalableBehaviour):

    n_color = ListProperty(['Red', '300'])
    d_color = ListProperty(['Orange', '600'])
    icon = StringProperty('')
    get_icon = ObjectProperty(get_icon_char)
    get_color = ObjectProperty(get_rgba_color)
    balpha = NumericProperty(1)
    txt_color = ListProperty(['Orange', '100'])
    outline_color = ListProperty(['Red', '400'])
    sp_width = NumericProperty(1)
    sp_round = NumericProperty(2)

    def __init__(self, **kwargs):

        super(FTogButton, self).__init__(**kwargs)
        self.get_color = get_rgba_color
        self.get_icon = get_icon_char
        self.background_color = (1, 1, 1, 0)
        self.ripple_base_color = self.d_color

        self.markup = True
        self.halign = 'center'
        self.valign = 'middle'
        self.color = self.get_color(self.txt_color, self.balpha)
        self.size_hint = 1, 1
        self.font_size = self.height * .75

    def on_txt_color(self, widget, color):
        self.color = self.get_color(color, self.balpha)
        self.ids.micon.color = self.get_color(color, self.balpha)

    def get_font(self, font_file):
        return construct_target_file_name(font_file, None)
