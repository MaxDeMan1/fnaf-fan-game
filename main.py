import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 400), pygame.SCALED | pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

office : pygame.Surface = pygame.image.load("/home/max/Pictures/fnaf/office.png")
left_door_area = pygame.Rect(0, 120, 185, 300)
right_vent_area = pygame.Rect(610, 125, 125, 115)

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if left_door_area.collidepoint(event.pos):
                    print("left")
                if right_vent_area.collidepoint(event.pos):
                    print("right")

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # Rendering
    screen.blit(office)
    # pygame.draw.rect(screen, (100, 200, 50), right_vent_area) # TODO: REMOVE

    pygame.display.flip() # Puts work on screen
    delta = clock.tick() / 1000 # Sets delta time

pygame.quit()

