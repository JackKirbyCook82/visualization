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

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['createplot', 'createax', 'setnames', 'setlabels', 'showplot', 'addcolorbar']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_DEFAULTCOLOR = 'Y1Gn'

_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)


def showplot(fig): display(fig)


# FACTORY
def createplot(size=(8,8), layout=(1,1), title=None):
    assert all([isinstance(item, tuple) for item in (size, layout)])
    assert all([len(item) == 2 for item in (size, layout)])
    fig = plt.figure(figsize=size)
    fig.suptitle(title)
    setattr(fig, 'layout', layout)
    return fig


def createax(fig, *args, projection=None, **kwargs):
    assert len(fig.axes) <= reduce(lambda x, y: x * y, list(fig.layout))
    projection = projection.lower() if projection else projection
    ax = fig.add_subplot(*fig.layout, len(fig.axes)+1, projection=projection)
    return ax
  

def addcolorbar(fig, colorrange, *args, orientation='horizontal', color=_DEFAULTCOLOR, **kwargs):
    mincolor, maxcolor = colorrange
    norm = Normalize(vmin=mincolor, vmax=maxcolor)
    ncmap = cm.ScalarMappable(norm=norm, cmap=color)
    if orientation == 'vertical':
        fig.subplots_adjust(right=0.85, wspace=0.25, hspace=0.25)    
        cbarax = fig.add_axes([0.9, 0.12, 0.02, 0.74])      
    elif orientation == 'horizontal':
        fig.subplots_adjust(bottom=0.1, wspace=0.25, hspace=0.25)    
        cbarax = fig.add_axes([0.1, 0.05, 0.8, 0.02]) 
    else: raise ValueError(orientation)
    fig.colorbar(ncmap, cax=cbarax, orientation=orientation)   
 
    
def setnames(ax, *args, title=None, names={}, **kwargs):
    axisnames = dict(x = lambda name: ax.set_xlabel(name), 
                     y = lambda name: ax.set_ylabel(name), 
                     z = lambda name: ax.set_zlabel(name))  
    if title: ax.set_title(title)
    for axiskey, axisname in names.items(): 
        if axiskey in axisnames.keys(): axisnames[axiskey](axisname)  
    
   
def setlabels(ax, *args, labels={}, rotations={}, **kwargs):  
    labels = {axis:labels.get(axis, None) for axis in ('x', 'y ', 'z')}
    rotations = {axis:rotations.get(axis, None) for axis in ('x', 'y ', 'z')}
    
    setticks_functions = dict(x='set_xticks', y='set_yticks', z='set_zticks')
    setlabels_functions = dict(x='set_xticklabels', y='set_yticklabels', z='set_zticklabels')
    getlabels_functions = dict(x='get_xticklabels', y='get_yticklabels', z='get_zticklabels')  
    
    for axis, axislabels in labels.items():
        if axislabels is not None: 
            getattr(ax, setticks_functions[axis])(np.arange(0, len(axislabels), 1))
            getattr(ax, setlabels_functions[axis])(axislabels, minor=False)
    
    for axis, rotation in rotations.items():
        if rotation is not None:
            for axistick in getattr(ax, getlabels_functions[axis])(): axistick.set_rotation(rotation)    
            
    

