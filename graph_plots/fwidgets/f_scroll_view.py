'''

@author: dan
'''
from kivy.uix.scrollview import ScrollView
from f_widget import FWidget


class FScrollView(ScrollView, FWidget):

    def __init__(self, **kwargs):
        super(FScrollView, self).__init__(**kwargs)
        self.sp_width = 4

        self.bar_color = self.get_color(['Red', '400'], 0.8)
        self.bar_width = 12  # self.width * .1
        self.bar_inactive_color = self.get_color(['Brown', '300'], 0.4)
        self.bar_margin = 4
        #self.padding = 5
        #self.outline_color = ['Orange', '100']


#    def on_width(self, *args):
#        self.bar_width = self.width * .1
