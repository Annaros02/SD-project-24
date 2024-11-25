import pygame, random, sys
from classgame import Game  # Import the Game class from the classgame file
from pygame.locals import *  # Import Pygame constants and functions
from classlevelmanagement import LevelManager # Import the LevelManager class from the classlevelmanagement file
from classprojectile import Projectile # Import the Projectile class from the classprojectile file
from classenemy import Enemy # Import the Enemy class from the classenemy file


BACKGROUNDCOLOR = (0, 0, 0)  # Background color for the screen (black)
WINDOWWIDTH = 1080  # Width of the game window
WINDOWHEIGHT = 720  # Height of the game window
GREEN = (0, 100, 0)  # Green color 
WHITE = (255, 255, 255)  # White color 
BLACK = (0,0,0)# Black color 
ORANGE = (255, 128, 0)# Orange color 

# Constants for colors and window dimensions
# Function to draw text with a background for better visibility
def drawTextWithBackground(text, font, surface, x, y, text_color, bg_color):
    textobj = font.render(text, True, text_color)  # Render the text with the specified color
    textrect = textobj.get_rect(center=(x, y))  # Center the text rectangle at (x, y)
    pygame.draw.rect(surface, bg_color, textrect.inflate(20, 10))  # Draw a background rectangle with padding
    surface.blit(textobj, textrect)  # Draw the text on the specified surface

# Function to display a level-up message and pause the game
def display_level_message(level):
    # Clear the screen and display the background
    windowSurface.blit(background, (0, 0))
    
    if level == 4:
        # Special message for level 4 with smaller font
      
        smaller_font = pygame.font.SysFont('Copperplate', 36)  # Even smaller font size
        message_line1 = "Final Level:"
        message_line2 = "You have reached your full evolution"
        color = ORANGE  # Use red for final level message

        # Draw the first line at the center of the screen
        drawText(message_line1, smaller_font, windowSurface, WINDOWWIDTH // 2, (WINDOWHEIGHT // 2) - 40, color)
        # Draw the second line slightly below the first
        drawText(message_line2, smaller_font, windowSurface, WINDOWWIDTH // 2, (WINDOWHEIGHT // 2) + 20, color)

    else:
        # Generic level-up message for all other levels
        message = f"You have reached Level {level}!"
        color = BLACK # Green color for other levels
        drawText(message, Title_design, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 2, color)
    
    # Update the display
    pygame.display.update()
    
    # Pause for 3 seconds
    pygame.time.delay(3000)

# Initialize Pygame
pygame.init()
mainClock = pygame.time.Clock()  # Main clock to control the FPS (frames per second)
pygame.mouse.set_visible(False)  # Hide the mouse cursor

FSP = 60  # Frames per second (FPS) limit


# Set up the game window
pygame.display.set_caption("Wild Quest")  # Set the title of the window
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))  # Create the game window
Title_design = pygame.font.SysFont('Copperplate', 62)  # Font for instructions and title
Instruction_design = pygame.font.SysFont('Copperplate', 30)
Score_design = pygame.font.SysFont('Copperplate', 32)
background = pygame.image.load("background2.png")  # Load the background image for the game

# Function to draw text on the screen
def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, True, color)  # Render the text with the specified color
    textrect = textobj.get_rect()  # Get the rectangle around the text for positioning
    textrect.center = (x, y)  # Center the text rectangle at (x, y)
    surface.blit(textobj, textrect)  # Draw the text on the specified surface

# Load sounds for game events such as game over, background music, and item collection
# Sound effect for touching a heart
gameOverSound = pygame.mixer.Sound('gameover.wav')  # Load the game over sound
pygame.mixer.music.load('Backgroundnoise.mp3')  # Load the background music
pickUpSound = pygame.mixer.Sound("pickup.wav")

# Function to terminate the game
def terminate():
    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

# Function to wait for the player to press a key before starting
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():  # Process events
            if event.type == pygame.QUIT:  # If the window is closed
                terminate()  # Exit the game
            if event.type == pygame.KEYDOWN:  # If a key is pressed
                if event.key == pygame.K_ESCAPE:  # If the Escape key is pressed
                    terminate()  # Exit the game
                return  # Exit the function and start the game

# Display the "Start" screen
# Load images for the starting screen
start_background = pygame.image.load("background1.png")  # Load the start background image
start_image = pygame.image.load("start_image.png")  # Load the start image of the character
start_image = pygame.transform.smoothscale(start_image, (220, 320))  # Scale player image


