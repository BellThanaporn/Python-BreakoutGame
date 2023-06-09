import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. 
    #It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels): 
        self.rect.x -= pixels
	    #Check that you are not going too far (off the screen)
        if self.rect.x < 0:
          self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > 700:
          self.rect.x = 700

    
