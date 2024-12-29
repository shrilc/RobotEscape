import pygame


class Robot:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("robot.png"), (50, 50))
        self.x = x
        self.y = y

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 5

        if keys[pygame.K_RIGHT]:
            self.x += 5

        if keys[pygame.K_UP]:
            self.y -= 5

        if keys[pygame.K_DOWN]:
            self.y += 5

    def collides_with_sides(self, screen_width, screen_height):
        if self.x <= 0 or self.x >= screen_width - 50 or self.y <= 0 or self.y >= screen_height - 50:
            print("Collides with screen side detected!")
