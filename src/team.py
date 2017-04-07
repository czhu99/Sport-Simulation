# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Team(object):
    
    playerList = []
    nm = ''
    
    def __init__(self, name, players):
        self.playerList = players
        self.nm = name
        
    def addPlayer(self, newPlayer):
        self.playerList.append(newPlayer)
    
    def getPlayers(self):
        return self.playerList
    
    def getName(self):
        return self.nm
    
    def avgOff(self):
        for i in range(0, len(self.playerList)):
            avgOff += self.playerList[i].getOff
        