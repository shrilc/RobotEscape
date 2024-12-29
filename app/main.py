import pygame
from robot import Robot
from bad_robot import BadRobot

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Create screen
# size argument in set_mode requires tuple - it is immutable - changed ,modified
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RobotEscape")

# Initialize robot object
robot = Robot(x=100, y=100)

# Initialize bad robot
bad_robot = BadRobot()
bad_robot2 = BadRobot()
bad_robot3 = BadRobot()

# Game scores and levels
score = 0
level = 0

# infinite loop
run = True
while run: #GAME LOOP
    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # game logic
    keys = pygame.key.get_pressed()

    # Call the robot move method here
    robot.move(keys)
    robot.collides_with_sides(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Bad robot
    bad_robot.appear_disappear()
    bad_robot.collides_with_robot(robot)

    # Bad robot 2
    bad_robot2.appear_disappear()
    bad_robot2.collides_with_robot(robot)

    # Bad robot 3
    bad_robot3.appear_disappear()
    bad_robot3.collides_with_robot(robot)

    screen.fill((255, 255, 255))
    screen.blit(robot.image, (robot.x, robot.y))
    if bad_robot.visible:
        pygame.draw.rect(screen, bad_robot.color, bad_robot.rect)

    if bad_robot2.visible:
        pygame.draw.rect(screen, bad_robot2.color, bad_robot2.rect)

    if bad_robot3.visible:
        pygame.draw.rect(screen, bad_robot3.color, bad_robot3.rect)

    pygame.display.update()

pygame.quit()

