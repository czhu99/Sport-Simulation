#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Player(object): #basic Class for a Player object - has name, offense, and defense value
    nm = ''
    off = 0
    defn = 0
   
    def __init__(self, name, offense, defense): #constructor
        self.nm = name
        self.off = offense
        self.defn = defense
      
    def avgStat(self):
        return (self.off + self.defn)/2

    def getName(self):
        return self.nm
    
    def getOff(self):
        return self.off

    def getDef(self):
        return self.defn