# ---- Import verything ----
import pygame, random, sys
from classgame import Game  # Import the Game class from the classgame file
from pygame.locals import *  # Import Pygame constants and functions
from classlevelmanagement import LevelManager # Import the LevelManager class from the classlevelmanagement file
from classprojectile import Projectile # Import the Projectile class from the classprojectile file
from classenemy import Enemy # Import the Enemy class from the classenemy file
from classtree import TreeObstacle
from classobstacle import PineappleRain 


# ---- Color and window dimension ----
BACKGROUNDCOLOR = (0, 0, 0)  # Background color for the screen (black)
WINDOWWIDTH = 1080  # Width of the game window
WINDOWHEIGHT = 720  # Height of the game window
GREEN = (0, 100, 0)  # Green color 
WHITE = (255, 255, 255)  # White color 
BLACK = (0,0,0)# Black color 
ORANGE = (255, 128, 0)# Orange color 


# ---- All functions ---- 

# Function to draw text on the screen
def drawText(text, font, surface, x, y, color):
    textobj = font.render(text, True, color)  # Render the text with the specified color
    textrect = textobj.get_rect()  # Get the rectangle around the text for positioning
    textrect.center = (x, y)  # Center the text rectangle at (x, y)
    surface.blit(textobj, textrect)  # Draw the text on the specified surface

# Function to draw text with a background for better visibility
def drawTextWithBackground(text, font, surface, x, y, text_color, bg_color):
    textobj = font.render(text, True, text_color)  # Render the text with the specified color
    textrect = textobj.get_rect(center=(x, y))  # Center the text rectangle at (x, y)
    pygame.draw.rect(surface, bg_color, textrect.inflate(20, 10))  # Draw a background rectangle with padding
    surface.blit(textobj, textrect)  # Draw the text on the specified surface

