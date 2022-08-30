import pygame
import os, sys
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED

def Heapify(Vis, n, i, Win, Font):
    root = i # initialize root as i
    l = 2 * i + 1
    r = 2 * i + 2
    
    # check if left child of root exists and is greater than root
    if l < n and Vis.array[root] < Vis.array[l]:
        root = l
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font)
    
    # check if right child of root exists and is greater than root
    if r < n and Vis.array[root] < Vis.array[r]:
        root = r
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font)  
          
    # Change root if needed
    if root != i:
        Vis.array[root], Vis.array[i] = Vis.array[i], Vis.array[root]
        
        Vis.Moving_Elements = [Vis.array[i], Vis.array[root]]
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font, newAccess=2)
        
        Heapify(Vis, n, root, Win, Font)
        
def HeapSort(Vis, Win, Font):
    # Building a max heap
    for i in range(Vis.size // 2 - 1, -1, -1):
        Heapify(Vis, Vis.size, i, Win, Font)
    
    # extract elements and heapify
    for i in range(Vis.size - 1, 0, -1):
        Vis.array[i], Vis.array[0] = Vis.array[0], Vis.array[i]
        
        Vis.Moving_Elements = [Vis.array[i], Vis.array[0]]
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font, newAccess=2)
        
        
        Heapify(Vis, i, 0, Win, Font)
    
    if not Vis.is_sorted:
        Vis.Draw_Check_Sorted(Win, Font)
    
    Vis.is_sorted = True
    Vis.Draw(Win, Font)