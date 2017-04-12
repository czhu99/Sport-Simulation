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
        avgOff = 0
        for i in range(0, len(self.playerList)):
            avgOff += self.playerList[i].getOff()
        return avgOff/len(self.playerList)
        
    def avgDef(self):
        avgDef = 0
        for i in range(0, len(self.playerList)):
            avgDef += self.playerList[i].getOff()
        return avgDef/len(self.playerList)
        
    def playTeam(self, t2):
        offChance = 0
        defChance = 0
        off1 = self.avgOff()
        def1 = self.avgDef()
        off2 = t2.avgOff()
        def2 = t2.avgDef()
        
        if off1 >= def2:
            if (off1 - def2) > 50:
                offChance = .75
            elif (off1 - def2) < 50 and (off1 - def2) > 25:
                offChance = .6
            elif (off1 - def2) < 25 and (off1 - def2) > 0:
                offChance = .55      
            elif off1 == def2:
                offChance = .5