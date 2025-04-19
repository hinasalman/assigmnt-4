import pygame
import random
from typing import List, Tuple

class SpaceInvaders:
    """Main game class for Space Invaders."""
    
    # Colors
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    RED: Tuple[int, int, int] = (255, 0, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    BLUE: Tuple[int, int, int] = (0, 0, 255)
    YELLOW: Tuple[int, int, int] = (255, 255, 0)
    
    def __init__(self, width: int = 800, height: int = 600):
        """Initialize the game with screen dimensions."""
        # Initialize pygame
        pygame.init()
        
        # Screen settings
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Invaders (Winning Condition)")
        
        # Fonts
        self.font = pygame.font.Font(None, 36)
        
        # Player settings
        self.player_width = 50
        self.player_height = 10
        self.player_x = self.WIDTH // 2 - self.player_width // 2
        self.player_y = self.HEIGHT - 50
        self.player_speed = 5
        
        # Enemy settings
        self.enemy_radius = 20
        self.enemy_x = random.randint(50, self.WIDTH - 50)
        self.enemy_y = 50
        self.enemy_speed = 3
        self.enemy_direction = 1  # 1 = right, -1 = left
        
        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_speed = 7
        self.bullets: List[List[int]] = []
        
        # Power-up settings
        self.power_up_active = False
        self.power_up_x = random.randint(50, self.WIDTH - 50)
        self.power_up_y = random.randint(100, self.HEIGHT - 200)
        
        # Game variables
        self.score = 0
        self.lives = 3
        self.WINNING_SCORE = 10  # Change this to set how many points to win
        self.high_score = 0
        self.clock = pygame.time.Clock()
        self.running = True
    
    def is_collision(self, enemy_x: float, enemy_y: float, bullet_x: float, bullet_y: float) -> bool:
        """Check if a bullet has collided with an enemy."""
        distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
        return distance < self.enemy_radius
    
    def handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Shoot immediately
                    self.bullets.append([self.player_x + self.player_width // 2, self.player_y])
    
    def update_player(self) -> None:
        """Update player position based on keyboard input."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_x > 0:
            self.player_x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.player_x < self.WIDTH - self.player_width:
            self.player_x += self.player_speed
    
    def update_enemy(self) -> None:
        """Update enemy position and direction."""
        self.enemy_x += self.enemy_speed * self.enemy_direction
        if self.enemy_x <= 0 or self.enemy_x >= self.WIDTH - self.enemy_radius:
            self.enemy_direction *= -1  # Change direction
    
    def update_bullets(self) -> None:
        """Update bullet positions and handle collisions."""
        # Move bullets and remove if off-screen
        for bullet in self.bullets[:]:
            bullet[1] -= self.bullet_speed
            if bullet[1] < 0:
                self.bullets.remove(bullet)
        
        # Check for collisions
        for bullet in self.bullets[:]:
            if self.is_collision(self.enemy_x, self.enemy_y, bullet[0], bullet[1]):
                self.bullets.remove(bullet)
                self.score += 1  # Increase score
                if self.score > self.high_score:
                    self.high_score = self.score
                self.enemy_x = random.randint(50, self.WIDTH - 50)  # Respawn enemy
                self.enemy_y = 50  # Reset enemy position at the top
        
        # Check if enemy reached bottom
        if self.enemy_y >= self.HEIGHT - 50:
            self.lives -= 1
            self.enemy_y = 50
            self.enemy_x = random.randint(50, self.WIDTH - 50)  # Respawn enemy
    
    def check_game_over(self) -> bool:
        """Check if the game is over (win or lose)."""
        # Winning condition
        if self.score >= self.WINNING_SCORE:
            self.show_end_screen("You Win! Press Q to Quit")
            return True
        
        # Game over condition
        if self.lives <= 0:
            self.show_end_screen("Game Over! Press Q to Quit")
            return True
        
        return False
    
    def show_end_screen(self, message: str) -> None:
        """Show the end game screen with a message."""
        self.screen.fill(self.BLACK)
        text = self.font.render(message, True, self.YELLOW)
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        
        # Wait for player to quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    waiting = False
                    self.running = False
    
    def draw(self) -> None:
        """Draw all game elements to the screen."""
        self.screen.fill(self.BLACK)  # Clear screen
        
        # Draw player
        pygame.draw.rect(self.screen, self.BLUE, (self.player_x, self.player_y, self.player_width, self.player_height))
        
        # Draw enemy
        pygame.draw.circle(self.screen, self.RED, (int(self.enemy_x), int(self.enemy_y)), self.enemy_radius)
        
        # Draw bullets
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, self.GREEN, (bullet[0], bullet[1], self.bullet_width, self.bullet_height))
        
        # Display Score and Lives
        score_text = self.font.render(f"Score: {self.score} | High Score: {self.high_score}", True, self.WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 40))
        
        pygame.display.update()  # Update screen
    
    def run(self) -> None:
        """Main game loop."""
        while self.running:
            self.clock.tick(60)  # 60 FPS
            self.handle_events()
            if self.check_game_over():
                continue
            self.update_player()
            self.update_enemy()
            self.update_bullets()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    game = SpaceInvaders()
    game.run()
