#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from team import Team
from player import Player

import numpy as np
import pandas as pd

vp = Team("Virtus.Pro", []) #VP
nip = Team("Ninjas in Pyjamas", []) #NiP
sk = Team("SK Gaming",[])
ast = Team("Astralis", [])

playerDF = pd.read_csv('Players.csv')

for i in range(0, len(playerDF)):
    plyr = Player(playerDF["Name"][i], playerDF["Offense"][i], playerDF["Defense"][i])
    teamName = playerDF["Team"][i]
    
    if teamName == "VP":
        vp.addPlayer(plyr)
    if teamName == "NiP":
        nip.addPlayer(plyr)
    if teamName == "SK":
        sk.addPlayer(plyr)
    if teamName == "Astralis":
        ast.addPlayer(plyr)
        
teams = [vp, nip, sk, ast]
for i in range(0, len(teams)):
    pList = teams[i].getPlayers()
    if i > 0:
        print("\n")
    print(teams[i].getName() + ": ")    
    for j in range(0, len(pList)):
        print(pList[j].getName(), pList[j].avgStat())
        


    
