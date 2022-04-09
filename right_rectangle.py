# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:00:21 2021

@author: Nathan
"""

# Import statements

import pygame

class RightRectangle:
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
        
        # Stat each new rectangle at the middle right of the screen
        self.rect.midright = self.screen_rect.midright
        
        # Store a decimal value for the ship's vertical position
        self.y = float(self.rect.y)
        
        # Movement flag
        self.right_rectangle_up = False
        self.right_rectangle_down = False
        
    def update(self):
        """Update the rectangle's position based on movement flags."""
        
        if self.right_rectangle_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rectangle_speed
            
        if self.right_rectangle_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rectangle_speed
            
        # Update rect object from self.y
        self.rect.y = self.y
        
    def center_right_rectangle(self):
        """Center the right rectangle on the screen."""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
        
    def reset_right_rectangle(self):
        """Resets the position of the right rectangle after a player loses a life."""
        
        # Start each new rectangle at the middle right of the screen
        self.rect.midright = self.screen_rect.midright
        
    def blitme(self):
        """Draw the rectangles at their current location."""
        
        self.screen.blit(self.image, self.rect)
    