# Function to terminate the game
def terminate():
    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

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
    drawText('Press RIGHT or LEFT Arrow to Move !', Instruction_design, windowSurface, WINDOWWIDTH // 2, (WINDOWHEIGHT // 4) + 150, BLACK)
    drawText('Press B to Launch a Projectile !', Instruction_design, windowSurface, WINDOWWIDTH // 2, (WINDOWHEIGHT // 4) + 200, BLACK)
    drawText('Press a key to start !', Instruction_design, windowSurface, WINDOWWIDTH // 2, (WINDOWHEIGHT // 4) + 250, GREEN)  # Positioned below all instructions


    pygame.display.update()  # Update the screen


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

# Function to spawn enemies 
def spawn_enemies(level, enemy_group, enemy_images, width, height):
    
    enemy_group.empty()  # Clear existing enemies
    #spawn_y = 500  # Fixed vertical position for all enemies

    for i in range(level):  # Spawn enemies equal to the level number
        random_enemy_image = random.choice(enemy_images)  # Randomly select an enemy image
        #spawn_x = random.randint(1080, 1280)  # Random X spawn position off-screen to the right
        #new_enemy = Enemy(random_enemy_image, width, height, spawn_y)
        new_enemy = Enemy(random_enemy_image, width, height)
        #new_enemy.rect.x = spawn_x  # Set the enemy's initial X-coordinate
        enemy_group.add(new_enemy)
 
        
    return enemy_group

# Function to create the "Game Over" 
def handle_game_over():
    global game_over_triggered, running

    # Marque l'état "Game Over"
    game_over_triggered = True
    running = False

    # Stoppe la musique et joue le son "Game Over"
    pygame.mixer.music.stop()
    gameOverSound.play()
    

    # Affiche l'écran de "Game Over"
    windowSurface.blit(background, (0, 0))
    dead_player_image = pygame.image.load("dead_player.png").convert_alpha()
    dead_player_image = pygame.transform.smoothscale(dead_player_image, (300, 300))
    dead_player_rect = dead_player_image.get_rect(center=(WINDOWWIDTH // 2, WINDOWHEIGHT - 150))
    windowSurface.blit(dead_player_image, dead_player_rect)
    drawText('GAME OVER', Title_design, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 4, BLACK)
    drawText('Press any key to quit the game!', Score_design, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 3, BLACK)
    pygame.display.update()

    # Attends que le joueur appuie sur une touche
    waitForPlayerToPressKey()
    terminate()



# ---- Initialize Pygame ----
pygame.init()

# ---- Control FPS (frame per second) ----

mainClock = pygame.time.Clock()  
FSP = 30  
# ---- GameFrameRateControl ----
mainClock = pygame.time.Clock() 

# ---- Hide the mouse cursor   ----
pygame.mouse.set_visible(False)  


# ---- Set up the game window ----
pygame.display.set_caption("Wild Quest")  # Set the title of the window
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))  # Create the game window
Title_design = pygame.font.SysFont('Copperplate', 62)  # Font for instructions and title
Instruction_design = pygame.font.SysFont('Copperplate', 30)
Score_design = pygame.font.SysFont('Copperplate', 32)
background = pygame.image.load("background2.png")  # Load the background image for the game

# ---- Load sounds for game events such as game over, background music, and item collection ----
gameOverSound = pygame.mixer.Sound('gameover.wav')  # Load the game over sound
pygame.mixer.music.load('Backgroundnoise.mp3')  # Load the background music
pickUpSound = pygame.mixer.Sound("pickup.wav")

# ---- Load images for the starting screen ----
start_background = pygame.image.load("background1.png")  # Load the start background image
start_image = pygame.image.load("start_image.png")  # Load the start image of the character
start_image = pygame.transform.smoothscale(start_image, (220, 320))  # Scale player image

# ---- List of enemy images ---- 
enemy_images = [
    "enemy1.png",  # Path to enemy1
    "enemy2.png",  # Path to enemy2
    "enemy3.png"   # Path to enemy3
]
enemy_image_1 = pygame.image.load("enemy1.png")

 
# ---- Initialize everything ----

#Initialize the top score 
topScore = 0  

## Create an instance of the Game class
game = Game()  

# Set the initial state of the game
running = True  

# Initialize the LevelManager
level_manager = LevelManager()
last_processed_level=0

# Initialize enemies 
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group() # Timer 
enemy_spawned = False
speed_limit = 10

# Initialize trees
trees = pygame.sprite.Group()  
tree_spawn_time = pygame.time.get_ticks()  # Timer 

# Initialize pineapple
pineapple_group = pygame.sprite.Group() 
pineapple_spawn_time = pygame.time.get_ticks() #Timer 

game_over_triggered = False #Indicate if the play is "Game Over"
vision_range = 20
counter = 0

# ---- Display ---- 
show_start_screen()  # Call the function to show the starting screen
waitForPlayerToPressKey()  # Wait for the player to press a key
pygame.display.update()


# MAIN GAME LOOP
while True:  # Main game loop
# Set everything 

    # Set up the start of a new game
    score = 0  # Reset score for each game

    # level_manager = LevelManager()  # Reset level manager for each game
    level_manager.reset_level()

    # Start background music (-1 means it loops indefinitely)
    pygame.mixer.music.play(-1, 0.0) 

    # Variable to track the current level
    current_level = level_manager.get_level()
       
    # Track time for incremental enemy spawning
    enemy_spawn_time = 0
    # Track time for incremental enemy spawning  
    time_between_spawns = 2000  

    # Game loop
    while running:

# ---- Handle events ----
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

# ---- Moves of the player ----  
        if game.pressed.get(pygame.K_RIGHT): #if the right arrow key is pressed 
            if game.player.rect.x + game.player.rect.width < WINDOWWIDTH:
                    game.player.move_right() #Move player to the right            
        if game.pressed.get(pygame.K_LEFT):
                if game.player.rect.x > 0:
                    game.player.move_left() 
        if game.pressed.get(pygame.K_SPACE): #If the player is jumping
                game.player.jump() #Make the player jump  

        game.player.apply_gravity()  # Apply gravity to the player 
        
# ---- Update level ---- 
        level_manager.update_level(score)  # Update level based on the current score
        new_level = level_manager.get_level()  # Get the updated level
        if new_level > current_level:
            current_level = new_level  # Update the current level
            enemies.empty()  # Clear all enemies from the previous level
            display_level_message(new_level)  # Display level-up message and pause

            # Reset the timer to control enemy spawns for this level
            enemy_spawn_time = pygame.time.get_ticks()

            if current_level == 5:
                # Final level completion logic
                windowSurface.blit(background, (0, 0))
                drawText("Congratulations!", Title_design, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 2 - 50, ORANGE)
                drawText("You have completed the game!", Title_design, windowSurface, WINDOWWIDTH // 2, WINDOWHEIGHT // 2 + 50, ORANGE)
                pygame.display.update()
                pygame.time.delay(5000)  # Pause to let the player see the message
                running = False  # Stop the game loop
                terminate()  # Exit the game

# ---- Spawn ----
        # Spawn one enemy at a time based on the timer
        current_time = pygame.time.get_ticks()
        if current_time - enemy_spawn_time >= time_between_spawns and len(enemies) < current_level:
            random_enemy_image = random.choice(enemy_images)
            new_enemy = Enemy(random_enemy_image, 150, 150)  # Adjust dimensions as needed
            enemies.add(new_enemy)
            enemy_spawn_time = current_time  # Reset the spawn timer

        

        # Spawn enemies 
        if current_level > last_processed_level:
            if current_level == 1 and len(enemies) < 1: 
                game.player.jumpStrength = -25
                new_enemies = spawn_enemies(1, enemies, enemy_images, 150, 150)  # Level 1: 1 enemy
                enemies = new_enemies
             
            elif current_level == 2 and len(enemies) < 2: 
                game.player.velocityX = 30
                game.player.jumpStrength = -25
                new_enemies = spawn_enemies(2, enemies, enemy_images, 150, 150)  # Level 2: 2 enemies
                enemies = new_enemies
                
            elif current_level == 3 and len(enemies) < 3: 
                game.player.velocityX = 35
                new_enemies = spawn_enemies(3, enemies, enemy_images, 150, 150)  # Level 3: 3 enemies
                enemies = new_enemies 
            
            elif current_level == 4 and len(enemies) < 4: 
                game.player.velocityX = 40
                new_enemies = spawn_enemies(4, enemies, enemy_images, 150, 150)  # Level 4: 4 enemies
                enemies = new_enemies  

        # Spawn a tree 
        current_time = pygame.time.get_ticks()
        if current_time - tree_spawn_time > random.randint(5000, 8000):  # Spawn toutes les 3 à 5 secondes
            new_tree = TreeObstacle("tree.png", WINDOWWIDTH, WINDOWHEIGHT)  # Initialise un tronc
            trees.add(new_tree)  # Ajoute le tronc au groupe
            tree_spawn_time = current_time  # Réinitialise le timer

        # Spawn pineapple 
        current_time = pygame.time.get_ticks()
        if current_time - pineapple_spawn_time > 500 and len(pineapple_group) < 5:
            pineapple = PineappleRain(WINDOWWIDTH, WINDOWHEIGHT)
            pineapple_group.add(pineapple)
            pineapple_spawn_time = current_time


# ---- Draw score with a background ----
        drawTextWithBackground('Score: %s' % (score), Score_design, windowSurface, 160, 25, WHITE, BLACK)
        level_text_x = WINDOWWIDTH - 160  # Position near the right edge of the window
        level_text_y = 25  # Same vertical alignment as the score
        drawText('Level: %s' % (level_manager.get_level()), Score_design, windowSurface, level_text_x, level_text_y, ORANGE)  # Draw level in the top right corner

        pygame.display.update()  # Update display to show the score and level

        


# ---- Draw everything ----
        windowSurface.blit(background, (0, 0)) #Draw the background              
        windowSurface.blit(game.player.image, game.player.rect)  # Draw the player on the screen
        enemies.update()  # Update all enemies
        enemies.draw(windowSurface)  # Draw enemies on the screen
        projectiles.update()
        projectiles.draw(windowSurface)
        trees.update()  # Met à jour les positions des troncs
        trees.draw(windowSurface)  # Dessine les troncs sur l’écran
        pineapple_group.update() # Mettre à jour les postions des ananas 
        pineapple_group.draw(windowSurface) # Dessiner les anans sur l'écran

        pygame.display.update()  

# ---- Collisions ----

        # Detect collisions between trees and pplayer
        if pygame.sprite.spritecollide(game.player, trees, False) and not game_over_triggered:  # Vérifie les collisions entre le joueur et les troncs
            handle_game_over()
        
        # Detect collisions between enemies and player 
        if pygame.sprite.spritecollide(game.player, enemies, False) and not game_over_triggered:
            handle_game_over()
        
        # Detect collisions between pineapple and player 
        if pygame.sprite.spritecollide(game.player, pineapple_group, False) and not game_over_triggered:
            handle_game_over()
        
        # Detect collisions between projectiles and enemies
        collisions = pygame.sprite.groupcollide(projectiles, enemies, True, True)
        if collisions:
            for hit in collisions:
                score += 100
                pickUpSound.play()
        
        
        mainClock.tick(FSP)  #Control FSP
        pygame.display.flip()  # Refresh the screen