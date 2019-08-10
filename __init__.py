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

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['Bar3DPlot']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_aslist = lambda items: [items] if not isinstance(items, (list, tuple)) else list(items)


class Bar3DPlot(dict):
    def __init__(self, figsize, barsize=(1,1)): 
        self.__wlim, self.__dlim = barsize
        self.__shade = True
        self.__alpha = 0.5
        self.__projection = '3d'
        self.fig = Figure(figsize=figsize)
        FigureCanvas(self.fig)
        self.axes = {}

    def display(self): display(self.fig)

    #def shape(self, key): return (len(self.xticks(key)), len(self.yticks(key)))
    #def xticks(self, key): return self[key].get_xticks()
    #def yticks(self, key): return self[key].get_yticks()        
    
    
    def __call__(self, arraytable):
        self.fig.add_subplot(111, projection=self.__projection)    
    
    
    def __setitem__(self, key, arraytable):
        assert isinstance(shape, tuple)
        super().__setitem__(key, )
        xticks, yticks = [np.arange(0,0,1+len(self.axes), length) for length in shape]
        self.ax.set_xticks(xticks)
        self.ax.set_yticks(yticks)          
            
    def __adddata(self, arraytable)
        pass

    def __addlabels(self, arraytable):
        title = arraytable.name
        xname, yname = arraytable.headerkeys
        zname = '\n'.join(arraytable.datakeys) if arraytable.layers > 1 else arraytable.datakeys[0]      
        
        ax.set_title(title)
        self.axes[arraytable.name].set_xlabel(xname)    
        self.axes[arraytable.name].set_ylabel(yname)
        self.axes[arraytable.name].set_zlabel(zname)
            
    def __call__(self, arraytable, *args, **kwargs):
        offsets = np.arange(0, self.__xlim)
        for index, datakey, dataarray in zip(range(arraytable.dim, arraytable.datakeys, arraytable.dataarrays.values()):
            
            
        #offsets = np.arange(0, len(self.data))
        #nonoffsets = np.zeros_like(offsets)        
        #xoffsets = offsets if self.__xlayer else nonoffsets
        #yoffsets = nonoffsets if self.__xlayer else offsets
        #for index, arraytable in zip(range(len(self.data)), self.data): 
        #    self.__plotdata(arraytable.values(), *args, xoffset=xoffsets[index]*self.__xlim, yoffset=yoffsets[index]*self.__ylim, **kwargs)
   
    def __plotdata(self, ax, data, *args, xoffset=0, yoffset=0, **kwargs):
        assert self.ax is not None
        x, y = np.meshgrid(self.xticks, self.yticks)
        x, y = x.ravel(), y.ravel()
        z = np.zeros_like(x + y)
        w = d = 0.1
        h = data.flatten()
        self.ax.bar3d(x+xoffset, y+yoffset, z, w, d, h, shade=self.__shade, alpha=self.__alpha)   








