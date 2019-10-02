# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 2019
@name:   Visualization Plots
@author: Jack Kirby Cook

"""

import numpy as np
import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['map_plot', 'dist_hbar_plot']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""

_BARCOLORS = 'Y1Gn'
_MAPCOLORS = {'roads':'DarkRed', 'water':'DarkBlue', 'map':'YlGn'}

_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)


# PLOTS
def map_plot(ax, data, *args, geo, base, roads=None, water=None, colors={}, **kwargs):
    colors = {key:colors.get(key, value) for key, value in _MAPCOLORS.items()}
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
    geomap.plot(ax=ax, column=data.name, alpha=0.5, cmap=colors['map'], edgecolor=None)    
    if roads: roads.plot(ax=ax, alpha=1, linewidth=0.3, edgecolor=colors['roads'])
    if water: water.plot(ax=ax, alpha=1, linewidth=0.3, edgecolor=colors['water'])
    ax.set_xlim(xlimit)
    ax.set_ylim(ylimit)

           
#def lineplot(ax, x, y, legend, *args, **kwargs): 
#    assert all([isinstance(item, np.ndarray) for item in (x, y)])
#    ax.plot(x, y, label=legend)


#def scatterplot(ax, x, y, s, legend, *args, **kwargs):
#    assert all([isinstance(item, np.ndarray) for item in (x, y, s)])
#    ax.scatter(x, y, s=s, alpha=0.5, label=legend)
 
    
def scatter_plot(ax, data, legend, *args, color, **kwargs):
    assert isinstance(data, pd.Series)
    axesnames = data.index.names
    dataname = data.name
    assert len(axesnames) == 2 or len(axesnames) == 3
    for axisname in axesnames: data = data.unstack(level=axisname)
    ax.scatter(*[data[axisname].to_numpy() for axisname in axesnames], s=data[dataname].to_numpy(), alpha=0.5, label=legend)
    ax.grid(True)
    
    
def dist_hbar_plot(ax, data, *args, **kwargs):
    assert isinstance(data, pd.DataFrame)
    index, columns = list(data.index.values), list(data.columns)
    data = data.to_numpy()
    cumdata = data.cumsum(axis=1)
    
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())
    
    colors = plt.get_cmap(_BARCOLORS)(np.linspace(0.15, 0.85, data.shape[1])) 
    for index, (category, color) in enumerate(index, colors):
        widths = data[:, index]
        starts = cumdata[:, index] - widths
        ax.barh(columns, widths, left=starts, height=0.5, label=index, color=color)
        
        centers = starts + widths / 2
        for y, (x, c) in enumerate(zip(centers, widths)): ax.text(x, y, str(int(c)), ha='center', va='center')        
    ax.legend(ncol=len(x), box_to_anchor=(0,1), loc='lower left')
        

#def bar3Dplot(ax, data, *args, size=(0.8,0.8), offset=(0,0), **kwargs):
#    assert isinstance(data, np.ndarray)
#    assert data.ndim == 2        
#    assert isinstance(size, tuple)
#    assert len(size) == 2
#    assert isinstance(offset, tuple)
#    assert len(offset) == 2
#    x, y = np.meshgrid(*[np.arange(0, length, 1) for length in data.shape])
#    x, y = x.ravel() + offset[0], y.ravel() + offset[1]
#    z = np.zeros_like(x + y)
#    w, d = size
#    h = data.flatten()
#    ax.bar3d(x-w/2, y-d/2, z, w, d, h, shade=True, alpha=0.5)   


#def surface3Dplot(ax, data, *args, **kwargs):
#    assert isinstance(data, np.ndarray)
#    assert data.ndim == 2       
#    x, y = np.meshgrid(*[np.arange(0, length, 1) for length in data.shape])
#    z = data
#    ax.plot_surface(x, y, z, shade=True, alpha=0.5)      
    
    
    

    