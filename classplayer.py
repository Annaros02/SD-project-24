import pygame

class Player(pygame.sprite.Sprite):  # Class representing the player character
    def __init__(self):
        super().__init__()  # Call the Sprite initializer
        self.health = 10  # Example player health
        self.max_health = 100  # Maximum player health
        self.velocityX = 5  # Horizontal movement speed
        self.image = pygame.image.load("player.png")  # Load player image
        self.image = pygame.transform.smoothscale(self.image, (160, 175))  # Scale player image
        self.rect = self.image.get_rect()  # Get rectangle for positioning
        self.rect.x = 20  # Initial horizontal position
        self.rect.y = 500  # Initial vertical position (ground level)
        self.velocityY = 0  # Vertical speed for jumping and falling
        self.jumpStrength = 0  # Initial upward force when jumping
        self.gravity = 1  # Gravity force applied to the player
        self.isJumping = False  # Track if the player is currently jumping
        

    def move_right(self):
        #Always allow horizontal movement 
        self.rect.x += self.velocityX

    def move_left(self):
        if self.rect.x > 0:  # Empêche de dépasser la bordure gauche
            self.rect.x -= self.velocityX


    def jump(self):
        if not self.isJumping:  # Only jump if the player is not already jumping
            self.velocityY = self.jumpStrength  # Apply upward jump force
            self.isJumping = True  # Set jumping state to true
            
    def apply_gravity(self):
        self.rect.y += self.velocityY  # Apply vertical speed to the player's position
        self.velocityY += self.gravity  # Increase vertical speed due to gravity


        # Check if the player has reached the ground
        if self.rect.y >= 500:  # Ground level position
            self.rect.y = 500  # Ensure the player stays on the ground
            self.isJumping = False  # Reset jumping state
            self.velocityY = 0  # Reset vertical speed
            
    