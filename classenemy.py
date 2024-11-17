import pygame
import random

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Example enemy size
        self.image.fill((255, 0, 0))  # Red color for the enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1080, 1280)  # Spawn off-screen to the right
        self.rect.y = 500  # Ground level
        self.speed = 5  # Speed of the enemy

    def update(self):
        self.rect.x -= self.speed  # Move enemy to the left
        if self.rect.x < -50:  # Remove enemy if it moves off-screen
            self.kill()