#Function to display the starting screen
def show_start_screen():
    # Draw the starting background
    windowSurface.blit(start_background, (0, 0))  # Fill the screen with the starting background image
    

    # Draw the start character image on top of the background
    start_image_rect = start_image.get_rect(center=(WINDOWWIDTH // 2, WINDOWHEIGHT // 1.3))  # Center the character image
    windowSurface.blit(start_image, start_image_rect)  # Draw the character image

    # Draw the title and instructions
    drawText('THE WILD QUEST', Title_design, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 4, GREEN)
    drawText('Press SPACE to Jump !', Instruction_design, windowSurface, WINDOWWIDTH // 2, (WINDOWHEIGHT // 4) + 100, BLACK)
    drawText("Press RIGHT Arrow to Move !", Instruction_design, windowSurface, WINDOWWIDTH // 2, (WINDOWHEIGHT // 4) + 150, BLACK)
    drawText('Press a key to start !', Instruction_design, windowSurface, WINDOWWIDTH // 2, (WINDOWHEIGHT // 4) +200, GREEN)  # Positioned below the character image

    pygame.display.update()  # Update the screen

# Display the "Start" screen and wait for player input
show_start_screen()  # Call the function to show the starting screen
waitForPlayerToPressKey()  # Wait for the player to press a key


topScore = 0  # Initialize the top score
game = Game()  # Create an instance of the Game class
running = True  # Set the initial state of the game

# Initialize the LevelManager
level_manager = LevelManager()




# Initialize an enemy group
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
# Variable to track if the speed has already increased and enemy introduced


enemy_spawned = False
last_processed_level=0
#drawTextWithBackground('Score: %s' % (score), Score_design, windowSurface, 160, 25, WHITE, BLACK)
#scorerect = Rect(160,25, 100, 100)
#pygame.draw.rect(windowSurface, BLACK, scorerect.inflate(20, 10))  # Draw a background rectangle with padding


# Main game loop
while True:  # Main game loop
    # Set up the start of a new game
    score = 0  # Reset score for each game
    # level_manager = LevelManager()  # Reset level manager for each game
    level_manager.reset_level()
    pygame.mixer.music.play(-1, 0.0)  # Start background music (-1 means it loops indefinitely)
    
    # Variable to track the current level
    current_level = level_manager.get_level()
    # Game loop
    while running:
        
        score += 1  # Increase score each frame
        level_manager.update_level(score)  # Update level based on the current score
        new_level = level_manager.get_level()  # Get the updated level
        if new_level > current_level:
            current_level = new_level  # Update the current level
            if current_level == 5:
     # Display final "Game Over" message
                windowSurface.blit(background, (0, 0))
                drawText("Congratulations!", Title_design, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 2 - 50, ORANGE)
                drawText("You have completed the game!", Title_design, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 2 + 50, ORANGE)
                pygame.display.update()
                pygame.time.delay(5000)  # Pause to let the player see the message
                running = False  # Stop the game loop
                terminate()  # Exit the game        
            else:
                display_level_message(new_level)  # Display level-up message and pause
        
        if current_level > last_processed_level:
                if current_level == 1:
                    game.player.jumpStrength= -10
                if current_level == 2:
                    game.player.velocityX = 20  # Set player speed for Level 2
                    game.player.jumpStrength= -25  # increase jump strength
                    if not enemy_spawned:
                             # Path to your enemy image                          
                            new_enemy = Enemy(enemyimage="enemy1.png", width=150, height=150)  # Create a new enemy
                            enemies.add(new_enemy)  # Add the enemy to the group
                            enemy_spawned = True


                elif current_level == 3:
                    game.player.velocityX = 50  # Set player speed for Level 3
    
                last_processed_level = current_level  # Update last processed level        
                
        windowSurface.blit(background, (0, 0)) #Draw the background


        
        game.player.apply_gravity()  # Apply gravity to the player
                 
        windowSurface.blit(game.player.image, game.player.rect)  # Draw the player on the screen
        enemies.update()  # Update all enemies
        enemies.draw(windowSurface)  # Draw enemies on the screen
        projectiles.update()
        projectiles.draw(windowSurface)
        
        

        
        if game.pressed.get(pygame.K_RIGHT): #if the right arrow key is pressed 
            if game.player.rect.x + game.player.rect.width < WINDOWWIDTH:
                 game.player.move_right() #Move player to the right 
            
        
        # Handle running and jumping simultaneously 
        if game.pressed.get(pygame.K_SPACE): #If the player is jumping
             game.player.jump() #Make the player jump   

        pygame.display.flip()  # Refresh the screen

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the window is closed
                running = False  # End the game loop
                terminate()  # Terminate the game

            elif event.type == pygame.KEYDOWN:  # If a key is pressed down
                game.pressed[event.key] = True  # Register the key as pressed

                if event.key == pygame.K_b:
                            # Create a new projectile at the player's position
                            new_projectile = Projectile(game.player.rect.x + game.player.rect.width, game.player.rect.y + 50, 15)  # Speed = 15
                            projectiles.add(new_projectile)  # Add to the projectiles group  


            elif event.type == pygame.KEYUP:  # If a key is released
                game.pressed[event.key] = False  # Register the key as released

        

        score+=10
        # Draw score and level on the screen
        # Draw score with a background
        drawTextWithBackground('Score: %s' % (score), Score_design, windowSurface, 160, 25, WHITE, BLACK)
        
        # Adjusted position for the level counter (top-right corner)
        level_text_x = WINDOWWIDTH - 160  # Position near the right edge of the window
        level_text_y = 25  # Same vertical alignment as the score
        drawText('Level: %s' % (level_manager.get_level()), Score_design, windowSurface, level_text_x, level_text_y, ORANGE)  # Draw level in the top right corner

        pygame.display.update()  # Update display to show the score and level

        mainClock.tick(FSP)  # Set the frame rate to limit the game speed

    # Stop the game and show the "Game Over" screen
    pygame.mixer.music.stop()
    gameOverSound.play()
    windowSurface.blit(0, (0, 0))
    drawText('GAME OVER', Title_design, windowSurface, (WINDOWWIDTH / 2), (WINDOWHEIGHT / 4), GREEN)  # Draw title
    drawText('Press a key to start again !', Score_design, windowSurface, (WINDOWWIDTH / 2) - 15, (WINDOWHEIGHT / 2) + 50, WHITE) 
    pygame.display.update()
    waitForPlayerToPressKey()
    gameOverSound.stop()

