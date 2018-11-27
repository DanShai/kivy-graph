'''

@author: dan
'''

from __future__ import division

from kivy.properties import NumericProperty, BooleanProperty,\
    BoundedNumericProperty, StringProperty, ListProperty, ObjectProperty,\
    DictProperty, AliasProperty
from kivy.graphics import Rectangle, Ellipse, Color
from graph import Plot
from Engine3D import Engine3D
from math import log10, floor, ceil
import numpy as np


class ScatterPlot3D(Plot):

    _radius = NumericProperty(5)
    _ellipses = ListProperty([])
    _fp = NumericProperty(0)
    _ck = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(ScatterPlot3D, self).__init__(**kwargs)
        self._engine = Engine3D(self.color, self.points, self._radius)
        self.points = np.array(self.points)
        self.bind(_fp=self.ask_draw)
        self.bind(_ck=self.ask_draw)

    def set_ck(self, ck):
        self._ck = ck

    def create_drawings(self):
        from kivy.graphics import PushMatrix, PopMatrix
        #from kivy.utils import get_color_from_hex as rgb
        from kivy.graphics import RenderContext
        self._grc = RenderContext(
            use_parent_modelview=True,
            use_parent_projection=True)

        with self._grc.before:
            PushMatrix()

        with self._grc:
            self._gcolor = Color(*self.color)
            self._ellipses = [Ellipse() for i in xrange(len(self.points))]

        with self._grc.after:
            PopMatrix()

        return [self._grc]

    def draw(self, *args):
        super(ScatterPlot3D, self).draw(*args)

        self._engine.setParams(self.getParams())

        for i in xrange(len(self.points)):

            apoint = self.points[i].copy()
            anellipse = self._ellipses[i]

            #e_params = self.getParams()
            e_rad = self._radius
            self._engine.render(anellipse, apoint, e_rad)

        if self._ck:
            self.update_angle()

    def update_angle(self, *args):
        self._engine.baseAngle = (
            self._engine.baseAngle + self._engine.rotspeed) % 100
        self._fp = (self._fp + 1) % 10

    def getParams(self):

        params = self._params
        funcx = log10 if params['xlog'] else lambda x: x
        funcy = log10 if params['ylog'] else lambda x: x
        xmin = funcx(params['xmin'])
        ymin = funcy(params['ymin'])
        xmax = funcx(params['xmax'])
        ymax = funcy(params['ymax'])

        size = params['size']
        ratiox = (size[2] - size[0]) / float(xmax - xmin)
        ratioy = (size[3] - size[1]) / float(ymax - ymin)

        e_params = (funcx, xmin, xmax, ratiox, funcy, ymin, ymax, ratioy, size)

        return e_params
