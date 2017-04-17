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
    
        diff1 = abs(off1 - def2)
        if diff1 > 50:
            offChance = .75
        elif diff1 < 50 and diff1 > 25:
            offChance = .6
        elif diff1 < 25 and diff1 > 0:
            offChance = .55      
        elif diff1 == 0:
            offChance = .5
        if (off1 - def2) < 0:
            offChance = -1 * offChance
         
        diff2 = abs(def1 - off2)
        if diff2 > 50:
            defChance = .75
        elif diff2 < 50 and diff1 > 25:
            defChance = .6
        elif diff2 < 25 and diff1 > 0:
            defChance = .55      
        elif diff2 == 0:
            defChance = .5
        if (off1 - def2) < 0:
            defChance = -1 * defChance
        
        return (offChance + defChance)/2
                
        
        