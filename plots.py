# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 2019
@name:   Visualization Plots
@author: Jack Kirby Cook

"""

import numpy as np
import pandas as pd
import geopandas as gp

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['mapplot', 'violinplot', 'barplot', 'lineplot', 'bar3Dplot', 'surface3Dplot']
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


# PLOTS
def mapplot(ax, data, *args, geo, base, roads=None, water=None, **kwargs):
    assert isinstance(geo, gp.GeoDataFrame)
    assert isinstance(base, gp.GeoDataFrame)
    assert isinstance(data, pd.Series)
    assert all([item.index.name == 'geography' for item in (data, geo)])  
    basemap = base
    geomap = geo.merge(data, on='geography')   
    assert not geomap.isnull().values.any()
    ax.set_aspect('equal')
    basemap.plot(ax=ax, color='white', edgecolor='black')
    xlimit, ylimit = ax.get_xlim(), ax.get_ylim() 
    geomap.plot(ax=ax, column=data.name, alpha=0.5, cmap=_MAPCOLOR, edgecolor=None)    
    if roads: roads.plot(ax=ax, alpha=1, linewidth=0.3, edgecolor=_ROADCOLOR)
    if water: water.plot(ax=ax, alpha=1, linewidth=0.3, edgecolor=_WATERCOLOR)
    ax.set_xlim(xlimit)
    ax.set_ylim(ylimit)

           
def violinplot(ax, data, *args, **kwargs):
    assert isinstance(data, list)
    assert all([isinstance(item, np.ndarray) for item in data])
    ax.violinplot(data, showmeans=True, showmedians=False, showextrema=True)


def barplot(ax, data, *args, **kwargs):
    assert isinstance(data, np.ndarray)
    assert data.ndim == 1    
    x = np.arange(0, len(data), 1)
    z = np.zeros_like(data)
    w = 0.8
    h = data    
    ax.bar(x, h, width=w, bottom=z)    
    
    
def lineplot(ax, data, *args, **kwargs):
    assert isinstance(data, list)
    assert all([isinstance(item, np.ndarray) for item in data])
    assert len(data) <= 3
    ax.plot(*data)


def scatterplot(ax, data, *args, **kwargs):
    assert isinstance(data, list)
    assert all([isinstance(item, np.ndarray) for item in data])    
    assert len(data) <= 3
    ax.scatter(*data, marker='•')
    

def bar3Dplot(ax, data, *args, size=(0.8,0.8), offset=(0,0), **kwargs):
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
    ax.bar3d(x-w/2, y-d/2, z, w, d, h, shade=True, alpha=0.5)   


def surface3Dplot(ax, data, *args, **kwargs):
    assert isinstance(data, np.ndarray)
    assert data.ndim == 2       
    assert isinstance(shade, bool)
    assert isinstance(alpha, float)
    x, y = np.meshgrid(*[np.arange(0, length, 1) for length in data.shape])
    z = data
    ax.plot_surface(x, y, z, shade=True, alpha=0.5)      
    
    
    

    