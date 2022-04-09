# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 16:51:24 2022

@author: Nathan
"""

import pygame.font

class Scoreboard:
    """A class to report scoring information."""
    
    def __init__(self, pg_game):
        """Initialize scorekeeping attributes."""
        
        self.screen = pg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pg_game.settings
        self.stats = pg_game.stats
        
        # Font settings for scoring information
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score images
        self.prep_right_score()
        self.prep_left_score()
        
    def prep_right_score(self):
        """Turn the right rectangle score into a rendered image."""
        
        right_score_str = str(self.stats.right_score)
        self.right_score_image = self.font.render(right_score_str, True, self.text_colour, self.settings.bg_colour)
       
        # Display the right_rectangle score at the top right of the screen
        self.right_score_rect = self.right_score_image.get_rect()
        self.right_score_rect.right = self.screen_rect.right - 20
        self.right_score_rect.top = 20
        
    def prep_left_score(self):
        """Turn the left rectangle score into a rendered image."""
        
        left_score_str = str(self.stats.left_score)
        self.left_score_image = self.font.render(left_score_str, True, self.text_colour, self.settings.bg_colour)
         
        # Display the left_rectangle score at the top left of the screen
        self.left_score_rect = self.left_score_image.get_rect()
        self.left_score_rect.left = self.screen_rect.left + 20
        self.left_score_rect.top = 20
        
    def show_score(self):
        """Draw score to the screen."""
        
        self.screen.blit(self.right_score_image, self.right_score_rect)
        self.screen.blit(self.left_score_image, self.left_score_rect)