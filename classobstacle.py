import pygame
import random

class PineappleRain(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.image = pygame.image.load("obstacles.pineapple.png")  # Assurez-vous d'avoir cette image
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajustez la taille si nécessaire
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = random.randint(-100, -50)  # Commence au-dessus de l'écran
        self.window_height = window_height

        

    def update(self):
        self.rect.y += 5  # La vitesse de descente des ananas
        if self.rect.top > self.window_height:  # Si l'ananas sort de l'écran par le bas
            self.kill()  # Supprimer l'ananas
