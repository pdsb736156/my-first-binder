# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 11:30:58 2022

@author: Nathan
"""

class GameStats:
    """Track statistics for Pong."""
    
    def __init__(self, pg_game):
        """Initialize statistics."""
        
        self.settings = pg_game.settings
        self.reset_right_stats()
        self.reset_left_stats()
        
        self.game_active = False
        
    def reset_right_stats(self):
        """Initialize statistics that can change during the game."""
        
        self.right_rectangles_left = self.settings.right_rectangle_limit
        
        self.right_score = self.right_rectangles_left
        
    def reset_left_stats(self):
        """Initialize statistics that can change during the game."""
        
        self.left_rectangles_left = self.settings.left_rectangle_limit

        self.left_score = self.left_rectangles_left
