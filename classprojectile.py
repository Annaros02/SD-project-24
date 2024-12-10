import pygame
WINDOWWIDTH = 1080

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("ninjastar.png")  # Load projectile image
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize if needed
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-10, -10)  # Slightly shrink the collision rectangle
        self.rect.x = x  # Start at the player's position
        self.rect.y = y
        self.speed = speed  # Horizontal speed of the projectile

    def update(self):
        self.rect.x += self.speed  # Move horizontally
        if self.rect.x > WINDOWWIDTH:  # Remove if off-screen
            self.kill()

