import pygame, random, sys
from classgame import Game  # Import the Game class from the classgame file
from pygame.locals import *  # Import Pygame constants and functions

# Constants for colors and window dimensions

BACKGROUNDCOLOR = (0, 0, 0)  # Background color for the screen (black)
WINDOWWIDTH = 1080  # Width of the game window
WINDOWHEIGHT = 720  # Height of the game window
GREEN = (0, 100, 0)  # Green color 
WHITE = (255, 255, 255)  # White color 
BLACK = (0,0,0)
ORANGE = (255, 128, 0)

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

while True:  # Main game loop
    # Set up the start of a new game
    score = 0  # Reset score for each game
    pygame.mixer.music.play(-1, 0.0)  # Start background music (-1 means it loops indefinitely)
    
    # Game loop
    while running:
        score += 1  # Increase score each frame
        windowSurface.blit(background, (0, 0))  # Draw the background
        game.player.apply_gravity()  # Apply gravity to the player

        # Draw the player character
        windowSurface.blit(game.player.image, game.player.rect)  # Draw the player on the screen

        # Check if the right arrow key is pressed and if the player is within screen bounds
        if game.pressed.get(pygame.K_RIGHT) and 0 < game.player.rect.x + game.player.rect.width < WINDOWWIDTH:
            game.player.move_right()  # Move player to the right
        
        # Check if the space key is pressed and if the player is not already jumping
        elif game.pressed.get(pygame.K_SPACE) and not game.player.isJumping:
            game.player.jump()  # Make the player jump
    
        pygame.display.flip()  # Refresh the screen

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the window is closed
                running = False  # End the game loop
                terminate()  # Terminate the game

            elif event.type == pygame.KEYDOWN:  # If a key is pressed down
                game.pressed[event.key] = True  # Register the key as pressed
            elif event.type == pygame.KEYUP:  # If a key is released
                game.pressed[event.key] = False  # Register the key as released

        # Increase score and display it on the screen
        score += 1
        drawText('Score: %s' % (score), Score_design, windowSurface, 160, 25, BLACK)  # Draw score in the top left corner
        pygame.display.update()  # Update display to show the score

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
      