'''

@author: dan
'''

from f_scroll_view import FScrollView
from f_boxlayout import FBoxLayout
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty, ObjectProperty
from pygments.lexers.graphics import GLShaderLexer
from unidecode import unidecode
from mcodeinput import MCodeInput
import re


Builder.load_string('''
<FScrollCodeInput>:
    FScrollView:
        id: scrlv
        scroll_type: ['bars', 'content']
        MCodeInput:
            id: ti
            font_size: 16
            lexer: root.lexer
            style_name: root.style_name
            text: root.rm_non_ascii(root.text)
            size_hint: 1 , None
            height: max(self.minimum_height, scrlv.height)
            padding: '5dp'
            focus: True 
            on_cursor_row: root.change_scroll_y(ti, scrlv)
            use_bubble: True

''')


class FScrollCodeInput(FBoxLayout):
    text = StringProperty("")
    lexer = ObjectProperty(GLShaderLexer())
    style_name = StringProperty("monokai")

    def __init__(self, **kwargs):
        super(FScrollCodeInput, self).__init__(**kwargs)

    def on_text(self, *args):
        self.ids.ti.text = self.rm_non_ascii(self.text)

    def on_lexer(self, *args):
        self.ids.ti.lexer = self.lexer

    def on_style_name(self, *args):
        self.ids.ti.style_name = self.style_name

    def change_scroll_y(self, ti, scrlv):
        y_cursor = ti.cursor_pos[1]
        y_bar = scrlv.scroll_y * (ti.height-scrlv.height)
        if ti.height > scrlv.height:
            if y_cursor >= y_bar + scrlv.height:
                dy = y_cursor - (y_bar + scrlv.height)
                scrlv.scroll_y = scrlv.scroll_y + \
                    scrlv.convert_distance_to_scroll(0, dy)[1]
            if y_cursor - ti.line_height <= y_bar:
                dy = (y_cursor - ti.line_height) - y_bar
                scrlv.scroll_y = scrlv.scroll_y + \
                    scrlv.convert_distance_to_scroll(0, dy)[1]

    def rm_non_ascii(self, text):
        return re.sub(r'[^\x00-\x7f]', r'', text)
