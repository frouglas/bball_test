'''
Created on Oct 20, 2017

Module to read in new gameLog data.

@author: doug
'''

import pandas as pd
import math
import os
import pickle
from db_funcs import *


if os.path.exists("stats.db"):
    activeDB = pickle.load("stats.db")
else:
    activeDB = 0
    
print("nothing")
