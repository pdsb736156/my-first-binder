# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:56:26 2021

@author: Nathan
"""

# Import statements

import pygame

class Ball:
    """A class to represent the ball."""
    
    def __init__(self, pg_game):
        """Initialize the ball and set its starting position."""
        
        self.screen = pg_game.screen
        self.screen_rect = pg_game.screen.get_rect()
        self.settings = pg_game.settings
        self.right_rectangle = pg_game.right_rectangle
        self.left_rectangle = pg_game.left_rectangle
        
        # Store the right rectangle's y value
        self.right_rectangle_y_loc = self.right_rectangle.y
        
        # Load the ball image and set its rect attribute
        self.image = pygame.image.load('images/ball.png')
        self.image = pygame.transform.scale(self.image, (25,25))
        self.rect = self.image.get_rect()

        # Start each new ball at the top of the screen
        self.rect.center = self.screen_rect.center

        # Store the ball's exact horizontal position
        self.x = float(self.rect.x)
        
        # Store the ball's exact vertical position
        self.y = float(self.rect.y)

        # Store the ball's speeds
        self.x_speed = self.settings.ball_xspeed
        
        self.y_speed = self.settings.ball_yspeed
        
    def update(self):
        """Update the ball's position."""
                
        # if self.settings.ball_trigger_motion:
            
        self.x -= self.x_speed

        self.y += self.y_speed
        
        # if self.x <= 0:
            # self.x_speed = self.x_speed * (-1)
            
        # elif self.x >= self.settings.screen_width:
            # self.x_speed *= -1

        if self.y <= 0:
            self.y_speed *= -1
            
        elif self.y >= self.settings.screen_height:
            self.y_speed *= -1
            
        self.rect.x = self.x
        self.rect.y = self.y
        
        # self.settings.ball_trigger_motion = False
        
    def update_after_collision_with_right_rectangle(self):
        """Update the ball's position after colliding with the right rectangle."""
        
        # self.x -= self.x_speed

        # self.y += self.y_speed
        
        # if self.x <= (self.settings.rectangle_width):
        
        # if self.y > self.right_rectangle_y_loc:
       #  self.x_speed *= (-1)
            # self.y_speed *= (1.1)
            
        # else:
        self.x_speed *= (self.settings.ball_multiplier)
        # self.y_speed *= (self.settings.ball_multiplier)
            
            
        # elif self.x >= self.settings.screen_width - (self.settings.rectangle_width):
            # self.x_speed *= -1

        # if self.y <= 0:
        # self.y_speed *= 1
            
        # elif self.y >= self.settings.screen_height:
            # self.y_speed *= -1
            
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update_after_collision_with_left_rectangle(self):
        """Update the ball's position after colliding with the left rectangle."""
                
        # self.x -= self.x_speed
        
        # self.y += self.y_speed
        
        self.x_speed *= (self.settings.ball_multiplier)
        # self.y_speed *= (self.settings.ball_multiplier)
        
        self.rect.x = self.x
        self.rect.y = self.y
        
    def reset_ball(self):
        """Resets the location of the ball after a player loses a life."""
        
        # Start each new ball at the top of the screen
        self.rect.center = self.screen_rect.center
        
        # Store the ball's exact horizontal position
        self.x = float(self.rect.x)
        
        # Store the ball's exact vertical position
        self.y = float(self.rect.y)
        
        # self.settings.ball_trigger_motion = True
        
    def blitme(self):
        """Draw the rectangles at their current location."""
        
        self.screen.blit(self.image, self.rect)