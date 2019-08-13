# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 2019
@name:   Visualization Objects
@author: Jack Kirby Cook

"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from IPython.core.display import display

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['createplot', 'createax', 'setnames', 'setticks', 'setlabels', 'violinplot', 'barplot', 'lineplot', 'bar3Dplot', 'surface3Dplot']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)

def showplot(fig): display(fig)

def xticks(ax): return ax.get_xticks()
def yticks(ax): return ax.get_yticks() 
def zticks(ax): return ax.get_zticks()


# FACTORY
def createplot(x, y):
    fig = plt.figure(figsize=(x,y))
    return fig


def createax(fig, *args, axsize=(1,1), projection=None, **kwargs):
    assert isinstance(axsize, tuple)
    assert len(axsize) == 2
    ax = fig.add_subplot(*axsize, len(fig.axes)+1, projection=projection.lower())
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
        

# PLOTS
def violinplot(ax, data, *args, showmeans=True, showmedians=False, showextrema=True, **kwargs):
    assert isinstance(data, list)
    assert all([isinstance(item, np.ndarray) for item in data])
    assert all([isinstance(item, bool) for item in (showmeans, showmedians, showextrema)])
    ax.violinplot(data, showmeans=showmeans, showmedians=showmedians, showextrema=showextrema)


def barplot(ax, data, *args, size=1, **kwargs):
    assert isinstance(data, np.ndarray)
    assert data.ndim == 1    
    assert isinstance(size, float)
    x = np.arange(0, len(data), 1)
    z = np.zeros_like(data)
    w = size
    h = data    
    ax.bar(x, h, width=w, bottom=z)    
    
    
def lineplot(ax, data, *args, **kwargs):
    assert isinstance(data, list)
    assert all([isinstance(item, np.ndarray) for item in data])
    assert len(data) <= 3
    ax.plot(*data)


def scatterplot(ax, data, *args, marker='•', **kwargs):
    assert isinstance(data, list)
    assert all([isinstance(item, np.ndarray) for item in data])    
    assert len(data) <= 3
    ax.scatter(*data, marker=marker)
    

def bar3Dplot(ax, data, *args, size=(1,1), offset=(0,0), shade=True, alpha=0.5, **kwargs):
    assert isinstance(data, np.ndarray)
    assert data.ndim == 2        
    assert isinstance(size, tuple)
    assert len(size) == 2
    assert isinstance(offset, tuple)
    assert len(offset) == 2
    assert isinstance(shade, bool)
    assert isinstance(alpha, float)
    x, y = np.meshgrid(*[np.arange(0, length, 1) for length in data.shape])
    x, y = x.ravel() + offset[0], y.ravel() + offset[1]
    z = np.zeros_like(x + y)
    w, d = size
    h = data.flatten()
    ax.bar3d(x-w/2, y-d/2, z, w, d, h, shade=shade, alpha=alpha)   


def surface3Dplot(ax, data, *args, shade=True, alpha=0.5, **kwargs):
    assert isinstance(data, np.ndarray)
    assert data.ndim == 2       
    assert isinstance(shade, bool)
    assert isinstance(alpha, float)
    x, y = np.meshgrid(*[np.arange(0, length, 1) for length in data.shape])
    z = data
    ax.plot_surface(x, y, z, shade=shade, alpha=alpha)      
    
    
    

    
    
    
    
