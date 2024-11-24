import pygame

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RobotEscape")

BLUE = (0, 191, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        #self.image = pygame.Surface((10, 10))
        self.image = pygame.image.load("robot.png")
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


robot = Robot(10, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        robot.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        robot.rect.x += 5
    if keys[pygame.K_UP]:
        robot.rect.y -= 5
    if keys[pygame.K_DOWN]:
        robot.rect.y += 5

    screen.fill(BLACK)
    robot.draw()
    pygame.display.update()


