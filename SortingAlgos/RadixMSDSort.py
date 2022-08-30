import pygame
import os, sys
from math import log10, floor
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED

# find the digit at index d in a integer
def digit_at(x, d):
    return (int) (x / pow(10, d-1)) % 10

# function to find largest integer
# Not needed at the moment since largest integer is known
def getMax(Vis):
    mx = max(Vis.array)

def MSD(Vis, l, r, d, Win, Font):
    if r <= l:
        return
    
    count = [0]*12
    tp = {}
    
    for i in range(l, r+1):
        c = digit_at(Vis.array[i], d)
        count[c+2] += 1
        
    for r in range(0,10+1):
        count[r+1] += count[r]
        
    for i in range(l, r+1):
        c = digit_at(Vis.array[i], d)
        tp[count[c+2]] = Vis.array[i]
        count[c+2] += 1
        
    for i in range(l, r+1):
        Vis.array[i] = tp[i-l]
        
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font) 
        
    for r in range(0, 10):
        MSD(Vis, l + count[r], l + count[r+1] -1, d-1)
        
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font) 


def RadixMSD(Vis, Win, Font):
    m = Vis.size
    d = floor(log10(abs(m))) + 1
    
    MSD(Vis, 0, Vis.size-1, d, Win, Font)