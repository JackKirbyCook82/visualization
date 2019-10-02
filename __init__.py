# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 2019
@name:   Visualization Package Options
@author: Jack Kirby Cook

"""

import json
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d

import visualization.figures as figures
import visualization.plots as plots

__version__ = "1.0.0"
__author__ = "Jack Kirby Cook"
__all__ = ['set_options', 'get_option', 'show_options', 'figures', 'plots']
__copyright__ = "Copyright 2018, Jack Kirby Cook"
__license__ = ""


_OPTIONS = {'axisfontsize':8, 'legendfontsize':8, 'titlefontsize':12}
_MPLMAPPING = {"axisfontsize":"font.size", "legendfontsize":"legend.fontsize", "titlefontsize":"figure.titlesize"}


def apply_options():
    for key, value in _MPLMAPPING.items(): mpl.rcParams[value] = _OPTIONS[key] 


def set_options(**kwargs):
    global _OPTIONS
    _OPTIONS.update(kwargs)
    apply_options()

    
def get_option(key): return _OPTIONS[key]
def show_options(): 
    optionstrings = json.dumps({key:str(value) for key, value in _OPTIONS.items()}, sort_keys=True, indent=3, separators=(',', ' : '))
    print('Visualization Options {}\n'.format(optionstrings))
    
    
