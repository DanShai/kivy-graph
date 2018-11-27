'''


@author: dan
'''
from graph_plots.fwidgets.f_boxlayout import FBoxLayout
from graph_plots.fwidgets.f_grid_layout import FGridLayout
from graph_plots.fwidgets.f_spinner import FSpinner
from graph_plots.fwidgets.f_label import FLabel
from graph_plots.fwidgets.f_button import FButton
from graph_plots.fwidgets.f_tog_button import FTogButton
from graph_plots.MGraph.histoGraph import HistoGraph
from graph_plots.MGraph.lineGraph import LineGraph
from graph_plots.MGraph.scatter2DGraph import Scatter2DGraph
from graph_plots.MGraph.scatter3DGraph import Scatter3DGraph
from kivy.base import EventLoop
from kivy.lang import Builder
from graph_plots.Data.data import Adata
import numpy as np

Builder.load_file('./graph_plots/GUI/graph_test.kv')


class GraphTest(FBoxLayout):
    def __init__(self, **kwargs):

        EventLoop.ensure_window()
        super(GraphTest, self).__init__(**kwargs)
        self._hist_graph = self.ids.hist_graph
        self._line_graph = self.ids.line_graph
        self._scatter2d_graph = self.ids.deuxd_graph
        self._scatter3d_graph = self.ids.troisd_graph
        self._spinner = self.ids.line_spinner
        self._anim_but = self.ids.animate_button
        self._Adata = Adata()
        self._ldata = self._Adata.make1DDatas()
        self._s3data = self._Adata.make3DDatas()
        self._s2data = self._Adata.make2DDatas()
        self._hdata = self._Adata.makeHistData()
        self.play = True
        self.make_plots()

    def change_plot(self, instance, value):
        val = str(value)
        self._line_graph.set_mode(val)
        X = self._ldata["X"]
        Y = self._ldata["Y"]
        self._line_graph.plotLine(X, Y)

    def animate(self, instance, value):

        self.play = not self.play
        if instance.state == "down":
            instance.text = "Pause"
            instance.icon = "fa-pause"
        else:
            instance.text = "Play"
            instance.icon = "fa-play"

        self.toggle3Danimation()

    def toggle3Danimation(self):
        if self._scatter3d_graph._agraph is not None:
            for plot in self._scatter3d_graph._agraph.plots:
                if hasattr(plot, '_ck'):
                    plot.set_ck(self.play)

    def make_plots(self):
        self.draw_line()
        self.draw_hist()
        self.draw_scatter2d()
        self.draw_scatter3d()

    def draw_line(self):
        X = self._ldata["X"]
        Y = self._ldata["Y"]
        self._line_graph.plotLine(X, Y)

    def draw_hist(self):
        Xlabel = " Number "
        Ylabel = " Frequency "
        hdata = self._hdata
        X0 = self._ldata["X"]
        Y0 = self._ldata["Y"]
        maxX = int(np.max(X0))
        maxY = int(np.max(Y0))
        self._hist_graph.plotHistoGram(hdata, maxX, maxY, Xlabel, Ylabel)

    def draw_scatter2d(self):
        X2 = self._s2data["X"]
        Y2 = self._s2data["Y"]
        self._scatter2d_graph.plotScatter(X2, Y2)

    def draw_scatter3d(self):
        X3 = self._s3data["X"]
        Y3 = self._s3data["Y"]
        print X3.shape, Y3.shape
        self._scatter3d_graph.plotScatter3D(X3, Y3)
