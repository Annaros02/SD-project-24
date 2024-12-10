import pygame
import random

class PineappleRain(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.image = pygame.image.load("obstacles.pineapple.png")  # Make sure you have this image
        self.image = pygame.transform.scale(self.image, (75, 75))  # Adjust the size if necessary
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = random.randint(-100, -50)  # Starts above the screen
        self.window_height = window_height

    def update(self):
        self.rect.y += 5  # The falling speed of pineapples
        if self.rect.top > self.window_height:  # If the pineapple goes off the screen at the bottom
            self.kill()  # Remove the pineapple

