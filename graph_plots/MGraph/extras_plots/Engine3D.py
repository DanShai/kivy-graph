'''

@author: dan
'''

from __future__ import division
from random import randint, random
from kivy.graphics import Mesh, Color, Rectangle, Ellipse, Scale, Translate
from kivy.graphics.texture import Texture
import numpy as np


class Engine3D:

    def __init__(self, mcolor, points, _rad, **kwargs):
        self._radius = _rad
        self.points = points
        self.baseAngle = random()*2
        self.color = mcolor
        self.rotspeed = .005
        self.trspeed = .01
        self.eye = np.array([100, 10, 1000])
        self.tex = self.makeTexture()

        self._params = None

    def setParams(self, p):
        self._params = p

    def rotate(self, apoint, axis, theta):
        axis = np.asarray(axis)
        axis = axis/np.sqrt(np.dot(axis, axis))
        a = np.cos(theta/2.0)
        b, c, d = -axis*np.sin(theta/2.0)
        aa, bb, cc, dd = a*a, b*b, c*c, d*d
        bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
        M = np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                      [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                      [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

        #v = [3, 5, 0]
        #axis = [4, 4, 1]
        #theta = 1.2

        return np.dot(M, apoint)

    def project(self, apoint):

        z = apoint[2]
        percpective = 1 / (1 + z / (self.eye[2]+self.eye[2]))
        apoint[:2] = (apoint[:2] - self.eye[:2]) * percpective + self.eye[:2]

        return apoint, percpective

    def render(self, anellipse, apoint, _rad):

        funcx, xmin, xmax, ratiox, funcy, ymin, ymax, ratioy, size = self._params
        rx = (xmin+xmax)/2
        ry = (ymin+ymax)/2

        apoint = self.rotate(apoint, [rx, ry, 1], self.baseAngle)
        #apoint = self.rotate(apoint, [0, 0, 1], self.baseAngle)
        apoint, perspective = self.project(apoint)

        x, y = apoint[:2]
        apoint[:2] = (funcx(x) - xmin) * ratiox + \
            size[0], (funcy(y) - ymin) * ratioy + size[1]

        #print "REAL: " , apoint
        #print "TRANSFORMED: " , x,y, z
        _center = apoint
        _radius = _rad/perspective

        self.drawEllipseGradient(anellipse, _center, _radius)

    def makeSpotLight(self, x, y, mux=.5, muy=.5, sigX=.1, sigY=.1, n=.2, algo="Gaussian"):

        if algo == "Gaussian":
            d = 1. - np.exp(- (((x-mux) ** 2) / sigX +
                               (((y-muy)) ** 2) / sigY))
        else:
            d = ((x-mux) ** 2 + (y-muy) ** 2) ** n

        return d

    def makeTexture(self):

        size = (4, 4)  # size = at least 4 times sigxy
        caa = random()  # .6
        ccc = caa*np.array(self.color)
        ccc[-1] = .5
        border_color = ccc
        light_color = np.array((1, 1, 1, 1))

        w, h = size         # Screen size
        r = float(h) / w
        # Screen coordinates: x0, y0, x1, y1.
        S = (-1.,   -r + .25,   1.,   r + .25)
        xx = np.linspace(S[0], S[2], w)
        yy = np.linspace(S[1], S[3], h)
        y, x = np.meshgrid(yy, xx)

        d = self.makeSpotLight(x, y, random(), random(),
                               random(), random(), random(), "Gaussian")

        #colors = np.outer(light_color,(1-d)) + np.outer(border_color,d)
        #arr = buf.T.ravel()

        colors = np.outer(1-d, light_color) + np.outer(d, border_color)
        colors *= 255


#         print "colrs: ", colors.shape
        buf = np.clip(colors, 0, 255).astype(np.uint8)
        arr = buf.ravel()
#         print "arr: ", arr.shape
        data = arr.tostring()
        tex = Texture.create(size=size, colorfmt='rgba')
        tex.blit_buffer(data, colorfmt='rgba', bufferfmt='ubyte')

        return tex

    def drawEllipseGradient(self, anellipse, _centerxy, _rad):
        x, y, z = _centerxy
        _size = (_rad, _rad)
        pos = (x, y)
        #Translate(x, y)
        anellipse.pos = pos
        anellipse.size = _size
        anellipse.texture = self.tex
