import pygame

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

    # if keys[pygame.K_LEFT]:
    #     robot_x -= 5
    # elif keys[pygame.K_RIGHT]:
    #     robot_x += 5
    # elif keys[pygame.K_UP]:
    #     robot_y -= 5
    # elif keys[pygame.K_DOWN]:
    #     robot_y += 5

    if robot_x <= 0:
        print("Robot collides at left side")
        pygame.quit()

    if robot_x >= SCREEN_WIDTH - 50:
        print("Robot collides at right side")

    if robot_y <= 0:
        print("Robot collides at top side")

    if robot_y >= SCREEN_HEIGHT - 50:
        print("Robot collides at bottom side")


    screen.fill((255, 255, 255))
    screen.blit(robot_image, (robot_x, robot_y))
    pygame.draw.rect(screen, object_color, object_rect)
    #screen.blit(robot_image, (40, 50))
    pygame.display.update()

pygame.quit()

