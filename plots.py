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


_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)


# PLOTS
def mapplot(ax, data, *args, geo, base, alpha=0.5, border=False, **kwargs):
    assert isinstance(geo, gp.GeoDataFrame)
    assert isinstance(base, gp.GeoDataFrame)
    assert isinstance(data, pd.Series)
    assert all([item.index.name == 'geography' for item in (data, geo)])  
    basemap = base
    geomap = geo.merge(data, on='geography')   
    assert not geomap.isnull().values.any()
    ax.set_aspect('equal')
    basemap.plot(ax=ax, color='white', edgecolor='black')
    geomap.plot(ax=ax, column=data.name, alpha=alpha, edgecolor='black' if border else None)
    
           
def violinplot(ax, data, *args, showmeans=True, showmedians=False, showextrema=True, **kwargs):
    assert isinstance(data, list)
    assert all([isinstance(item, np.ndarray) for item in data])
    assert all([isinstance(item, bool) for item in (showmeans, showmedians, showextrema)])
    ax.violinplot(data, showmeans=showmeans, showmedians=showmedians, showextrema=showextrema)


def barplot(ax, data, *args, size=0.8, **kwargs):
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
    

def bar3Dplot(ax, data, *args, size=(0.8,0.8), offset=(0,0), shade=True, alpha=0.5, **kwargs):
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
    
    
    

    