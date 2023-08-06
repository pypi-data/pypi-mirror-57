#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
load features

@author: livy
"""

import featuretools as ft
from v_ft import custom_primitives
from pkg_resources import resource_stream
#import time_unit
import glob
import pandas as pd
def load_features():
    all_ft = {}
    for name in glob.glob('data/*.json'):
        all_ft[name[5:-5]]=ft.load_features(name)
    #saved_features = ft.load_features('ft_case2case.json')
    return all_ft

#all_ft = load_features()
#print(all_ft.keys())

#ft.load_features()
#resource_stream('v_ft','data/*.json')
