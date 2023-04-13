# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:41:48 2021

@author: miron
"""

import numpy
import matplotlib.pyplot as plt
import random


num_samples = 100000
num_win_stay = 0
num_lose_stay = 0
num_win_change = 0
num_lose_change = 0
num_win_rand = 0
num_lose_rand = 0

for i in range(num_samples):
    print(i)
    
    win_door = random.randint(0, 2)
    choice = random.randint(0, 2)
    
    #stay
    if win_door == choice:
        num_win_stay += 1
    else:
        num_lose_stay += 1
    
    if win_door != choice:
        num_win_change += 1
    else:
        num_lose_change += 1
    
    if random.randint(0,1) == 1:
        
        if win_door != choice:
            num_win_rand += 1
        else:
            num_lose_rand += 1
    else:
        if win_door == choice:
            num_win_rand += 1
        else:
            num_lose_rand += 1

figure, axis = plt.subplots(1, 3)

axis[0].pie([num_win_stay, num_lose_stay], labels=['win', 'lose'])
axis[0].set_title('stay')
axis[1].pie([num_win_change, num_lose_change], labels=['win', 'lose'])
axis[1].set_title('change')
axis[2].pie([num_win_rand, num_lose_rand], labels=['win', 'lose'])
axis[2].set_title('rand')

plt.show()
