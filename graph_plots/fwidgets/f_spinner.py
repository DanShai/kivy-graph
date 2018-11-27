
'''

@author: dan
'''
from f_widget import FWidget
from kivy.uix.spinner import Spinner, SpinnerOption
from f_button import FButton
from kivy.lang import Builder

Builder.load_string('''
#:import Factory kivy.factory.Factory

<MyFSpinnerOption@SpinnerOption+FWidget>:
    bg_color: ['Red','300']
    outline_color: ['White','500']
    background_color: 1,1,1,0
    txt_color: ['Orange','100']

<FSpinner>:
    txt_color: ['Orange','100']
    option_cls: Factory.get("MyFSpinnerOption")
    animate_me: False
      
''')


class FSpinner(Spinner, FButton):

    def __init__(self, **kwargs):
        super(FSpinner, self).__init__(**kwargs)
        self.outline_color = ['Grey', '111']
