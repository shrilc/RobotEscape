import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Create screen
# size argument in set_mode requires tuple - it is immutable - changed ,modified
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RobotEscapeObject")

# robot_image = pygame.image.load("robot2.png")
# robot_image = pygame.transform.scale(robot_image, (50, 50))
# robot_x = 10
# robot_y = 20

object_width = 50
object_height = 50
object_color = (255, 0, 0)
object_rect = pygame.Rect(0, 0, object_width, object_height)

# set the minimum and maximum time the object should appear in seconds
min_appear_time = 10
max_appear_time = 20

# set the minimum and maximum time between the appearances in seconds
min_disappear_time = 7
max_disappear_time = 11

# infinite loop
run = True
while run:
    object_rect.x = random.randint(0, 600)
    object_rect.y = random.randint(0, 600)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, object_color, object_rect)
    pygame.display.flip()

    start_time = time.time()
    while time.time() - start_time < random.uniform(min_appear_time, max_appear_time):
        #Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    screen.fill((255, 255, 255))
    pygame.display.flip()

    start_time = time.time()
    while time.time() - start_time < random.uniform(min_disappear_time, max_disappear_time):
        #Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

pygame.quit()
