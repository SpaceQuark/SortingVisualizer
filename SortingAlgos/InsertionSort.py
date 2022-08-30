import pygame
import os, sys
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED

def InsertionSort(Vis, Win, Font):
    for i in range(1, Vis.size):
        e = Vis.array[i]  
        j = i-1
        while j >= 0 and Vis.array[j] > e:
            
            #swap to show movement
            Vis.array[j+1],Vis.array[j] = Vis.array[j], Vis.array[j+1]
            
            j -= 1
        
            Vis.Moving_Elements = [Vis.array[i]]
            
            SORTING_KEY_PRESSED()
            Vis.Draw(Win, Font)
    
        # Vis.array[j+1] = e

    if not Vis.is_sorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.is_sorted = True
    Vis.Draw(Win, Font)