import random
import pygame
from Exceptions import ArraySizeError
from GUI_Functions import KEY_PRESSED
from time import sleep as WaitTime
from math import ceil
# import winsound as BeepSound
# from Sound_Generator import ToneGenerator

# Generator = ToneGenerator()
# Sound_Duration = 0.2 # Time (seconds) to play at each step.
# Sound_Frequency_Range = [i for i in range(255, 1000)]
# Amplitude = 3  # Amplitude of the waveform.

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
        :param info: Array storing the current Sorting Algorithm and the array size.

        """
        if size > 10000: # sizes bigger than 1000 take too much time sorting and displaying the array.
            raise ArraySizeError(f"Array size is too big, size can't be bigger than 10000. Selected size is {size}.")
        else:
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.size = size
            self.accesses = 0 # Count how many accesses to the array we have made.
            self.jumps = ceil(RGB_SIZE/size) # Find corresponding RGB colours with more or less steps.
            self.info = info
            self.Moving_Elements = [] # Knowing the values of the current elements that we are moving.
            self.isSorted = False # Using it to know if we have to execute the sorting algorithm.
            
            self.array = [i for i in range(1, size+1)] # Generate array with numbers from 1 to size.
            random.shuffle(self.array) # Moving the numbers to random positions.
            # self.array = random.sample(range(1, size+1), size)


    def Draw(self, Win, Font, extraAcceses=1, cleanScreen=True):
        """
        :param Win: PyGame surface, to draw the array.
        :param Font: Font to write the information.
        :param extraAcceses: Using it to count the array accesses, sometimes we move more than one element so we have to add more than one to the counter.
        """

        Win.fill((0, 0, 0)) # Clearing everything
        if not self.isSorted: # If not sorted, we add the accesses.
            self.accesses += extraAcceses

        try:
            normal_array = [i / max(self.array) for i in self.array]  # Creating an array with values between [0, 1].
        # print(self.array[:20:], max(self.array))
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

            color = RGB[self.array[i]*self.jumps%RGB_SIZE] # Getting the colour value depending on our value, here we don't use the normalized value, since we want to acces to a position of an array and we can't do Array[0.7].
            pygame.draw.rect(Win, color, rectangle) # Drawing on the surface, with the colour, and the generated rectangle.

        self._Draw_Text(Win, Font)
        pygame.display.update() # Updating screen.

    def Draw_Check_Sorted(self, Win, Font):
        self._Draw_Text(Win, Font)
        
        normal_array = [i / max(self.array) for i in self.array]  # Creating an array with values between [0, 1].
        for i in range(self.size):
            curr_elem = normal_array[i] # Getting the value of the element.
            rectangle = pygame.Rect(self.x + i*self.width, self.y, self.width, self.height*curr_elem) # Drawing the rectangle, x position increases at every iteration and height depends on the value of the element.
            rectangle.bottom = self.y
  
            color = (70, 230, 70) # Getting the colour value depending on our value, here we don't use the normalized value, since we want to acces to a position of an array and we can't do Array[0.7].
            pygame.draw.rect(Win, color, rectangle) # Drawing on the surface, with the colour, and the generated rectangle.

            KEY = KEY_PRESSED()
            if KEY == "QUIT":
                pygame.quit()
                exit()
            else:
                pygame.display.update() # Updating screen.

    def _Draw_Text(self, Win, Font):
        Accesses_Text = Font.render(f"Array Accesses: {self.accesses}", True, (255, 255, 255)) # Drawing the text with the accesses to the array.
        Win.blit(Accesses_Text, (10, 10))
        Rendered_1 = Font.render(self.info[0], True, (255, 255, 255)) # Array size.
        Rendered_2 = Font.render(self.info[1], True, (255, 255, 255)) # Current algorithm.
        Win.blit(Rendered_1, (400, 10))
        Win.blit(Rendered_2, (720, 10))
        

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.array)