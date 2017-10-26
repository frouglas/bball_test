'''
Created on Oct 20, 2017

Module to read in new gameLog data.

@author: doug
'''

import numpy as np
import pandas as pd
import math
import os
import pickle
from data_structure import *


def initialLoad(datafile):
    if os.path.exists(datafile):
        rawData = pd.read_csv(datafile)
    else:
        return NameError
    
    players = {}
    teams = {}
    games = {}
    
    for entry in range(0,rawData.size):
        thisEntry = rawData.iloc[entry]
        playerName = thisEntry["PLAYER FULL NAME"]
        if players.has_key(playerName):
            exists = 1
    return 1
    
initialLoad("gameLogs.csv")
