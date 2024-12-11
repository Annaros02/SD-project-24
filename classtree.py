import pygame
import random

class TreeObstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, window_width, ground_level):
        super().__init__()
        # Load the tree trunk image
        self.image = pygame.image.load(image_path).convert_alpha()
        # Resize the tree trunk
        self.image = pygame.transform.smoothscale(self.image, (120, 120))  # Adjusted size
        self.rect = self.image.get_rect()
        # Initial position at the right of the screen
        self.rect.x = window_width
        # Aligned with the ground
        self.rect.y = ground_level - self.rect.height
        # Random speed
        self.speed = random.randint(5, 10)

    def update(self):
        # Move the tree trunk to the left
        self.rect.x -= self.speed
        # If the tree trunk goes off-screen, remove it
        if self.rect.right < 0:
            self.kill()
