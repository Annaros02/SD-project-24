import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("obstacles.png")  # Load the obstacle image
        self.image = pygame.transform.smoothscale(self.image, (100, 100))  # Resize obstacle
        self.rect = self.image.get_rect()
        self.rect.x = 20  # Initial horizontal position
        self.rect.y = 500  # Vertical position (aligned to the ground)

    def update(self, scroll_speed):
        # Move the obstacle with the scrolling background
        self.rect.x -= scroll_speed
        # Remove the obstacle if it moves off-screen to the left
        if self.rect.right < 0:
            self.kill()

