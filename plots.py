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
__all__ = ['map_plot', 'hbar_plot', 'vbar_plot', 'hist_plot', 'surface_plot']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_DEFAULTCOLOR = 'b'
_DEFAULTCOLORSTYLE = 'GnBu'
_MAPCOLORS = {'roads':'DarkRed', 'water':'DarkBlue', 'map':'YlGn', 'border':'black', 'division':'black'}

_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)
_flatten = lambda nesteditems: [item for items in nesteditems for item in items]


# PLOTS
def surface_plot(ax, dataframe, *args, x, y, z, color=_DEFAULTCOLORSTYLE, **kwargs):
    assert all([i in dataframe.columns for i in (x, y, z)])
    dataframe = dataframe.pivot(index=y, columns=x, values=z)
    x, y, z = np.arange(len(dataframe.columns)), np.arange(len(dataframe.index)), dataframe.to_numpy()
    x, y = np.meshgrid(dataframe.columns, dataframe.index)
    ax.plot_surface(x, y, z, cmap=color)
      
def contour_plot(ax, dataframe, *args, x, y, z, density=50, color=_DEFAULTCOLORSTYLE, **kwargs):
    assert all([i in dataframe.columns for i in (x, y, z)])
    dataframe = dataframe.pivot(index=y, columns=x, values=z)
    x, y, z = np.arange(len(dataframe.columns)), np.arange(len(dataframe.index)), dataframe.to_numpy()
    x, y = np.meshgrid(dataframe.columns, dataframe.index)
    ax.contour3D(x, y, z, density, cmap=color)
  
def line_plot(ax, dataframe, *args, colors=None, **kwargs):
    if not colors: colors = [_DEFAULTCOLOR] * len(dataframe.columns)
    else: assert len(dataframe.columns) == len(colors)
    x = dataframe.index.to_numpy()
    for y, c in zip(dataframe.to_numpy().transpose(), colors): ax.plot(x, y, color=c)

def map_plot(ax, data, *args, geo, basegeo, roads=None, water=None, color=_MAPCOLORS['map'], span, **kwargs):
    assert isinstance(data, pd.Series)  
    assert isinstance(geo, gp.GeoDataFrame)
    assert isinstance(basegeo, gp.GeoDataFrame)
    if roads is not None: assert isinstance(roads, gp.GeoSeries)
    if water is not None: assert isinstance(water, gp.GeoSeries)
    assert all([item.index.name == 'geography' for item in (data, geo)])  
    
    geomap, basemap = geo.merge(data, on='geography'), basegeo   
    geomap = geomap.replace([np.inf, -np.inf], np.nan).dropna(how='any', axis=0)
    ax.set_aspect('equal')
    basemap.plot(ax=ax, color='white', edgecolor=_MAPCOLORS['border'])
    xlimit, ylimit = ax.get_xlim(), ax.get_ylim() 
    geomap.plot(ax=ax, column=data.name, alpha=0.5, cmap=color, vmin=span[0], vmax=span[-1], edgecolor=_MAPCOLORS['division'])    
    if roads is not None: roads.plot(ax=ax, alpha=1, linewidth=0.3, edgecolor=_MAPCOLORS['roads'])
    if water is not None: water.plot(ax=ax, alpha=1, linewidth=0.3, edgecolor=_MAPCOLORS['water'])
    ax.set_xlim(xlimit)
    ax.set_ylim(ylimit)

def hist_plot(ax, data, *args, color=_DEFAULTCOLORSTYLE, weights=None, **kwargs):
    assert isinstance(data, pd.DataFrame)
    labels = [str(values) for values in data.columns.values]
    values = data.values.transpose()
    colors = plt.get_cmap(color)(np.linspace(0.15, 0.85, len(labels)))  
    
    for label, value, valuecolor in zip(labels, values, colors):
        ax.hist(value, histtype="stepfilled", alpha=0.5, weights=weights, density=False, color=valuecolor, label=str(label))
    ax.legend(ncol=len(labels), bbox_to_anchor=(0.5,1), loc='lower center')   

def hbar_plot(ax, data, *args, color=_DEFAULTCOLORSTYLE, **kwargs):
    assert isinstance(data, pd.DataFrame)
    labels = [str(values) for values in data.index.values]
    axes = [str(values) for values in data.columns.values]
    values = data.values
    cumvalues = values.cumsum(axis=0)
    colors = plt.get_cmap(color)(np.linspace(0.15, 0.85, len(labels))) 
    
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data.to_numpy(), axis=0).max())    
         
    for i, (label, labelcolor) in enumerate(zip(labels, colors)):
        widths = values[i]
        positions = cumvalues[i] - widths
        ax.barh(axes, widths, left=positions, height=0.5, label=str(label), color=labelcolor)
    
        centers = positions + widths / 2
        for y, (x, c) in enumerate(zip(centers, widths)): ax.text(x, y, str(int(c)), ha='center', va='center')        
    ax.legend(ncol=len(labels), bbox_to_anchor=(0.5,1), loc='lower center')    

def vbar_plot(ax, data, *args, color=_DEFAULTCOLORSTYLE, **kwargs):
    assert isinstance(data, pd.DataFrame)
    labels = [str(values) for values in data.index.values]
    axes = [str(values) for values in data.columns.values]
    values = data.values  
    colors = plt.get_cmap(color)(np.linspace(0.15, 0.85, len(labels))) 
 
    for i, (label, label_color) in enumerate(zip(labels, colors)):
        width = 0.1 
        positions = np.arange(len(axes)) - (width * len(labels) / 2) + (width * i)
        heights = values[i]
        ax.bar(positions, heights, width=width, label=str(label), color=label_color)
    ax.legend(ncol=len(labels), bbox_to_anchor=(0.5,1), loc='lower center') 





    


    