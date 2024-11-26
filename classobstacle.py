#A MODIFIER APRES LES ENNEMIS SOIENT TERMINE

import pygame 
import random

class FallingObstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, window_width, world_offset_x):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (70, 70))  # Adjust size
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(world_offset_x, world_offset_x + window_width)  # Spawn based on world position
        self.rect.y = -self.rect.height  # Start above the screen
        self.speed = random.randint(3, 6)  # Random falling speed

    def update(self, world_offset_x, scroll_speed):
        
        #Adjust obstacle position based on scrolling

        self.rect.x -= scroll_speed  # Move with the world
        self.rect.y += self.speed  # Move downwards

        # Remove if off-screen
        if self.rect.y > 720 or self.rect.x < -self.rect.width or self.rect.x > WINDOWWIDTH + self.rect.width:
            self.kill()
