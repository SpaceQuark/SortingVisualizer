import random
import pygame
from Exceptions import ArraySizeError
from GUI_Functions import KEY_PRESSED
from time import sleep as WaitTime
from math import ceil


RED_PINK = [[255, 0, i] for i in range(256)]
PINK_BLUE = [[i, 0, 255] for i in reversed(range(256))]
BLUE_AQUA = [[0, i, 255] for i in range(256)]
AQUA_GREEN = [[0, 255, i] for i in reversed(range(256))]
GREEN_YELLOW = [[i, 255, 0] for i in range(256)]
YELLOW_RED = [[255, i, 0] for i in reversed(range(256))]
RGB = RED_PINK + PINK_BLUE + BLUE_AQUA + AQUA_GREEN + GREEN_YELLOW + YELLOW_RED
RGB_SIZE = len(RGB)

class Visualizer:
    def __init__(self, size, x, y, width, height, info):
        """

        :param size: Number of elements on the array.
        :param x: Initial x position for the first element on the array.
        :param y: Initial y position for the first element on the array.
        :param width: Width of the biggest element on the array.
        :param height: Height of the biggest element on the array.
        :param info: list storing the current Sorting Algorithm and the array size.

        """
        if size > 10000: 
            raise ArraySizeError(f"Array size is too big, size can't be bigger than 10000. Selected size is {size}.")
        else:
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.size = size
            self.accesses = 0 
            self.jumps = ceil(RGB_SIZE/size) 
            self.info = info
            self.Moving_Elements = [] 
            self.is_sorted = False 
            
            self.array = [i for i in range(1, size+1)] # Generate array with numbers from 1 to size.
            random.shuffle(self.array) # Moving the numbers to random positions.
            # self.array = random.sample(range(1, size+1), size)


    def Draw(self, Win, Font, newAccess=1, cleanScreen=True):
        """
        :param Win: PyGame surface, to draw the array.
        :param Font: Font to write the information.
        :param newAccess: count new accesses
        """

        Win.fill((0, 0, 0)) # Clearing everything
        if not self.is_sorted: # If not sorted, we add the accesses.
            self.accesses += newAccess

        try:
            normal_array = [i / max(self.array) for i in self.array]  # Creating an array with values between [0, 1].
        except ZeroDivisionError:
            normal_array = []
            for i in self.array:
                if i == 0:
                    normal_array.append(i)
                else:
                    normal_array.append(i / max(self.array))

        for i in range(self.size):
            curr_elem = normal_array[i] # Getting the value of the element.
            rectangle = pygame.Rect(self.x + i*self.width, self.y, self.width, self.height*curr_elem)
            rectangle.bottom = self.y

            color = RGB[self.array[i]*self.jumps%RGB_SIZE] # Getting the color value depending on our value
            pygame.draw.rect(Win, color, rectangle) 

        self._Draw_Text(Win, Font)
        pygame.display.update() # Updating screen.

    def Draw_Check_Sorted(self, Win, Font):
        self._Draw_Text(Win, Font)
        
        normal_array = [i / max(self.array) for i in self.array]  # Creating an array with values between [0, 1].
        for i in range(self.size):
            curr_elem = normal_array[i] # Getting the value of the element.
            rectangle = pygame.Rect(self.x + i*self.width, self.y, self.width, self.height*curr_elem) 
            rectangle.bottom = self.y
  
            color = (70, 230, 70) # Using green color to illustrate sorted
            pygame.draw.rect(Win, color, rectangle) 

            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                exit()
            else:
                pygame.display.update() # Update screen.

    def _Draw_Text(self, Win, Font):
        arr_size = Font.render(self.info[0], True, (255, 255, 255)) # Array size.
        curr_algo = Font.render(self.info[1], True, (255, 255, 255)) # Current algorithm.
        Win.blit(curr_algo, (10, 10))
        Win.blit(arr_size, (10, 50))
        
        Accesses_Text = Font.render(f"Array Accesses: {self.accesses}", True, (255, 255, 255)) 
        Win.blit(Accesses_Text, (10, 100))
        

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.array)