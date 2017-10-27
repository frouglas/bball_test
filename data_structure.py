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
    def __init__(self, params):
        self.gameStats = params.get('gameStats')
        self.gamesPlayed = params.get('gamesPlayed')
        self.gamesEligible = params.get('gamesEligible')
        self.name = params.get('name')
        self.activeTeam = params.get('activeTeam')
        self.playerCareer = params.get('playerCareer')
        self.positions = params.get('positions')
        self.playerID = params.get('playerID')
        
class team():
    def __init__(self):
        self.teamName = ""
        self.activePlayers = []
        self.historicalPlayers = []

class game():
    def __init__(self):
        self.gamePlayers = []
        