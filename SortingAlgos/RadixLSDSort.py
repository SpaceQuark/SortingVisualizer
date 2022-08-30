import pygame
import os, sys
from math import log10, floor
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED

# auxilarity counting sort function
def _counting_sort(Vis, place, Win, Font):
    size = Vis.size
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = Vis.array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = Vis.array[i] // place
        output[count[index % 10] - 1] = Vis.array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        Vis.array[i] = output[i]
        
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font) 
        
        
def RadixLSD(Vis, Win, Font):
    max_elem = Vis.size
    place = 1
    while max_elem // place > 0:
        _counting_sort(Vis, place, Win, Font)
        
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font) 
        
        place *= 10