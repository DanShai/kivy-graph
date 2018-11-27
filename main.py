
#import os
#os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
#Config.set('graphics', 'width', '400')
#Config.set('graphics', 'height', '400')
Config.set('postproc', 'maxfps', '0')
Config.write()
Window.size = (80 * 16, 80 * 12)
from graph_plots.GUI.graph_test import GraphTest


class graphApp(App):
    def build(self):
        return GraphTest()

    def warn(self, message):
        print message


if __name__ == '__main__':
    app = graphApp()
    app.run()
