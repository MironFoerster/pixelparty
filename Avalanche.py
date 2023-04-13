# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 08:00:09 2021

@author: miron
"""

class Avalanche():
    def __init__(self, players, n_holes):
        self.players = players # [Max, Anna, Dean]
        self.n_players = len(players)
        self.n_holes = n_holes # 8?
        self.obstacles = [[o, o, o, o],
                          [o, o, o]]
        self.balls =
        
    def animate(self):
        
        
    def runBall(self, hole):
        pass
        return hole...
    
    def gameLoop(self):
        pass

class Obstacle():
    def __init__(self, inputs=(l, r), outputs=(l, r), init_state=0):
        self.inputs = inputs # l, r - input obstacles
        self.outputs = outputs # l, r - output obstacles
        self.state = init_state # 0 left, 1 right
        self.filled = None # Ball-object wich is filling
        
    def ProcessBall(self, ball):
        if self.filled != None:
            
        return ball
            
class Ball():
    def __init__(self, color, hole):
        self.color = color
        self.stuck = False
        self.input_to = (None, None) # (obstacle, input_side)
        
        
    def 

# main loop

