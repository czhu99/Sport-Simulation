# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import random
class Team(object):
    
    playerList = []
    nm = ''
    wins = 0
    
    def __init__(self, name, players):
        self.playerList = players
        self.nm = name
        
    def addPlayer(self, newPlayer):
        self.playerList.append(newPlayer)
    
    def getPlayers(self):
        return self.playerList
    
    def getName(self):
        return self.nm
        
    def addWin(self):
        self.wins += 1
    
    def getWins(self):
        return self.wins
        
    def avgOff(self):
        avgOff = 0
        for i in range(0, len(self.playerList)):
            avgOff += self.playerList[i].getOff()
        return avgOff/len(self.playerList)
        
    def avgDef(self):
        avgDef = 0
        for i in range(0, len(self.playerList)):
            avgDef += self.playerList[i].getDef()
        return avgDef/len(self.playerList)
        
    def playTeam(self, t2):
        offChance = 0
        defChance = 0
        winChance = 0
        off1 = self.avgOff()
        def1 = self.avgDef()
        off2 = t2.avgOff()
        def2 = t2.avgDef()
    
        diff1 = abs(off1 - def2)
        if diff1 > 50:
            offChance = .95
        elif diff1 < 50 and diff1 > 25:
            offChance = .8
        elif diff1 < 25 and diff1 > 15:
            offChance = .7      
        elif diff1 < 15 and diff1 > 0:
            offChance = .6
        elif diff1 == 0:
            offChance = .5
        if (off1 - def2) < 0:
            offChance = -1 * offChance
         
        diff2 = abs(def1 - off2)
        if diff2 > 50:
            defChance = .95
        elif diff2 < 50 and diff2 > 25:
            defChance = .8
        elif diff2 < 25 and diff2 > 15:
            defChance = .7
        elif diff2 < 15 and diff2 > 0:
            defChance = .6
        elif diff2 == 0:
            defChance = .5
        if (def1 - off2) < 0:
            defChance = -1 * defChance
        
        winChance = (offChance + defChance)/2.0
        if winChance < 0:
            winChance += 1.0
        
        
        num = random.randint(0, 100)
        if num/100 <= winChance:
            return self
        else:
            return t2
        
        return self
        