'''


@author: dan
'''
from kivy.uix.widget import Widget
from kivy.lang import Builder


from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from utils import get_rgba_color


Builder.load_string('''
<FWidget>:
    canvas.before:
        Color:
            rgba: self.get_color(self.bg_color,self.balpha)
        Rectangle:
            pos: self.pos
            size: self.size
            
        Color:
            rgba: self.get_color(self.outline_color,self.balpha)
        Line:
            rounded_rectangle: (self.x , self.y, self.width , self.height, self.sp_round)
            width: self.p_width if self.p_width else 1
            
''')


class FWidget(Widget):

    get_color = ObjectProperty(get_rgba_color)
    bg_color = ListProperty(['Grey', '000'])  # Black
    p_width = NumericProperty(1)
    outline_color = ListProperty(['Grey', '111'])  # White
    sp_round = NumericProperty(1)
    balpha = NumericProperty(1)

    def __init__(self, **kwargs):
        super(FWidget, self).__init__(**kwargs)
        #eng = Engine3D(mcolor = self.get_color(['Red', '700'],self.balpha))
        #self.texture = eng.makeTexture()
