'''


@author: dan
'''
from kivy.uix.widget import Widget
from kivy.properties import (ObjectProperty, OptionProperty, NumericProperty,
                             ListProperty, StringProperty, BooleanProperty)


class ScalableBehaviour(Widget):
    initial_font_size = NumericProperty(64)
    fscale = NumericProperty(.9)
    min_font_size = NumericProperty(32)
    max_font_size = NumericProperty(64)

    def __init__(self, **kwargs):
        super(ScalableBehaviour, self).__init__(**kwargs)
        self.font_size = self.initial_font_size
        self.bind(on_texture_size=self.on_size)
        self.texture_size = self.size

    def on_size(self, *largs):
        # self.texture_update()
        #         self.texture_size= self.size
        self.calculate_font()
        # self.texture_update()
        # print self.font_size , self.texture_size , self.size

    def on_text(self, *largs):
        self.on_size(*largs)

    def calculate_font(self, *largs):
        try:
            if self.texture_size:
                factor = [self.font_size / self.texture_size[0],
                          self.font_size / self.texture_size[1]]
                font_size0 = self.size[0] * self.fscale * factor[0]
                font_size1 = self.size[1] * self.fscale * factor[1]

                if font_size0 < font_size1:
                    self.font_size = max(font_size0, self.min_font_size)
                else:
                    self.font_size = max(font_size1, self.min_font_size)
        except ZeroDivisionError:
            self.font_size = self.min_font_size
