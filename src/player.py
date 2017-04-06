#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Player(object):
    nm = ''
    off = 0
    defn = 0

    
    def __init__(self, name, offense, defense):
        self.nm = name
        self.off = offense
        self.defn = defense

        
    def avgStat(self):
        return (self.off + self.defn)/2

    def getName(self):
        return self.nm