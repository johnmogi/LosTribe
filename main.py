import pygame
import random
import asyncio
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

class Element(Enum):
    FIRE = "F"  # Simplified from emoji for web compatibility
    AIR = "A"
    EARTH = "E"
    WATER = "W"

class GameState:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The LosTribe")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 36)  # Using system font instead of None
        self.state = "TITLE"
        self.player = {
            "hp": 100,
            "mp": 100,
            "x": 0,
            "y": 0,
            "element": Element.FIRE
        }
        self.maze = self.generate_maze()
        
    def generate_maze(self, size=10):
        maze = [[{"type": "empty", "visited": False} for _ in range(size)] for _ in range(size)]
        maze[0][0]["type"] = "start"
        maze[size-1][size-1]["type"] = "end"
        room_types = ["monster", "treasure", "story"]
        for i in range(size):
            for j in range(size):
                if maze[i][j]["type"] == "empty":
                    maze[i][j]["type"] = random.choice(room_types)
        return maze

    def draw_title_screen(self):
        self.screen.fill(BLACK)
        title = self.font.render("The LosTribe", True, WHITE)
        subtitle = self.font.render("Press SPACE to Start", True, GRAY)
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, SCREEN_HEIGHT//3))
        self.screen.blit(subtitle, (SCREEN_WIDTH//2 - subtitle.get_width()//2, SCREEN_HEIGHT//2))

    def draw_maze(self):
        self.screen.fill(BLACK)
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                color = GRAY
                if self.maze[y][x]["type"] == "monster":
                    color = RED
                elif self.maze[y][x]["type"] == "treasure":
                    color = YELLOW
                elif self.maze[y][x]["type"] == "story":
                    color = BLUE
                
                rect = pygame.Rect(
                    x * TILE_SIZE + SCREEN_WIDTH//4,
                    y * TILE_SIZE + SCREEN_HEIGHT//4,
                    TILE_SIZE-2,
                    TILE_SIZE-2
                )
                pygame.draw.rect(self.screen, color, rect)
                
                if x == self.player["x"] and y == self.player["y"]:
                    player_rect = pygame.Rect(
                        x * TILE_SIZE + SCREEN_WIDTH//4 + TILE_SIZE//4,
                        y * TILE_SIZE + SCREEN_HEIGHT//4 + TILE_SIZE//4,
                        TILE_SIZE//2,
                        TILE_SIZE//2
                    )
                    pygame.draw.rect(self.screen, GREEN, player_rect)

        # Draw UI
        hp_text = self.font.render(f"HP: {self.player['hp']}", True, WHITE)
        mp_text = self.font.render(f"MP: {self.player['mp']}", True, WHITE)
        element_text = self.font.render(f"Element: {self.player['element'].value}", True, WHITE)
        self.screen.blit(hp_text, (10, 10))
        self.screen.blit(mp_text, (10, 50))
        self.screen.blit(element_text, (10, 90))

    async def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.state == "TITLE" and event.key == pygame.K_SPACE:
                    self.state = "GAME"
                elif self.state == "GAME":
                    if event.key == pygame.K_w and self.player["y"] > 0:
                        self.player["y"] -= 1
                    elif event.key == pygame.K_s and self.player["y"] < len(self.maze) - 1:
                        self.player["y"] += 1
                    elif event.key == pygame.K_a and self.player["x"] > 0:
                        self.player["x"] -= 1
                    elif event.key == pygame.K_d and self.player["x"] < len(self.maze[0]) - 1:
                        self.player["x"] += 1
                    
                    current_room = self.maze[self.player["y"]][self.player["x"]]
                    if current_room["type"] == "monster":
                        print("Battle!")
                    elif current_room["type"] == "treasure":
                        print("Found treasure!")
                    elif current_room["type"] == "story":
                        print("Story event!")
        return True

    async def game_loop(self):
        running = True
        while running:
            running = await self.handle_input()
            
            if self.state == "TITLE":
                self.draw_title_screen()
            elif self.state == "GAME":
                self.draw_maze()
            
            pygame.display.flip()
            await asyncio.sleep(0)  # Required for web compatibility
            self.clock.tick(60)

async def main():
    game = GameState()
    await game.game_loop()
    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())
