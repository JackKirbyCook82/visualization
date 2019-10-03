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
__all__ = ['map_plot']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_DEFAULTCOLOR = 'Y1Gn'
_MAPCOLORS = {'roads':'DarkRed', 'water':'DarkBlue', 'map':'YlGn'}

_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)


# PLOTS
def map_plot(ax, data, *args, geo, base, roads=None, water=None, colors={}, **kwargs):
    assert isinstance(data, pd.Series)  
    assert isinstance(geo, gp.GeoDataFrame)
    assert isinstance(base, gp.GeoDataFrame)
    if roads: assert isinstance(roads, gp.GeoDataFrame)
    if water: assert isinstance(water, gp.GeoDataFrame)
    assert all([item.index.name == 'geography' for item in (data, geo)])  
    colors = {key:colors.get(key, value) for key, value in _MAPCOLORS.items()}
    
    geomap, basemap = geo.merge(data, on='geography'), base   
    assert not geomap.isnull().values.any()
    ax.set_aspect('equal')
    basemap.plot(ax=ax, color='white', edgecolor='black')
    xlimit, ylimit = ax.get_xlim(), ax.get_ylim() 
    geomap.plot(ax=ax, column=data.name, alpha=0.5, cmap=colors['map'], edgecolor=None)    
    if roads: roads.plot(ax=ax, alpha=1, linewidth=0.3, edgecolor=colors['roads'])
    if water: water.plot(ax=ax, alpha=1, linewidth=0.3, edgecolor=colors['water'])
    ax.set_xlim(xlimit)
    ax.set_ylim(ylimit)
 
 
#def scatter_plot(ax, data, *args, color=_DEFAULTCOLOR, **kwargs):
#    assert isinstance(data, pd.Dataframe)
#    indexnames = list(data.index.names)
#    columns = list(data.columns.values)
#
#    assert len(indexnames) == 2 or len(indexnames) == 3    
#    colors = plt.get_cmap(color)(np.linspace(0.15, 0.85, len(columns))) 
#    
#    for column, colcolor in zip(columns, colors):
#        coldata = data[column]
#        for indexname in indexnames: coldata = coldata.unstack(level=indexname)
#        ax.scatter(*[coldata[indexname].to_numpy() for indexname in indexnames], s=coldata.to_numpy(), alpha=0.5, color=colcolor, label=column)     
#    ax.grid(True)


#def hist_plot(ax, data, *args, color=_DEFAULTCOLOR, **kwargs):
#    assert isinstance(data, pd.Dataframe)
#    indexnames = list(data.index.names)
#    columns = list(data.columns.values)
#
#    data = data.to_numpy()    
#    colors = plt.get_cmap(color)(np.linspace(0.15, 0.85, len(index))) 
#    
#    for i, (label, label_color) in enumerate(columns, colors):
#        weights = data[i, :]
#        ax.hist(index, weights=weights, label=label, color=label_color)


#def dist_vbar_plot(ax, data, *args, color=_DEFAULTCOLOR, **kwargs):
#    assert isinstance(data, pd.Series)
#    assert len(data.index.names) == 2
#    data = data.unstack()
#    index, columns = list(data.index.values), list(data.columns.values)
#    data = data.to_numpy()
#    colors = plt.get_cmap(color)(np.linspace(0.15, 0.85, len(index))) 
#
#    space = 0.2
#    width = (1 - space) / (len(index) * len(columns)) 
#    for i, (label, label_color) in enumerate(columns, colors):
#        hieght = data[i, :]
#        positions = np.arange(len(index)) - (width / len(columns))
#        ax.bar(positions, hieght, width, label=label, color=label_color)
    

#def dist_hbar_plot(ax, data, *args, color=_DEFAULTCOLOR, **kwargs):
#    assert isinstance(data, pd.Series)
#    assert len(data.index.names) == 2
#    data = data.unstack()
#    index, columns = list(data.index.values), list(data.columns.values)
#    data = data.to_numpy()
#    cumdata = data.cumsum(axis=1)
#    colors = plt.get_cmap(color)(np.linspace(0.15, 0.85, len(index))) 
#    
#    ax.invert_yaxis()
#    ax.xaxis.set_visible(False)
#    ax.set_xlim(0, np.sum(data.to_numpy(), axis=1).max())
#       
#    for i, (label, label_color) in enumerate(columns, colors):
#        widths = data[i, :]
#        starts = cumdata[i, :] - widths
#        ax.barh(index, widths, left=starts, height=0.5, label=label, color=label_color)
#        
#        centers = starts + widths / 2
#        for y, (x, c) in enumerate(zip(centers, widths)): ax.text(x, y, str(int(c)), ha='center', va='center')        
#    ax.legend(ncol=len(x), box_to_anchor=(0,1), loc='lower left')       


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
    
    
    

    