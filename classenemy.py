import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyimage, width, height):
        
        #Initialize the enemy sprite.
        
        #:param enemyimage: Path to the enemy image file.
        #:param width: Optional width to resize the enemy image.
        #:param height: Optional height to resize the enemy image.
        
        super().__init__()
        
        # Load the image and ensure a fresh instance is used each time
        self.image = pygame.image.load(enemyimage)
        self.image = self.image.convert_alpha()
        
        # Resize the image if width and height are provided
        if width and height:
            self.image = pygame.transform.smoothscale(self.image, (width, height))
        
        # Get the rectangle for positioning
        self.rect = self.image.get_rect()
        
        # Set initial spawn position
        self.rect.x = random.randint(1080, 1280)  # Spawn off-screen to the right
        self.rect.y = 500  # Ground level
        
        # Movement speed
        self.speed = 5

    def update(self):
        
        #Update the enemy's position and remove it if it moves off-screen.
        
        self.rect.x -= self.speed  # Move the enemy to the left
        
        # Remove the enemy if it moves off the left side of the screen
        if self.rect.x < -self.rect.width:
            self.kill()
