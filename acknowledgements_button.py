# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:07:23 2022

@author: Nathan
"""

import pygame.font

class Acknowledgements_button:
    
    def __init__(self, pg_game, msg):
        """Initialize button attributes."""
        self.screen = pg_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_colour = (0, 200, 255)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        
        # Build the button's rect obect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midbottom = self.screen_rect.midbottom
        
        # The button message needs to be prepped only once
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on to the button."""
        self.msg_image = self.font.render(msg, True, self.text_colour, self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.midbottom = self.rect.midbottom
        
    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)