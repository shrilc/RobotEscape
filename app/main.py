import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Create screen
# size argument in set_mode requires tuple - it is immutable - changed ,modified
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RobotEscape")

robot_image = pygame.image.load("robot2.png")
robot_x = 10
robot_y = 20

# infinite loop
run = True
while run:
    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot_x -= 5
    if keys[pygame.K_RIGHT]:
        robot_x += 5
    if keys[pygame.K_UP]:
        robot_y -= 5
    if keys[pygame.K_DOWN]:
        robot_y += 5

    screen.blit(robot_image, (robot_x, robot_y))
    #screen.blit(robot_image, (40, 50))
    pygame.display.update()

pygame.quit()

