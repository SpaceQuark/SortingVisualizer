import os
import sys

import pygame
from pygame.locals import *
from Array_GUI import Visualizer
from GUI_Functions import KEY_PRESSED
from SortingAlgos.InsertionSort import InsertionSort
from SortingAlgos.SelectionSort import SelectionSort
from SortingAlgos.BubbleSort import BubbleSort
from SortingAlgos.CocktailShakerSort import CocktailShakerSort
from SortingAlgos.MergeSort import MergeSort
from SortingAlgos.QuickSort import QuickSort
from SortingAlgos.HeapSort import HeapSort
from SortingAlgos.CountingSort import CountingSort
from SortingAlgos.RadixLSDSort import RadixLSD
from SortingAlgos.RadixMSDSort import RadixMSD

from Exceptions import ArraySizeError
from math import log

ARRAY_SIZE = 256 # Max value is 5000.


SCREENSIZE = (1280, 800) 
# FLAGS = FULLSCREEN | DOUBLEBUF # Fullscreen mode.
pygame.init() # Starting PyGame library.
WIN_SIZE = (SCREENSIZE[0], SCREENSIZE[1]) # Screen resolution depending on the screen size.
WIN = pygame.display.set_mode(WIN_SIZE) # Creating screen in fullscreen mode.
WIN.set_alpha(None) # Disabling alpha, since we don't use images so that improves the perfomance.
pygame.display.set_caption("Color Array Visualizer")
pygame.display.set_icon(pygame.image.load("./Icon.png"))
pygame.mouse.set_visible(False) # Hide the mouse.
pygame.event.set_allowed([QUIT, KEYDOWN]) 
FONT = pygame.font.SysFont('Arial', 24) # Using the font to count iterations.
SA = ["Insertion Sort", "Selection Sort", "Bubble Sort", "Cocktail Shaker Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Counting Sort", "Radix LSD Sort", "Radix MSD Sort"]

info_text = [str(f"Array Size: {ARRAY_SIZE}"), str(f"Current Algorithm: None")] 
Vis = Visualizer(ARRAY_SIZE, 5, WIN_SIZE[1], (WIN_SIZE[0] - 20) / ARRAY_SIZE, WIN_SIZE[1] - 30, info_text) # Creating the Vis.

while True:
    KEY = KEY_PRESSED()
    if KEY == "QUIT":
        MAIN_LOOP = False
        
        pygame.quit()
        sys.exit()
        
    if KEY == 0:
        Vis = Visualizer(ARRAY_SIZE, 5, WIN_SIZE[1], (WIN_SIZE[0] - 20) / ARRAY_SIZE, WIN_SIZE[1] - 30, info_text) # Creating the Vis.
        Vis.Draw(WIN, FONT, True)
    if KEY == 1:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        InsertionSort(Vis, WIN, FONT)
    if KEY == 2:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        SelectionSort(Vis, WIN, FONT)
    if KEY == 3:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        BubbleSort(Vis, WIN, FONT)
    if KEY == 4:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        CocktailShakerSort(Vis, WIN, FONT)
    if KEY == 5:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        MergeSort(Vis, WIN, FONT)
    if KEY == 6:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        QuickSort(Vis, WIN, FONT)
    if KEY == 7:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        HeapSort(Vis, WIN, FONT)
    if KEY == 8:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        CountingSort(Vis, WIN, FONT)
    if KEY == 9:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        RadixLSD(Vis, WIN, FONT)
    if KEY == 10:
        Vis.info[1] = str(f"Current Algorithm: {SA[KEY-1]}")
        RadixMSD(Vis, WIN, FONT)
            
        
        
