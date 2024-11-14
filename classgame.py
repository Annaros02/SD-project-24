import pygame
from classplayer import Player  # Import the Player class

class Game:
    def __init__(self):  # Initialize the Game
        self.player = Player()  # Create a new instance of the player character
        self.pressed = {}  # Dictionary to track pressed keys 