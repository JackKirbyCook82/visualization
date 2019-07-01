# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 2019
@name:   Geography Visualization Objects
@author: Jack Kirby Cook

"""

import json

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['Geography_Plotter']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_aslist = lambda items: [item for item in items] if hasattr(items, '__iter__') and not isinstance(items, str) else [items]


class Geography_Plotter(object):
    def __init__(self, geotable, arraytable): 
        assert all([item in geotable.data.columns for item in ('geography', 'geometry')])
        assert 'geography' in arraytable.data.dims
        self.__queue = {key:_aslist(arraytable.data.coords[key].values) for key in arraytable.data.dims if key != 'geography'}
        self.__geotable, self.__arraytable = geotable, arraytable
    
    def __repr__(self): return '{}()'.format(self.__class__.__name__)   
    def __str__(self): return '\n'.join([self.__class__.__name__, json.dumps(self.asdict(), sort_keys=False, indent=3, separators=(',', ' : '))])  
    def asdict(self): return {key:values for key, values in self.__queue.items()}      
        
    @property
    def geotable(self): return self.__geotable
    @property
    def arraytable(self): return self.__arraytable

    def __getitem__(self, key): return self.__queue[key]
    def __setitem__(self, key, value): 
        assert key in self.__queue.keys()
        assert value in self.__queue[key]
        self.__queue[key] = value 

    def plotmap(self):
        assert all([isinstance(value, str) for value in self.__queue.values()])
        maptable = self.__arraytable[self.asdict()].flatten()
        print(maptable)