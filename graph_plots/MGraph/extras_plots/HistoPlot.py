'''

@author: dan
'''

from __future__ import division

from kivy.properties import ListProperty, ObjectProperty, NumericProperty

from kivy.graphics import Rectangle, Ellipse, Color, RenderContext
from graph import Plot
from math import log10


class HistoPlot(Plot):
    _grects = ListProperty([])
    _colors = ObjectProperty(None)
    _points = ListProperty([])
    _bar_width = NumericProperty(16)

    def __init__(self, **kwargs):
        super(HistoPlot, self).__init__(**kwargs)
#         self.bind(points=self.ask_draw)
        self.points = self._points
        print self.points

    def create_drawings(self):

        self._grc = RenderContext(
            use_parent_modelview=True,
            use_parent_projection=True)
        with self._grc:
            for i in xrange(len(self._points)):
                self.color = next(self._colors)
                self._gcolor = Color(*self.color)
                self._grects.append(Rectangle())

        return [self._grc]

    def draw(self, *args):
        super(HistoPlot, self).draw(*args)
        points = self._points
        mapX, mapY = HistoPlot.convert(self)

        for i in xrange(len(points)):
            xp0, yp0 = points[i]
            posxp0 = mapX(xp0)
            posyp0 = mapY(yp0)
            l = self._bar_width
            h = posyp0 - mapY(0)

            self._grects[i].pos = posxp0, mapY(0)
            self._grects[i].size = (l, h)

    @staticmethod
    def convert(self):
        params = self._params
        funcx = log10 if params['xlog'] else lambda x: x
        funcy = log10 if params['ylog'] else lambda x: x
        xmin = funcx(params['xmin'])
        ymin = funcy(params['ymin'])
        size = params['size']
        ratiox = (size[2] - size[0]) / float(funcx(params['xmax']) - xmin)
        ratioy = (size[3] - size[1]) / float(funcy(params['ymax']) - ymin)

        def X(x): return (funcx(x) - xmin) * ratiox + size[0]

        def Y(y): return (funcx(y) - ymin) * ratioy + size[1]

        return (X, Y)
