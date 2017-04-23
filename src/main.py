#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from team import Team
from player import Player

from random import shuffle
import numpy as np
import pandas as pd

#creates 8 Team objects 
vp = Team("Virtus.Pro", []) 
nip = Team("Ninjas in Pyjamas", []) 
sk = Team("SK Gaming",[])
ast = Team("Astralis", [])
faze = Team("FaZe Clan", [])
navi = Team("Natus Vincere", [])
fnc = Team("Fnatic", [])
north = Team("North", [])

playerDF = pd.read_csv('Players.csv')

for i in range(0, len(playerDF)): #loops through entire data set and adds each player to their team to their team based on name
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
    if teamName == "FaZe":
        faze.addPlayer(plyr)
    if teamName == "Na'Vi":
        navi.addPlayer(plyr)
    if teamName == "Fnatic":
        fnc.addPlayer(plyr)
    if teamName == "North":
        north.addPlayer(plyr)
        
teams = [vp, nip, sk, ast, faze, navi, fnc, north]

print("Teams and Average Player Stats: ")
#loops through each Team in teams and each player in each team, printing the player's average stat
for i in range(0, len(teams)):
    pList = teams[i].getPlayers()
    if i > 0:
        print("\n")
    print(teams[i].getName() + ": ")    
    for j in range(0, len(pList)):
        print(pList[j].getName(), pList[j].avgStat())
print("\n")

#runs 10,000 trials of 8 team single-elimination tournament. Final winner has win added to total wins
print("Tournament Wins Out of 10,000 Played: ")     
for j in range(0, 10000):
    bracket = teams
    tempbrack = []
    shuffle(bracket)
    while(len(bracket) > 1):
        for i in range(0, len(bracket)):
            if i%2 == 0:
                tempbrack.append(bracket[i].playTeam(bracket[i+1]))
        bracket = tempbrack
        tempbrack = []
        
    bracket[0].addWin()

for i in range(0, len(teams)):
    print(teams[i].getName(), teams[i].getWins())      

