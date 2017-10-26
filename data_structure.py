'''
Created on Oct 20, 2017

Contains the data structures used in organizing the 

@author: doug
'''

import os

class tenure():
    def __init__(self):
        self.team = -1
        self.startDate = -1
        self.endDate = -1
    

class player():
    def __init__(self):
        self.gamestats = []
        self.gamesPlayed = 0
        self.gamesEligible = 0
        self.name = ""
        self.activeTeam = 0
        self.player_career = []
        self.positions = ()
        self.PlayerID = 0
        
class team():
    def __init__(self):
        self.teamName = ""
        self.activePlayers = []
        self.historicalPlayers = []

class game():
    def __init__(self):
        self.gamePlayers = []
        