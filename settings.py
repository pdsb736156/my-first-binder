# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:45:52 2021

@author: Nathan
"""

class Settings:
    """A class to store all game settings for pong."""
    
    def __init__(self):
        """initialize the game's static settings."""
    
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (0, 0, 0)
        
        # Acknowledgements settings
        self.acknowledgements_width = 625
        self.acknowledgements_height = 325
        
        # Rectangle settings
        self.rectangle_width = 20
        self.rectangle_height = 125
        self.rectangle_speed = 1
        self.right_rectangle_limit = 5
        self.left_rectangle_limit = 5

        # Ball settings
        self.ball_xspeed = 0.25
        self.ball_yspeed = 0.25
        self.ball_trigger_motion = True
        self.ball_multiplier = (-1.1)
        
        # How quickly the game speeds up
        self.speedup_scale = 5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.rectangle_speed = 1.0
        self.ball_xspeed = 0.25
        self.ball_yspeed = 0.25
        
    def increase_speed(self):
        """Increase speed settings."""
        # self.rectangle_speed *= self.speedup_scale
        self.ball_xspeed *= self.speedup_scale
        self.ball_yspeed *= self.speedup_scale