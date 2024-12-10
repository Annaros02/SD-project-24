import pygame

class Player(pygame.sprite.Sprite):  # Class representing the player character
    def __init__(self):
        super().__init__()  # Call the Sprite initializer
        self.health = 100  # Initial player health
        self.max_health = 100  # Maximum player health
        self.velocityX = 5  # Horizontal movement speed
        self.image = pygame.image.load("player.png")  # Load player image
        self.image = pygame.transform.smoothscale(self.image, (160, 175))  # Scale player image
        self.rect = self.image.get_rect()  # Get rectangle for positioning
        self.rect.x = 20  # Initial horizontal position
        self.rect.y = 500  # Initial vertical position (ground level)
        self.velocityY = 0  # Vertical speed for jumping and falling
        self.jumpStrength = -25  # Initial upward force when jumping
        self.gravity = 1  # Gravity force applied to the player
        self.isJumping = False  # Track if the player is currently jumping
        self.heart_image = pygame.image.load("heart.png")
        self.heart_image = pygame.transform.smoothscale(self.heart_image, (50, 50))  # Ajustez la taille selon vos besoins

        

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

    def take_damage(self, damage):
        #Reduces player's health when hit.
        self.health -= damage
        if self.health <= 0:  # If health reaches zero, the game is over
            self.health = 0 
            return True  # Indicate game over
        return False  # Indicate the player is still alive
    

        
    def draw_health_bar(self, surface):
        # Dessine un coeur au-dessus du joueur si la santé est supérieur à 50% 
        if self.health > 50:  # Affiche le cœur uniquement si la santé est supérieure à 50
            heart_x = self.rect.x + self.rect.width // 2 - 15  # Centré horizontalement
            heart_y = self.rect.y - 35  # Positionné au-dessus du joueur
            surface.blit(self.heart_image, (heart_x, heart_y))

        