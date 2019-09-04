# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 2019
@name:   Visualization Figures
@author: Jack Kirby Cook

"""

import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
from IPython.core.display import display


__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['createplot', 'createax', 'setnames', 'setticks', 'setlabels', 'showplot', 'xticks', 'yticks', 'zticks']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)

def showplot(fig): display(fig)

def xticks(ax): return ax.get_xticks()
def yticks(ax): return ax.get_yticks() 
def zticks(ax): return ax.get_zticks()


# FACTORY
def createplot(size=(8,8), layout=(1,1)):
    assert all([isinstance(item, tuple) for item in (size, layout)])
    assert all([len(item) == 2 for item in (size, layout)])
    fig = plt.figure(figsize=size)
    setattr(fig, 'layout', layout)
    return fig


def createax(fig, *args, projection=None, **kwargs):
    assert len(fig.axes) <= reduce(lambda x, y: x * y, list(fig.layout))
    projection = projection.lower() if projection else projection
    ax = fig.add_subplot(*fig.layout, len(fig.axes)+1, projection=projection)
    return ax


def setnames(ax, title=None, **names):
    axisnames = dict(x = lambda name: ax.set_xlabel(name.upper()), 
                     y = lambda name: ax.set_ylabel(name.upper()), 
                     z = lambda name: ax.set_zlabel(name.upper()))    
    if title: ax.set_title(title.upper())
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






 
    
    
