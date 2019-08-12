# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 2019
@name:   Visualization Objects
@author: Jack Kirby Cook

"""

import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from IPython.core.display import display

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = []
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)


def showplot(fig): display(fig)

def xticks(ax): return ax.get_xticks()
def yticks(ax): return ax.get_yticks() 


# FACTORY
def createplot(figsize):
    fig = Figure(figsize=figsize)
    FigureCanvas(fig)
    return fig

def createax(fig, *args, axsize=(1,1), projection, axisshape, **kwargs):
    assert isinstance(axsize, tuple)
    assert len(axsize) == 2
    assert isinstance(axisshape, tuple)
    assert len(axisshape) == 2
    ax = fig.add_subplot(*axsize, len(fig.axes)+1, projection=projection)
    xticks, yticks = [np.arange(0, axislen, 1) for axislen in axisshape]
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    return ax

def createnames(ax, *args, title=None, names={}, **kwargs):
    assert isinstance(names, dict)
    axisnames = dict(x = lambda name: ax.set_xlabel(name), y = lambda name: ax.set_ylabel(name), z = lambda name: ax.set_zlabel(name))    
    if title: ax.set_title(title)
    for axiskey, axisname in names.items(): axisnames[axiskey](axisname)     


# PLOTS
def bar3Dplot(ax, data, *args, barsize=(1,1), shade=True, alpha=0.5, **kwargs):
    assert isinstance(barsize, tuple)
    assert len(barsize) == 2
    assert isinstance(shade, bool)
    assert isinstance(data, np.ndarray)
    assert data.dim == 1
    x, y = np.meshgrid(xticks(ax), yticks(ax))
    x, y = x.ravel(), y.ravel()
    z = np.zeros_like(x + y)
    w, d = barsize
    h = data
    ax.bar3d(x, y, z, w, d, h, shade=shade, alpha=alpha)   





            
#def __call__(self, arraytable, *args, **kwargs):
#    offsets = np.arange(0, self.__xlim)
#    for index, datakey, dataarray in zip(range(arraytable.dim), arraytable.datakeys, arraytable.dataarrays.values()):
#        pass
                    
#    offsets = np.arange(0, len(self.data))
#    nonoffsets = np.zeros_like(offsets)        
#    xoffsets = offsets if self.__xlayer else nonoffsets
#    yoffsets = nonoffsets if self.__xlayer else offsets
#    for index, arraytable in zip(range(len(self.data)), self.data): 
#        self.__plotdata(arraytable.values(), *args, xoffset=xoffsets[index]*self.__xlim, yoffset=yoffsets[index]*self.__ylim, **kwargs)
   








