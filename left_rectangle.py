# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:28:25 2021

@author: Nathan
"""

# Import statements

import pygame

class LeftRectangle:
    """A class to manage the rectangles."""
    
    def __init__(self, pg_game):
        """Initialize the rectangles and set their starting positions."""
        
        self.screen = pg_game.screen
        self.screen_rect = pg_game.screen.get_rect()
        
        self.settings = pg_game.settings

        # Load the rectangle images and get thier rects
        self.image = pygame.image.load('images/white rectangle.png')
        self.image = pygame.transform.scale(self.image, (self.settings.rectangle_width, self.settings.rectangle_height))
        self.rect = self.image.get_rect()
        
        # Start each new rectangle at the middle right of the screen
        self.rect.midleft = self.screen_rect.midleft
        
        # Store a decimal value for the ship's vertical position
        self.y = float(self.rect.y)
        
        # Movement flag
        self.left_rectangle_up = False
        self.left_rectangle_down = False
        
    def update(self):
        """Update the rectangle's position based on movement flags."""
        
        if self.left_rectangle_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rectangle_speed
            
        if self.left_rectangle_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rectangle_speed
            
        # Update rect object from self.y
        self.rect.y = self.y
    
    def reset_left_rectangle(self):
        """Resets the position of the left rectangle after a player loses a life."""
        
        # Start each new rectangle at the middle right of the screen
        self.rect.midleft = self.screen_rect.midleft
        
    def blitme(self):
        """Draw the rectangles at their current location."""
        
        self.screen.blit(self.image, self.rect)
    