import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Create screen
# size argument in set_mode requires tuple - it is immutable - changed ,modified
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RobotEscape")

# Robot setup variables
robot_image = pygame.image.load("robot2.png")
robot_image = pygame.transform.scale(robot_image, (50, 50))
robot_x = 100
robot_y = 100

# Object setup variables
object_width = 50
object_height = 50
object_color = (255, 0, 0)
object_rect = pygame.Rect(0, 0, object_width, object_height)
object_visible = True
object_timer = 0

# set the minimum and maximum time the object should appear in seconds
min_appear_time = 5
max_appear_time = 5

# set the minimum and maximum time between the appearances in seconds
min_disappear_time = 3
max_disappear_time = 5

# infinite loop
run = True
while run: #GAME LOOP
    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Robot logic
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        robot_x -= 5

    if keys[pygame.K_RIGHT]:
        robot_x += 5

    if keys[pygame.K_UP]:
        robot_y -= 5

    if keys[pygame.K_DOWN]:
        robot_y += 5

    # Checking if robot collides with sides of the screen
    # if robot_x <= 0:
    #     print("Robot collides at left side")
    #     pygame.quit()
    #
    # if robot_x >= SCREEN_WIDTH - 50:
    #     print("Robot collides at right side")
    #
    # if robot_y <= 0:
    #     print("Robot collides at top side")
    #
    # if robot_y >= SCREEN_HEIGHT - 50:
    #     print("Robot collides at bottom side")

    # Individual state for robot collision with side combined used 'or' operator.
    if robot_x <= 0 or robot_x >= SCREEN_WIDTH - 50 or robot_y <= 0 or robot_y >= SCREEN_HEIGHT - 50:
        print("Collides with screen side detected!")

    # Object
    object_timer += 1
    if object_timer >=60: # Object changes every 60 frames
        object_timer = 0
        object_visible = not object_visible

        if object_visible:
            object_rect.x = random.randint(0, 600)
            object_rect.y = random.randint(0, 600)

    if object_visible and robot_x < object_rect.x + 50 and robot_x + 50 > object_rect.x and robot_y < object_rect.y + 50 and robot_y + 50 > object_rect.y:
        print("Robot collides with Object")

    screen.fill((255, 255, 255))
    screen.blit(robot_image, (robot_x, robot_y))
    if object_visible:
        pygame.draw.rect(screen, object_color, object_rect)

    pygame.display.update()

pygame.quit()

