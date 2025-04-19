class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = 5
        self.rect = (x, y, width, height)
    
    def move(self, keys, window_width=800, window_height=600):
        """Move player based on key presses"""
        # Up
        if keys[0]:
            self.y = max(0, self.y - self.velocity)
        # Down
        if keys[1]:
            self.y = min(window_height - self.height, self.y + self.velocity)
        # Left
        if keys[2]:
            self.x = max(0, self.x - self.velocity)
        # Right
        if keys[3]:
            self.x = min(window_width - self.width, self.x + self.velocity)
        
        # Update rectangle position
        self.update_rect()
    
    def update_rect(self):
        """Update the rectangle position"""
        self.rect = (self.x, self.y, self.width, self.height)
    
    def draw(self, win):
        """Draw the player on the window"""
        import pygame
        pygame.draw.rect(win, self.color, self.rect)