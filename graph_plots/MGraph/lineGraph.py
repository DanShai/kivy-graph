
from extras_plots.graph import Graph, SmoothLinePlot, MeshLinePlot, LinePlot, MeshStemPlot
import itertools
from kivy.utils import get_color_from_hex as rgb
from graph_plots.fwidgets.f_boxlayout import FBoxLayout
import numpy as np
from kivy.properties import StringProperty


class LineGraph(FBoxLayout):
    # mode = StringProperty("SmoothLine")

    def __init__(self, **kwargs):
        super(LineGraph, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.mode = "SmoothLine"

        self.opts = {"Line": LinePlot, "SmoothLine": SmoothLinePlot,
                     "Mesh": MeshLinePlot, "Stem": MeshStemPlot}

        self._colors = itertools.cycle([rgb('8e44ad'), rgb('b7ff00'), rgb('DB0A5B'),
                                        rgb('C8F7C5'), rgb(
                                            '34495e'), rgb('f1c40f'),
                                        rgb('6C7A89'), rgb(
                                            'BFBFBF'), rgb('00CCFF'),
                                        rgb('e67e22')
                                        ])

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

    def set_mode(self, m):
        self.mode = m

    def plotLine(self, X, Y):

        if self._agraph is not None:
            self.clear_all()
            self.remove_widget(self._agraph)

        mx = int(np.min(X)) - 1
        Mx = int(np.max(X)) + 1

        my = int(np.min(Y)) - 1
        My = int(np.max(Y)) + 1

        pointss = zip(X.ravel(), Y.ravel())
        #print pointss
        #plot = SmoothLinePlot(color=next(self._colors))
        plotmode = self.opts[self.mode]
        plot = plotmode(color=next(self._colors))

        plot.points = pointss
        self._agraph = Graph(xlabel='X',
                             ylabel='Y',
                             x_ticks_minor=0,
                             x_ticks_major=1,
                             y_ticks_major=10,
                             y_grid_label=True,
                             x_grid_label=True,
                             padding=5,
                             xlog=False,
                             ylog=False,
                             x_grid=True,
                             y_grid=True,
                             xmin=mx,
                             xmax=Mx,
                             ymin=my,
                             ymax=My,
                             **self._graph_theme)

        self._agraph.add_plot(plot)
        self.add_widget(self._agraph)
