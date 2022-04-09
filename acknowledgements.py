# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:50:08 2022

@author: Nathan
"""

# Import statements

import pygame

class Acknowledgements:
    """A class to manage the acknowledgements screen."""
    
    def __init__(self, pg_game):
        """Initialize the acknowledgement screen."""
        
        self.screen = pg_game.screen
        self.screen_rect = pg_game.screen.get_rect()
        
        self.settings = pg_game.settings

        # Load the rectangle images and get thier rects
        self.image = pygame.image.load('images/acknowledgements.jpg')
        self.image = pygame.transform.scale(self.image, (self.settings.acknowledgements_width, self.settings.acknowledgements_height))
        self.rect = self.image.get_rect()
        
        # Stat each new rectangle at the middle right of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw the acknowledgement screen at its current location."""
        
        self.screen.blit(self.image, self.rect)