import pygame
import random

class TreeObstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, window_width, ground_level):
        super().__init__()
        # Charge l'image du tronc
        self.image = pygame.image.load(image_path).convert_alpha()
        # Redimensionne le tronc
        self.image = pygame.transform.smoothscale(self.image, (150, 150))  # Taille ajustée
        self.rect = self.image.get_rect()
        # Position initiale à droite de l'écran
        self.rect.x = window_width
        # Aligné au sol
        self.rect.y = ground_level - self.rect.height
        # Vitesse aléatoire
        self.speed = random.randint(5, 10)

    def update(self):
        # Déplace le tronc vers la gauche
        self.rect.x -= self.speed
        # Si le tronc sort de l'écran, supprime-le
        if self.rect.right < 0:
            self.kill()
