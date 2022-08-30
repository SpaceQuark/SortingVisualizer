import pygame
import os, sys
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED

def CountingSort(Vis, Win, Font):
    out = [0] * Vis.size
    
    # count array (serving as a size+1 numbers)
    count = [0] * (Vis.size+1)

    
    for i in range(0, Vis.size):
        count[Vis.array[i]] += 1
    
    # store cumulative count
    for i in range(1, Vis.size+1):
        count[i] += count[i-1]
      
    # Find the index of each number of the original array in count array
    # place the elements in out array  
    i = Vis.size - 1
    while i >= 0:
        out[count[Vis.array[i]]-1] = Vis.array[i]
        count[Vis.array[i]] -= 1
        
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font) 
        
        i -= 1
    
    # Copy the sorted elements into original array
    for i in range(0, Vis.size):     
        Vis.array[i] = out[i]
        
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font)    
    
    
    if not Vis.is_sorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.is_sorted = True
    Vis.Draw(Win, Font)