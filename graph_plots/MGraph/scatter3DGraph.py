'''

@author: dan
'''


from extras_plots.graph import Graph
from extras_plots.ScatterPlot3D import ScatterPlot3D

import itertools
from kivy.utils import get_color_from_hex as rgb
from graph_plots.fwidgets.f_boxlayout import FBoxLayout
import numpy as np


class Scatter3DGraph(FBoxLayout):

    def __init__(self, **kwargs):
        super(Scatter3DGraph, self).__init__(**kwargs)

        self.orientation = "vertical"

        self._colors = itertools.cycle([rgb('34495e'), rgb('f1c40f'), rgb(
            '6C7A89'), rgb('BFBFBF'), rgb('00CCFF'), rgb('e67e22')])

        self._graph_theme = {
            'label_options': {
                'color': rgb('99ccff'),  # color of tick labels and titles
                'bold': True},
            # 3B3C3D back ground color of canvas 738ffe
            'background_color': rgb('3B3C3D'),
            'tick_color': rgb('5588ff'),  # ticks and grid
            'border_color': rgb('5588ff')}  # border drawn around each graph

        self._agraph = None

    def clear_all(self):
        if self._agraph is not None:
            for plot in self._agraph.plots:
                self._agraph.remove_plot(plot)

    def plotScatter3D(self, X, Y):
        y = Y.ravel()
        m = int(np.min(X)) - 1
        M = int(np.max(X)) + 1
        if self._agraph is not None:
            self.clear_all()
            self.remove_widget(self._agraph)
        self._agraph = Graph(xlabel='X1',
                             ylabel='X2',
                             x_ticks_minor=0,
                             x_ticks_major=1,
                             y_ticks_major=1,
                             y_grid_label=True,
                             x_grid_label=True,
                             padding=5,
                             xlog=False,
                             ylog=False,
                             x_grid=False,
                             y_grid=False,
                             xmin=m,
                             xmax=M,
                             ymin=m,
                             ymax=M,
                             **self._graph_theme)

        u = np.unique(y)
        for i in u:
            # self._agraph._clear_buffer()
            Xi = X[y == i, :]
            #Xi = Xi[Xi[:, 0].argsort()]
            Xi = Xi[:, :3]
            Xi = list(map(tuple, Xi))
            plot = ScatterPlot3D(color=next(self._colors),
                                 _radius=16, points=Xi)
            self._agraph.add_plot(plot)

        self.add_widget(self._agraph)
