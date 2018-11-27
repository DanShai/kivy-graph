'''

@author: dan
'''

from __future__ import division

from kivy.properties import NumericProperty, BooleanProperty,\
    BoundedNumericProperty, StringProperty, ListProperty, ObjectProperty,\
    DictProperty, AliasProperty
from kivy.graphics import Rectangle, Ellipse, Color
from graph import Plot
from math import log10, floor, ceil
import numpy as np


class ScatterPlot(Plot):
    _radius = NumericProperty(5)
    _ellipses = ListProperty([])

    def __init__(self, **kwargs):
        super(ScatterPlot, self).__init__(**kwargs)

    def create_drawings(self):
        from kivy.graphics import RenderContext

        self._grc = RenderContext(
            use_parent_modelview=True,
            use_parent_projection=True)

        with self._grc:
            self._gcolor = Color(*self.color)
            self._ellipses = [Ellipse() for i in xrange(len(self.points))]

        return [self._grc]

    def draw(self, *args):
        super(ScatterPlot, self).draw(*args)
        params = self._params
        funcx = log10 if params['xlog'] else lambda x: x
        funcy = log10 if params['ylog'] else lambda x: x
        xmin = funcx(params['xmin'])
        ymin = funcy(params['ymin'])
        size = params['size']
        ratiox = (size[2] - size[0]) / float(funcx(params['xmax']) - xmin)
        ratioy = (size[3] - size[1]) / float(funcy(params['ymax']) - ymin)
        for i in xrange(len(self.points)):
            x, y = self.points[i]
            pos = ((funcx(x) - xmin) * ratiox + size[0],
                   (funcy(y) - ymin) * ratioy + size[1])
            self._ellipses[i].pos = pos
            self._ellipses[i].size = (self._radius, self._radius)
