import sys
import numpy
from PyQt4 import QtGui
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.patches import Circle


class SelectablePoint:
    def __init__(self, xy, label, fig):
        self.point = Circle( (xy[0], xy[1]), 0.15, figure=fig)
        self.label = label
        self.cidpress = self.point.figure.canvas.mpl_connect('button_press_event', self.onClick)

    def onClick(self, e):
        if self.point.contains(e)[0]:
            print self.label


class ScatterPlot(FigureCanvas):

    def __init__(self, parent=None):

        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


        self.axes = self.fig.add_subplot(111)
        xlim = [0,10]
        ylim = [0,10]
        self.axes.set_xlim(xlim)
        self.axes.set_ylim(ylim)
        self.axes.set_aspect( 1 )


class matplotlibWidget(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = ScatterPlot()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)