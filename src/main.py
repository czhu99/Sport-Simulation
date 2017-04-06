#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from team import Team
from player import Player


import numpy as np
import pandas as pd

t1 = Team([]) #VP
t2 = Team([]) #NiP
playerDF = pd.read_csv('Players.csv')

for i in range(0, len(playerDF)):
    if playerDF["Team"][i] == "VP":
        t1.addPlayer(Player(playerDF["Name"][i], playerDF["Offense"][i], playerDF["Defense"][i]))
    elif playerDF["Team"][i] == "NiP":
        t2.addPlayer(Player(playerDF["Name"][i], playerDF["Offense"][i], playerDF["Defense"][i]))
        
pList = t1.getPlayers()

for i in range(0, len(pList)):
    print(pList[i].getName(), pList[i].avgStat())
    
