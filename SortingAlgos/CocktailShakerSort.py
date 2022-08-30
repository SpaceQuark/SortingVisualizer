import pygame
import os, sys
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED

def CocktailShakerSort(Vis, Win, Font):
    for i in range(Vis.size - 1, 0, -1):
        swapped = False
        for j in range(i, 0, -1):
            if Vis.array[j] < Vis.array[j - 1]:
                Vis.array[j], Vis.array[j - 1] = Vis.array[j - 1], Vis.array[j]
                Vis.Moving_Elements = [Vis.array[j], Vis.array[j - 1]]

                SORTING_KEY_PRESSED()
                Vis.Draw(Win, Font, newAccess=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                swapped = True
        for j in range(i):
            if Vis.array[j] > Vis.array[j + 1]:
                Vis.array[j], Vis.array[j + 1] = Vis.array[j + 1], Vis.array[j]
                Vis.Moving_Elements = [Vis.array[j], Vis.array[j + 1]]

                SORTING_KEY_PRESSED()
                Vis.Draw(Win, Font, newAccess=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                swapped = True
        if not swapped:
            if not Vis.is_sorted:
                Vis.Draw_Check_Sorted(Win, Font)

            Vis.is_sorted = True
            Vis.Draw(Win, Font)