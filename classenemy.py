import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyimage, width, height, base_speed=6, speed_variation=3):
        
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
        self.rect.x = random.randint(1280, 1480)  # Spawn off-screen to the right
        self.rect.y = 500  # Ground level
        
        # Movement speed
        self.speed = base_speed + random.randint(0, speed_variation)

        # Initial health of the enemy
        self.health = 100 

    def update(self):      
        #Update the enemy's position and remove it if it moves off-screen.      
        self.rect.x -= self.speed  # Move the enemy to the left
        
        # Remove the enemy if it moves off the left side of the screen
        if self.rect.x < -self.rect.width:
            self.kill()


    
    def draw_health_bar(self, surface):
        # Health bar (red by default)
        BAR_WIDTH = 40
        BAR_HEIGHT = 5
        bar_x = self.rect.centerx - BAR_WIDTH // 2
        bar_y = self.rect.y - 10  # Position above the enemy

        health_ratio = self.health / 100  # Percentage of remaining health
        health_bar_width = int(BAR_WIDTH * health_ratio)

        # Draw a red bar (background)
        pygame.draw.rect(surface, (255, 0, 0), (bar_x, bar_y, BAR_WIDTH, BAR_HEIGHT))
        # Draw a green bar (remaining health)
        pygame.draw.rect(surface, (0, 255, 0), (bar_x, bar_y, health_bar_width, BAR_HEIGHT))
