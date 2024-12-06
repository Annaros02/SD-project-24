import pygame

class LevelManager:
    def __init__(self):
        self.level = 1  # Initial level

    def update_level(self, score):
        # Update level based on score (1 level every 500 points)
        self.level = (score // 500) + 1

    def get_level(self):
        return self.level
    
    def reset_level(self):
        self.level = 1