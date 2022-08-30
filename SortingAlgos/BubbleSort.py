import pygame
import os, sys
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED

def BubbleSort(Vis, Win, Font):

    for i in range(Vis.size):
        swapped = False
        for j in range(0, Vis.size - i - 1):
            if Vis.array[j] > Vis.array[j+1]:
                Vis.array[j], Vis.array[j+1] = Vis.array[j + 1], Vis.array[j]
                Vis.Moving_Elements = [Vis.array[j], Vis.array[j + 1]]
                
                swapped = True
                SORTING_KEY_PRESSED()
                Vis.Draw(Win, Font, newAccess=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                
        if swapped == False:
            break

    if not Vis.is_sorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.is_sorted = True
    Vis.Draw(Win, Font)
