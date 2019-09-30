# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 2019
@name:   Visualization Figures
@author: Jack Kirby Cook

"""

import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
from IPython.core.display import display

from utilities.strings import uppercase

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['createplot', 'createax', 'setnames', 'setticks', 'setlabels', 'showplot', 'xticks', 'yticks', 'zticks']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""

_MAPCOLOR = 'YlGn'
_ROADCOLOR = 'DarkRed'
_WATERCOLOR = 'DarkBlue'


_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)

def config(*args, mapcolor=_MAPCOLOR, roadcolor=_ROADCOLOR, watercolor=_WATERCOLOR, **kwargs):
    global _MAPCOLOR
    global _ROADCOLOR
    global _WATERCOLOR
    _MAPCOLOR, _ROADCOLOR, _WATERCOLOR = mapcolor, roadcolor, watercolor 
    
    
def showplot(fig): display(fig)

def xticks(ax): return ax.get_xticks()
def yticks(ax): return ax.get_yticks() 
def zticks(ax): return ax.get_zticks()


# FACTORY
def createplot(size=(8,8), layout=(1,1), title=None):
    assert all([isinstance(item, tuple) for item in (size, layout)])
    assert all([len(item) == 2 for item in (size, layout)])
    fig = plt.figure(figsize=size)
    fig.suptitle(uppercase(title, withops=True))
    setattr(fig, 'layout', layout)
    return fig


def createax(fig, *args, projection=None, **kwargs):
    assert len(fig.axes) <= reduce(lambda x, y: x * y, list(fig.layout))
    projection = projection.lower() if projection else projection
    ax = fig.add_subplot(*fig.layout, len(fig.axes)+1, projection=projection)
    return ax
  

def addcolorbar(fig, colorrange, *args, orientation='horizontal', **kwargs):
    mincolor, maxcolor = colorrange
    norm = Normalize(vmin=mincolor, vmax=maxcolor)
    ncmap = cm.ScalarMappable(norm=norm, cmap=_MAPCOLOR)
    if orientation == 'vertical':
        fig.subplots_adjust(right=0.85, wspace=0.25, hspace=0.25)    
        cbarax = fig.add_axes([0.9, 0.12, 0.02, 0.74])      
    elif orientation == 'horizontal':
        fig.subplots_adjust(bottom=0.1, wspace=0.25, hspace=0.25)    
        cbarax = fig.add_axes([0.1, 0.05, 0.8, 0.02]) 
    else: raise ValueError(orientation)
    fig.colorbar(ncmap, cax=cbarax, orientation=orientation)   
    
      
def setnames(ax, title=None, **names):
    axisnames = dict(x = lambda name: ax.set_xlabel(uppercase(name, withops=True)), 
                     y = lambda name: ax.set_ylabel(uppercase(name, withops=True)), 
                     z = lambda name: ax.set_zlabel(uppercase(name, withops=True)))  
    if title: ax.set_title(uppercase(title, withops=True))
    for axiskey, axisname in names.items(): 
        if axiskey in axisnames.keys(): axisnames[axiskey](axisname)  
    
    
def setticks(ax, **ticks):
    function = lambda num: np.arange(0, num, 1)
    axisticks = dict(x = lambda num: ax.set_xticks(function(num)), 
                     y = lambda num: ax.set_yticks(function(num)), 
                     z = lambda num: ax.set_zticks(function(num))) 
    for axiskey, axislen in ticks.items(): 
        if axiskey in axisticks.keys(): axisticks[axiskey](axislen)


def setlabels(ax, **labels):
    axislabels = dict(x = lambda xlabels: ax.set_xticklabels(xlabels, minor=False), 
                      y = lambda ylabels: ax.set_yticklabels(ylabels, minor=False), 
                      z = lambda zlabels: ax.set_zticklabels(zlabels, minor=False))     
    for axiskey, axislbls in labels.items(): 
        if axiskey in axislabels.keys(): axislabels[axiskey](axislbls)






 
    
    
