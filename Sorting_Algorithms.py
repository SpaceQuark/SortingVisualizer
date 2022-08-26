import pygame
import os, sys
import copy
import random
from pygame.locals import *
from GUI_Functions import KEY_PRESSED
from Exceptions import ArraySizeError

def InsertionSort(Vis, Win, Font, DrawSort=True):
    for arrayPosition in range(1, len(Vis.array)):
        actualElement = Vis.array[arrayPosition]  
        while arrayPosition > 0 and Vis.array[arrayPosition - 1] > actualElement:
            Vis.array[arrayPosition] = Vis.array[arrayPosition - 1]
            arrayPosition -= 1
            Vis.array[arrayPosition] = actualElement
            if DrawSort:
                Vis.Moving_Elements = [Vis.array[arrayPosition]]
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    Vis.Draw(Win, Font)

    if not Vis.isSorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.isSorted = True
    return Vis

def CocktailShakerSort(Vis, Win, Font, DrawSort=True):
    for i in range(len(Vis.array) - 1, 0, -1):
        Swapped = False
        for j in range(i, 0, -1):
            if Vis.array[j] < Vis.array[j - 1]:
                Vis.array[j], Vis.array[j - 1] = Vis.array[j - 1], Vis.array[j]
                Vis.Moving_Elements = [Vis.array[j], Vis.array[j - 1]]
                if DrawSort:
                    KEY = KEY_PRESSED()
                    if KEY == "QUIT":
                        pygame.quit()
                        sys.exit()
                    else:
                        Vis.Draw(Win, Font, extraAcceses=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                    Swapped = True
        for j in range(i):
            if Vis.array[j] > Vis.array[j + 1]:
                Vis.array[j], Vis.array[j + 1] = Vis.array[j + 1], Vis.array[j]
                Vis.Moving_Elements = [Vis.array[j], Vis.array[j + 1]]
                if DrawSort:
                    KEY = KEY_PRESSED()
                    if KEY == "QUIT":
                        pygame.quit()
                        sys.exit()
                    else:
                        Vis.Draw(Win, Font, extraAcceses=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                    Swapped = True
        if not Swapped:
            if not Vis.isSorted:
                Vis.Draw_Check_Sorted(Win, Font)

            Vis.isSorted = True
            return Vis

def BubbleSort(Vis, Win, Font, DrawSort=True):
    Swapped = True
    while Swapped:
        Swapped = False
        for i in range(len(Vis.array) - 1):
            if Vis.array[i] > Vis.array[i + 1]:
                Vis.array[i], Vis.array[i + 1] = Vis.array[i + 1], Vis.array[i]
                Vis.Moving_Elements = [Vis.array[i], Vis.array[i + 1]]
                if DrawSort:
                    KEY = KEY_PRESSED()
                    if KEY == "QUIT":
                        pygame.quit()
                        sys.exit()
                    else:
                        Vis.Draw(Win, Font, extraAcceses=2) # Since we are moving two elements on the array, we have to add 2 acceses instead of one.
                    Swapped = True

    if not Vis.isSorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.isSorted = True
    return Vis

RUN = 32

def Tim_InsertionSort(Vis, Left, Right, Win, Font, DrawSort):
    for i in range(Left + 1, Right + 1):
        Temp = Vis.array[i]
        j = i - 1
        while Vis.array[j] > Temp and j >= Left:
            Vis.array[j + 1] = Vis.array[j]
            Vis.Moving_Elements = [Vis.array[j], Vis.array[j + 1]]
            j -= 1
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                if DrawSort:
                    Vis.Draw(Win, Font)
        Vis.array[j + 1] = Temp
        Vis.Moving_Elements = [Vis.array[j + 1]]
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            if DrawSort:
                Vis.Draw(Win, Font)

def Merge(Vis, l, m, r, Win, Font, DrawSort):
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
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                Vis.Draw(Win, Font)
        else:
            Vis.array[k] = Right[j]
            Vis.Moving_Elements = [Vis.array[k]]
            j += 1
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                if DrawSort:
                    Vis.Draw(Win, Font)
        k += 1
    while i < LEN_1:
        Vis.array[k] = Left[i]
        Vis.Moving_Elements = [Vis.array[k]]
        k += 1
        i += 1
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            if DrawSort:
                Vis.Draw(Win, Font)
    while j < LEN_2:
        Vis.array[k] = Right[j]
        Vis.Moving_Elements = [Vis.array[k]]
        k += 1
        j += 1
        KEY = KEY_PRESSED()
        if KEY == "QUIT":
            pygame.quit()
            sys.exit()
        else:
            if DrawSort:
                Vis.Draw(Win, Font)


def TimSort(Vis, Win, Font, DrawSort=True):
    if not Vis.isSorted:
        N = len(Vis.array)
        for i in range(0, N, RUN):
            Tim_InsertionSort(Vis, i, min((i + 31), (N - 1)), Win, Font, DrawSort)
        Size = RUN
        while Size < N:
            for Left in range(0, N, 2 * Size):
                Mid = Left + Size - 1
                Right = min((Left + 2 * Size - 1), (N - 1))
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    if DrawSort:
                        Vis.Draw(Win, Font)
                Merge(Vis, Left, Mid, Right, Win, Font, DrawSort)
            Size = 2 * Size

    if not Vis.isSorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.isSorted = True
    return Vis


def CycleSort(Vis, Win, Font):
    if not Vis.isSorted:
        Writes = 0
        for cycleStart in range(0, len(Vis) - 1):
            Item = Vis.array[cycleStart]
            Position = cycleStart
            for i in range(cycleStart + 1, len(Vis)):
                if Vis.array[i] < Item:
                    Position += 1
            if Position == cycleStart:
                continue

            while Item == Vis.array[Position]:
                Position += 1
            Vis.array[Position], Item = Item, Vis.array[Position]
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                Vis.Draw(Win, Font, extraAcceses=2)
            Writes += 1

            while Position != cycleStart:
                Position = cycleStart
                for i in range(cycleStart + 1, len(Vis)):
                    if Vis.array[i] < Item:
                        Position += 1
                while Item == Vis.array[Position]:
                    Position += 1
                Vis.array[Position], Item = Item, Vis.array[Position]
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    Vis.Draw(Win, Font, extraAcceses=2)
                Writes += 1

    if not Vis.isSorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.isSorted = True
    return Vis

def rotLeft(Array, n=1):
    return Array[n % len(Array):] + Array[:n % len(Array)]

def Rotate(Vis, rotationTimes, Win, Font):
    if not Vis.isSorted:
        for _ in range(rotationTimes):
            Vis.array = rotLeft(Vis.array)
            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                sys.exit()
            else:
                Vis.Draw(Win, Font)

        Vis.Draw_Check_Sorted(Win, Font)

    Vis.isSorted = True
    return Vis

def ElementsIncreaser(Vis, increaseSize, Win, Font):
    if not Vis.isSorted:
        for _ in range(increaseSize):
            for arrayPosition in range(len(Vis)):
                Vis.array[arrayPosition] += 1
                KEY = KEY_PRESSED()
                if KEY == "QUIT":
                    pygame.quit()
                    sys.exit()
                else:
                    Vis.Draw(Win, Font)

        Vis.Draw_Check_Sorted(Win, Font)

    Vis.isSorted = True
    return Vis