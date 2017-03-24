#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Player(object):
    off = 0
    defn = 0
    ht = 0
    wt = 0
    
    def __init__(self, offense, defense, height, weight):
        self.off = offense
        self.defn = defense
        self.ht = height
        self.wt = weight
        
    def avgStat(self):
        return (self.off + self.defn)/2
