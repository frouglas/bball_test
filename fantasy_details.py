'''
Created on Oct 22, 2017

@author: frouglas
'''

import os
import pandas as pd

def parsePoints(filename):
    if os.path.exists(filename):
        ptDB = pd.read_csv(filename)
        return ptDB
    else:
        return -1
    
