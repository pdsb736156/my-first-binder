# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:59:30 2022

@author: Nathan
"""

import pygame.font

class Title:
    
    def __init__(self, pg_game, msg):
        """Initialize button attributes."""
        self.screen = pg_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button
        self.width, self.height = 500, 125
        self.button_colour = (0, 0, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 144)
        
        # Build the button's rect obect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop
        
        # The button message needs to be prepped only once
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on to the button."""
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.midtop = self.rect.midtop
        
    def draw_title(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)