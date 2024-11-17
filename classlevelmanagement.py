import pygame
import w

class LevelManager:
    def __init__(self):
        self.level = 1  # Initial level

    def update_level(self, score):
        # Update level based on score (1 level every 1000 points)
        self.level = (score // 1000) + 1

    def get_level(self):
        return self.level
