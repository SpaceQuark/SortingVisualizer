import pygame
import os, sys
from pygame.locals import *
from GUI_Functions import SORTING_KEY_PRESSED


def Merge(Vis, l, m, r, Win, Font):
    LEN_1, LEN_2 = m - l + 1, r - m
    Left, Right = [], []

    for i in range(0, LEN_1):
        Left.append(Vis.array[l + i])

    for i in range(0, LEN_2):
        Right.append(Vis.array[m + 1 + i])

    i, j, k = 0, 0, l
    while i < LEN_1 and j < LEN_2:
        if Left[i] <= Right[j]:
            Vis.array[k] = Left[i]
            Vis.Moving_Elements = [Vis.array[k]]
            i += 1
            
            SORTING_KEY_PRESSED()
            Vis.Draw(Win, Font)
        else:
            Vis.array[k] = Right[j]
            Vis.Moving_Elements = [Vis.array[k]]
            j += 1
            
            SORTING_KEY_PRESSED()
            Vis.Draw(Win, Font)
            
        k += 1
    while i < LEN_1:
        Vis.array[k] = Left[i]
        Vis.Moving_Elements = [Vis.array[k]]
        k += 1
        i += 1
        
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font)
    while j < LEN_2:
        Vis.array[k] = Right[j]
        Vis.Moving_Elements = [Vis.array[k]]
        k += 1
        j += 1
        
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font)

def MergeSort(Vis, Win, Font):
    
    def _merge_sort(Vis, Win, Font, L, R):
        if L >= R:
            return
        
        M = (L+R) // 2
        _merge_sort(Vis, Win, Font, L, M)
        _merge_sort(Vis, Win, Font, M+1, R)
      
        Merge(Vis, L, M, R, Win, Font)

    
    _merge_sort(Vis, Win, Font, 0, Vis.size-1)
    if not Vis.is_sorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.is_sorted = True
    Vis.Draw(Win, Font)