import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE
WHITE, BLACK, GRAY, RED, GREEN, BLUE, CYAN, ORANGE, PURPLE, YELLOW = (
    (255, 255, 255), (0, 0, 0), (128, 128, 128), (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (0, 255, 255), (255, 165, 0), (160, 32, 240), (255, 255, 0)
)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]
COLORS = [CYAN, YELLOW, PURPLE, RED, GREEN, ORANGE, BLUE]

class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x, self.y = COLUMNS // 2 - len(shape[0]) // 2, 0

    def rotate(self):
        return [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.current_piece = self.new_piece()
        self.hold_piece = None
        self.held = False
        self.running = True
        self.score = 0
        self.level = 1
        self.fall_speed = 500  # Faster drop speed for smooth gameplay

    def new_piece(self):
        index = random.randint(0, len(SHAPES) - 1)
        return Tetromino(SHAPES[index], COLORS[index])

    def move(self, dx, dy):
        if not self.check_collision(dx, dy):
            self.current_piece.x += dx
            self.current_piece.y += dy

    def hard_drop(self):
        while not self.check_collision(0, 1):
            self.current_piece.y += 1
        self.lock_piece()

    def check_collision(self, dx, dy):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_piece.x + x + dx
                    new_y = self.current_piece.y + y + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                        return True
                    if new_y >= 0 and self.grid[new_y][new_x] != BLACK:
                        return True
        return False

    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_y, new_x = self.current_piece.y + y, self.current_piece.x + x
                    if new_y >= ROWS:
                        self.running = False
                        return
                    self.grid[new_y][new_x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = self.new_piece()
        if self.check_collision(0, 0):
            self.running = False

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == BLACK for cell in row)]
        lines_cleared = ROWS - len(new_grid)
        self.score += lines_cleared * 10
        self.level = self.score // 50 + 1  # Increase speed every 50 points
        self.fall_speed = max(50, 500 - (self.level * 30))  # Make game faster gradually
        self.grid = [[BLACK] * COLUMNS] * lines_cleared + new_grid

    def swap_hold(self):
        if self.held:
            return
        if self.hold_piece:
            self.current_piece, self.hold_piece = self.hold_piece, self.current_piece
        else:
            self.hold_piece = self.current_piece
            self.current_piece = self.new_piece()
        self.held = True

    def draw(self, screen):
        screen.fill(GRAY)
        for y in range(ROWS):
            for x in range(COLUMNS):
                pygame.draw.rect(screen, self.grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.current_piece.color, ((self.current_piece.x + x) * BLOCK_SIZE, (self.current_piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
        pygame.display.flip()

    def run(self):
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        fall_time = 0

        while self.running:
            screen.fill(BLACK)
            fall_time += clock.get_rawtime()
            if fall_time > self.fall_speed:
                if not self.check_collision(0, 1):
                    self.current_piece.y += 1
                else:
                    self.lock_piece()
                fall_time = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.move(0, 1)
                    elif event.key == pygame.K_UP:
                        rotated_shape = self.current_piece.rotate()
                        if not self.check_collision(0, 0):
                            self.current_piece.shape = rotated_shape
                    elif event.key == pygame.K_SPACE:
                        self.hard_drop()
                    elif event.key == pygame.K_c:
                        self.swap_hold()

            self.draw(screen)
            clock.tick(60)  # Increased frame rate for smooth gameplay
        pygame.quit()

if __name__ == "__main__":
    game = Tetris()
    game.run()
