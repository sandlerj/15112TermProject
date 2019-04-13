## The Ship Sprite
#Made with some reference to Lukas Peraza's pygame templates:


import pygame, os

class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join("Photos", "ship.png"))
        self.image = self.image.convert_alpha()
        self.width, self.height self.image.get_size()
        self.rect = self.image.get_rect()
        self.updateRect()
        self.dx = 0
        self.speed = 10

    def updateRect(self):
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2,
                                self.x + self.width//2, self.y + self.height//2)

    def update(self, keysDown, screenWidth, screenHeight):
        if keysDown(pygame.K_LEFT) and keysDown(pygame.K_RIGHT):
            self.dx = 0
        elif keysDown(pygame.K_LEFT):
            self.dx = -1
        elif keysDown(pygame.K_RIGHT):
            self.dx = 1
        else:
            self.dx = 0

        self.x += self.speed * self.dx
        self.updateRect()
