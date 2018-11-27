'''

@author: dan
'''


from graph_plots.MGraph.extras_plots.graph import Graph
from graph_plots.MGraph.extras_plots.HistoPlot import HistoPlot
import itertools
from kivy.utils import get_color_from_hex as rgb
from graph_plots.fwidgets.f_boxlayout import FBoxLayout


class HistoGraph(FBoxLayout):

    def __init__(self, **kwargs):
        super(HistoGraph, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.size_hint = (1, 1)
        self._colors = itertools.cycle([
            rgb('ccff00'), rgb('e67e22'), rgb('8e44ad'),
            rgb('b7ff00'), rgb('f1c40f'), rgb('6C7A89'),
            rgb('34495e'), rgb('DB0A5B'), rgb('C8F7C5'),
            rgb('BFBFBF')
        ])

        self._graph_theme = {
            'label_options': {
                'color': rgb('99ccff'),  # color of tick labels and titles
                'bold': True},
            # #3B3C3D back ground color of canvas 738ffe
            'background_color': rgb('3B3C3D'),
            'tick_color': rgb('5588ff'),  # ticks and grid
            'border_color': rgb('5588ff')}  # border drawn around each graph

        self._agraph = Graph(xlabel=" ",
                             ylabel=" ",
                             x_ticks_minor=0,
                             x_ticks_major=1,
                             y_ticks_major=2,
                             y_grid_label=True,
                             x_grid_label=True,
                             padding=5,
                             xlog=False,
                             ylog=False,
                             x_grid=True,
                             y_grid=True,
                             xmin=0,
                             xmax=0,
                             ymin=0,
                             ymax=0,
                             **self._graph_theme)

        self.add_widget(self._agraph)

    def clear_plots(self):
        if self._agraph is not None:
            for plot in self._agraph.plots:
                self._agraph.remove_plot(plot)

    def plotHistoGram(self, ldatas, maxX, maxY, Xlabel, Ylabel):

        self.clear_plots()

        self._agraph.xmax = maxX
        self._agraph.ymax = maxY
        self._agraph.xlabel = Xlabel
        self._agraph.ylabel = Ylabel

        plot = HistoPlot(_points=ldatas, _colors=self._colors, _width=16)

        self._agraph.add_plot(plot)
