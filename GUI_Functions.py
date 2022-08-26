import pygame
from pygame.locals import *

def KEY_PRESSED():
    for Event in pygame.event.get():
        if Event.type == pygame.KEYDOWN:
            if Event.key == K_LEFT or Event.key == K_a:
                return 'LEFT'
            if Event.key == K_RIGHT or Event.key == K_d:
                return 'RIGHT'
            if Event.key == K_DOWN or Event.key == K_s:
                return 'DOWN'
            if Event.key == K_UP or Event.key == K_w:
                return 'UP'
            if Event.key == K_TAB:
                return 'TAB'
            if Event.key == K_ESCAPE:
                return 'QUIT'
            if Event.key == K_SPACE:
                return 'SPACE'
            if Event.key == K_0:
                return 0
            if Event.key == K_1:
                return 1
            if Event.key == K_2:
                return 2
            if Event.key == K_3:
                return 3
            if Event.key == K_4:
                return 4
            if Event.key == K_5:
                return 5
            if Event.key == K_6:
                return 6
            if Event.key == K_7:
                return 7
            if Event.key == K_8:
                return 8              
            
        if Event.type == pygame.QUIT:
            return 'QUIT'
    return None