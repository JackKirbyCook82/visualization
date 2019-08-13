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
from functools import update_wrapper

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = []
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)


def showplot(fig): display(fig)

def xticks(ax): return ax.get_xticks()
def yticks(ax): return ax.get_yticks() 
def zticks(ax): return ax.get_zticks()

# FACTORY
def createplot(x, y):
    fig = Figure(figsize=(x,y))
    FigureCanvas(fig)
    return fig

def createax(fig, *args, axsize=(1,1), projection=None, **kwargs):
    assert isinstance(axsize, tuple)
    assert len(axsize) == 2
    ax = fig.add_subplot(*axsize, len(fig.axes)+1, projection=projection)
    return ax

def setshape(ax, ticks):
    assert isinstance(ticks, dict)
    axisticks = dict(x = lambda items: ax.set_xticks(items), 
                     y = lambda items: ax.set_yticks(items), 
                     z = lambda items: ax.set_zticks(items))        
    for axiskey, axisitems in ticks.items(): axisticks[axiskey](axisitems)

def createnames(ax, *args, title=None, names={}, **kwargs):
    assert isinstance(names, dict)
    axisnames = dict(x = lambda name: ax.set_xlabel(name), 
                     y = lambda name: ax.set_ylabel(name), 
                     z = lambda name: ax.set_zlabel(name))    
    if title: ax.set_title(title)
    for axiskey, axisname in names.items(): axisnames[axiskey](axisname)     

def numpydata(dim):
    def decorator(function):
        def wrapper(ax, data, *args, **kwargs):
            assert isinstance(data, np.ndarray)
            assert data.dim == dim
            return function(ax, data, *args, **kwargs)
        return wrapper
        update_wrapper(wrapper, function)
    return decorator
 

# PLOTS
@numpydata(2)
def violinplot(ax, data, *args, showmeans=True, showmedians=False, showextrema=True, **kwargs):
    assert all([isinstance(item, bool) for item in (showmeans, showmedians, showextrema)])
    ax.violinplot(data, showmeans=showmeans, showmedians=showmedians, showextrema=showextrema)

@numpydata(1)
def barplot(ax, data, *args, size=1, **kwargs):
    assert isinstance(size, float)
    x = np.arange(0, len(data), 1)
    z = np.zeros_like(data)
    w = size
    h = data    
    ax.bar(x, h, width=w, bottom=z)    
    
@numpydata()
def line3Dplot(ax, data, *args, **kwargs):
    pass

@numpydata()
def scatter3Dplot(ax, data, *args, **kwargs):
    pass
    
@numpydata(2)
def bar3Dplot(ax, data, *args, size=(1,1), offset=(0,0), shade=True, alpha=0.5, **kwargs):
    assert isinstance(size, tuple)
    assert len(size) == 2
    assert isinstance(offset, tuple)
    assert len(offset) == 2
    assert isinstance(shade, bool)
    assert isinstance(alpha, float)
    x, y = np.meshgrid(*[np.arange(0, len(length), 1) for length in data.shape])
    x, y = x.ravel(), y.ravel()
    z = np.zeros_like(x + y)
    w, d = size
    h = data.flatten()
    ax.bar3d(x, y, z, w, d, h, shade=shade, alpha=alpha)   

@numpydata(2)
def surface3Dplot(ax, data, *args, shade=True, alpha=0.5, **kwargs):
    assert isinstance(shade, bool)
    assert isinstance(alpha, float)
    x, y = np.meshgrid(*[np.arange(0, len(length), 1) for length in data.shape])
    z = data
    ax.plot_surface(x, y, z, shade=shade, alpha=alpha)      
    
    
    

    
    
    
    
