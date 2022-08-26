import os
import sys
import ctypes
import pygame
from pygame.locals import *
from Array_GUI import Visualizer
from GUI_Functions import KEY_PRESSED
from Sorting_Algorithms import InsertionSort, CocktailShakerSort, BubbleSort, TimSort, CycleSort, Rotate, ElementsIncreaser
from Exceptions import ArraySizeError
from time import sleep as WaitTime
from math import log

ARRAY_SIZE = 256 # Max value is 10000.
AL = 7 # 1 for Insertion Sort, 2 for Cocktail Shaker Sort, 3 for Bubble Sort, 4 for Tim Sort, 5 for Cycle Sort, 6 for Rotation and 7 for Elements Increaser.

# user32 = ctypes.windll.user32
SCREENSIZE = (1200, 800) # user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# FLAGS = FULLSCREEN | DOUBLEBUF # Fullscreen mode.
pygame.init() # Starting PyGame library.
WIN_SIZE = (SCREENSIZE[0], SCREENSIZE[1]) # Screen resolution depending on the screen size.
WIN_NAME = "Array Visualizer"
WIN_BG = (0, 0, 0)
WIN_ICON = pygame.image.load("./Icon.png")
WIN = pygame.display.set_mode(WIN_SIZE) # Creating screen in fullscreen mode.
WIN.set_alpha(None) # Disabling alpha, since we don't use images so that improves the perfomance.
pygame.display.set_caption(WIN_NAME)
pygame.display.set_icon(WIN_ICON)
pygame.mouse.set_visible(False) # Hidding the mouse.
pygame.event.set_allowed([QUIT, KEYDOWN]) # Adding the two onlu allowed keys, for better perfomance.
FONT = pygame.font.SysFont('Consolas', 24) # Using the font to count iterations.
MAIN_LOOP = True
ALS = ["Insertion Sort", "Cocktail Shaker Sort", "Bubble Sort", "Tim Sort", "Cycle Sort", "Rotation", "Elements Increaser"]

if AL == 4: # In case of TimSort, checking if the array size is a power of two.
    if not (log(ARRAY_SIZE, 2)).is_integer():
        raise ArraySizeError("When using Tim Sort, array size should be power of two. (64, 128, 256, 512)")
    
info_text = [str(f"Array Size: {ARRAY_SIZE}"), str(f"Current Algorithm: {ALS[AL-1]}")] # Creating the text which contains information like the name of the algorithm and the size of the array.
array = Visualizer(ARRAY_SIZE, 5, WIN_SIZE[1], (WIN_SIZE[0] - 20) / ARRAY_SIZE, WIN_SIZE[1] - 30, info_text) # Creating the array.

while MAIN_LOOP:
    KEY = KEY_PRESSED()
    if KEY == "QUIT":
        MAIN_LOOP = False
        
        pygame.quit()
        sys.exit()
    if KEY == 0:
        array = Visualizer(ARRAY_SIZE, 5, WIN_SIZE[1], (WIN_SIZE[0] - 20) / ARRAY_SIZE, WIN_SIZE[1] - 30, info_text) # Creating the array.
        array.Draw(WIN, FONT, True)
    if KEY == 1:
        InsertionSort(array, WIN, FONT).Draw(WIN, FONT, True)
    if KEY == 2:
        CocktailShakerSort(array, WIN, FONT).Draw(WIN, FONT, True)
    if KEY == 3:
        BubbleSort(array, WIN, FONT).Draw(WIN, FONT, True)
    if KEY == 4:
        TimSort(array, WIN, FONT).Draw(WIN, FONT, True)
    if KEY == 5:
        CycleSort(array, WIN, FONT).Draw(WIN, FONT, True)
    if KEY == 6:
        Rotate(array, len(array), WIN, FONT).Draw(WIN, FONT, True)
    if KEY == 7:
        ElementsIncreaser(array, len(array), WIN, FONT).Draw(WIN, FONT, True)
    # else:
    #     if AL == 1:
    #         InsertionSort(array, WIN, FONT, False).Draw(WIN, FONT, True)
    #     elif AL == 2:
    #         CocktailShakerSort(array, WIN, FONT).Draw(WIN, FONT, True)
    #     elif AL == 3:
    #         BubbleSort(array, WIN, FONT).Draw(WIN, FONT, True)
    #     elif AL == 4:
    #         TimSort(array, WIN, FONT).Draw(WIN, FONT, True)
    #     elif AL == 5:
    #         CycleSort(array, WIN, FONT).Draw(WIN, FONT, True)
    #     elif AL == 6:
    #         Rotate(array, len(array), WIN, FONT).Draw(WIN, FONT, True)
    #     elif AL == 7:
    #         ElementsIncreaser(array, len(array), WIN, FONT).Draw(WIN, FONT, True)
            