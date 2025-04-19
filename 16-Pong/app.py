import pygame
import sys
import os
import random

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
WINNING_SCORE = 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Courier", 24)
large_font = pygame.font.SysFont("Courier", 30, bold=True)

# Load sounds
def load_sound(filename):
    if os.path.exists(filename):
        try:
            return pygame.mixer.Sound(filename)
        except:
            print(f"Error loading sound: {filename}")
    else:
        print(f"Sound file not found: {filename}")
    return None

bounce_sound = load_sound("bounce.wav")
score_sound = load_sound("score.wav")
game_over_sound = load_sound("game_over.wav")

# Function to play sounds
def play_sound(sound):
    if sound:
        try:
            sound.play()
        except:
            print("Error playing sound")

# Game objects
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.speed = 10
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    def move_up(self):
        if self.y > 0:
            self.y -= self.speed
            self.rect.y = self.y
    
    def move_down(self):
        if self.y < HEIGHT - self.height:
            self.y += self.speed
            self.rect.y = self.y
    
    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.reset()
        self.speed_increase = 1.1
    
    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = BALL_SIZE
        self.speed_x = 5 * random.choice([-1, 1])
        self.speed_y = 5 * random.choice([-1, 1])
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        # Wall collision (top and bottom)
        if self.y <= 0 or self.y >= HEIGHT - self.size:
            self.speed_y *= -1
            play_sound(bounce_sound)
        
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

def main():
    # Get player names
    print("Enter Player A name: ")
    player_a_name = input() or "Player A"
    print("Enter Player B name: ")
    player_b_name = input() or "Player B"
    
    # Create game objects
    paddle_a = Paddle(20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    paddle_b = Paddle(WIDTH - 20 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()
    
    # Scores
    score_a = 0
    score_b = 0
    
    # Game state
    running = True
    game_over = False
    winner = ""
    
    # Main game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE and game_over:
                    # Reset game
                    score_a = 0
                    score_b = 0
                    ball.reset()
                    game_over = False
        
        # Get keys pressed
        keys = pygame.key.get_pressed()
        
        if not game_over:
            # Move paddles
            if keys[pygame.K_w]:
                paddle_a.move_up()
            if keys[pygame.K_s]:
                paddle_a.move_down()
            if keys[pygame.K_UP]:
                paddle_b.move_up()
            if keys[pygame.K_DOWN]:
                paddle_b.move_down()
            
            # Update ball
            ball.update()
            
            # Paddle collision
            if ball.rect.colliderect(paddle_a.rect):
                ball.speed_x = abs(ball.speed_x) * ball.speed_increase
                play_sound(bounce_sound)
            
            if ball.rect.colliderect(paddle_b.rect):
                ball.speed_x = -abs(ball.speed_x) * ball.speed_increase
                play_sound(bounce_sound)
            
            # Score
            if ball.x < 0:
                score_b += 1
                play_sound(score_sound)
                ball.reset()
            
            if ball.x > WIDTH:
                score_a += 1
                play_sound(score_sound)
                ball.reset()
            
            # Check for game over
            if score_a >= WINNING_SCORE or score_b >= WINNING_SCORE:
                game_over = True
                winner = player_a_name if score_a >= WINNING_SCORE else player_b_name
                play_sound(game_over_sound)
        
        # Draw everything
        screen.fill(BLACK)
        
        # Draw paddles and ball
        paddle_a.draw()
        paddle_b.draw()
        ball.draw()
        
        # Draw scores
        score_text = font.render(f"{player_a_name}: {score_a}  {player_b_name}: {score_b}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
        
        # Draw center line
        pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
        
        # Draw game over message
        if game_over:
            game_over_text = large_font.render(f"Game Over! {winner} wins!", True, WHITE)
            restart_text = font.render("Press SPACE to play again or Q to quit", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 30))
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 30))
        
        # Update display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(FPS)
    
    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()