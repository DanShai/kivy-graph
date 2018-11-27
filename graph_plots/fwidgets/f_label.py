'''


@author: dan
'''

from f_widget import FWidget
from kivy.uix.label import Label
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.button import Button

from utils import get_icon_char, get_rgba_color
from f_scalable import ScalableBehaviour

from kivy.lang import Builder

Builder.load_string('''

<FLabel>:
    font_name: './graph_plots/fwidgets/data/font/fsix.ttf'

    
    Label:
        id: micon
        font_name: './graph_plots/fwidgets/data/font/fontawesome-webfont.ttf'
        pos: root.pos[0]+2.*root.width/3.,root.pos[1]+2.*root.height/3.
        size: root.width/3.,root.height/3.
        font_size: self.height * .75
        text: root.get_icon(root.icon) if root.icon else ''
        color: root.get_color(root.txt_color)
        
            
      
''')


class FLabel(FWidget, Button, ScalableBehaviour):

    icon = StringProperty('')
    get_icon = ObjectProperty(get_icon_char)
    txt_color = ListProperty(['Orange', '100'])

    def __init__(self, **kwargs):

        super(FLabel, self).__init__(**kwargs)

        self.get_icon = get_icon_char
        self.background_color = (1, 1, 1, 0)
        self.markup = True
        self.halign = 'center'
        self.valign = 'middle'
        self.color = self.get_color(self.txt_color, self.balpha)
        self.size_hint = 1, 1
        self.font_size = self.initial_font_size  # self.height * .75
        # self.outline_color = ['Blue','400']
        self.sp_width = 1
        self.p_width = 1
        # self.text_size = self.size
        # self.bind(txt_color=self.on_color_changed)

#     def on_color_changed(self, widget, color):
#         self.ids.micon.color = self.get_color(color)

    def on_txt_color(self, widget, color):
        self.color = self.get_color(color, self.balpha)
        self.ids.micon.color = self.get_color(color, self.balpha)

    def get_font(self, font_file):
        return construct_target_file_name(font_file, None)
