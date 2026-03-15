import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))  # width=800, height=600
pygame.display.set_caption("My First Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close button pressed
            running = False

    screen.fill((0, 0, 0))  # Fill screen with black
    pygame.display.flip()   # Update the display

pygame.quit()