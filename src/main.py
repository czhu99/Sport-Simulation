#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from team import Team
from player import Player

t1 = Team([Player(70, 40, 190, 180), Player(70, 40, 190, 180), Player(70, 40, 190, 180)])
#t1.addPlayer(Player(70, 40, 190, 180))
pList = t1.getPlayers()

for i in range(0, len(pList)):
    print(pList[i].avgStat())