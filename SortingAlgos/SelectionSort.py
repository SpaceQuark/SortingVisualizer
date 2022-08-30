import pygame
import os, sys
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED

def SelectionSort(Vis, Win, Font):
    for i in range(Vis.size):
        mini = i
        for j in range(i+1, Vis.size):
            if Vis.array[j] < Vis.array[mini]:
                mini = j
                
                SORTING_KEY_PRESSED()
                Vis.Draw(Win, Font)
    
        Vis.array[i], Vis.array[mini] = Vis.array[mini], Vis.array[i]
        Vis.Moving_Elements = [Vis.array[i]]

    if not Vis.is_sorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.is_sorted = True
    Vis.Draw(Win, Font)