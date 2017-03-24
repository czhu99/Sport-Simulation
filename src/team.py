# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Team(object):
    global playerList
    playerList = []
    
    def __init__(self, players):
        self.playerList = players
    
    def addPlayer(self, newPlayer):
        playerList.append(newPlayer)
    
    def getPlayers(self):
        return playerList