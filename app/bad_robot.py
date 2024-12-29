import pygame
import random


class BadRobot:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.visible = True
        self.timer = 0

    def appear_disappear(self):
        self.timer += 1
        if self.timer >=60: # Object changes every 60 frames
            self.timer = 0
            self.visible = not self.visible

            if self.visible:
                self.rect.x = random.randint(0, 600)
                self.rect.y = random.randint(0, 600)

    def collides_with_robot(self, robot):
        if self.visible and robot.x < self.rect.x + 50 and robot.x + 50 > self.rect.x and robot.y < self.rect.y + 50 and robot.y + 50 > self.rect.y:
            print("Robot collides with bad robot")


