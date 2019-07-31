# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 2019
@name:   Visualization Functions
@author: Jack Kirby Cook

"""

import numpy as np
import time
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
from IPython.core.display import display

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['geoplot', 'bar3Dplot']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_ticks = lambda labels: [i for i in range(len(labels))]
_axisnames = dict(x = lambda ax, name: ax.set_xlabel(name), 
                   y = lambda ax, name: ax.set_ylabel(name), 
                   z = lambda ax, name: ax.set_zlabel(name))


def geoplot(arraytable, geotable, *args, **kwargs):
    assert arraytable.layers == 1
    assert arraytable.dim == 1
    assert arraytable.shape == (1, len(geotable.index)) or (len(geotable.index), 1)
    assert arraytable.headers['geography'] == geotable.index
    
    raise Exception('UNDER CONSTRUCTION')


def bar3Dplot(arraytable, *args, title=None, barwidth=0.3, speed=0.1, **kwargs):
    assert arraytable.layers == 1
    assert arraytable.dim == 2
    
    xname, yname = arraytable.headerkeys
    zname = arraytable.datakeys[0]
    xlabels, ylabels = list(arraytable.headers.values())
    xticks, yticks = _ticks(xlabels), _ticks(ylabels)
    x, y = np.meshgrid(xticks, yticks)
    x, y = x.ravel(), y.ravel()
    z = np.zeros_like(x + y)
    w = d = barwidth
    h = arraytable.data[arraytable.datakeys[0]].values.flatten()

    fig = Figure(figsize=(13,13))
    FigureCanvas(fig)
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(x, y, z, w, d, h, shade=True, alpha=0.5)
    
    if title: ax.set_title(title)
    ax.set_xlabel(xname)    
    ax.set_ylabel(yname)
    ax.set_zlabel(zname)

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    for angle in range(0, 360, 15): 
        ax.view_init(30, angle)
        display(fig)
        time.sleep(speed)    













