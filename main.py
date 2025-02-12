import pygame
import random
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 60
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

class Element(Enum):
    FIRE = "Fire"
    AIR = "Air"
    EARTH = "Earth"
    WATER = "Water"

class GameState:
    TITLE = "TITLE"
    GAME = "GAME"
    COMBAT = "COMBAT"

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("The LosTribe")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 36)
        self.small_font = pygame.font.SysFont("Arial", 24)
        self.state = GameState.TITLE
        self.player = {
            "hp": 100,
            "mp": 100,
            "x": 0,
            "y": 0,
            "element": Element.FIRE
        }
        self.maze = self.generate_maze()
        self.combat_enemy = None
        self.message = ""
        self.message_timer = 0
        
    def generate_maze(self, size=10):
        maze = [[{"type": "empty", "visited": False} for _ in range(size)] for _ in range(size)]
        maze[0][0]["type"] = "start"
        maze[size-1][size-1]["type"] = "end"
        room_types = ["monster", "treasure", "story", "empty"]
        for i in range(size):
            for j in range(size):
                if maze[i][j]["type"] == "empty":
                    maze[i][j]["type"] = random.choice(room_types)
        return maze

    def draw_title_screen(self):
        self.screen.fill(BLACK)
        title = self.font.render("The LosTribe", True, WHITE)
        subtitle = self.font.render("Press SPACE to Start", True, GRAY)
        controls = self.small_font.render("Controls: WASD to move, SPACE to interact", True, GRAY)
        
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, SCREEN_HEIGHT//3))
        self.screen.blit(subtitle, (SCREEN_WIDTH//2 - subtitle.get_width()//2, SCREEN_HEIGHT//2))
        self.screen.blit(controls, (SCREEN_WIDTH//2 - controls.get_width()//2, SCREEN_HEIGHT*2//3))

    def draw_maze(self):
        self.screen.fill(BLACK)
        
        # Draw maze grid
        for y in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                color = GRAY
                if self.maze[y][x]["type"] == "monster":
                    color = RED
                elif self.maze[y][x]["type"] == "treasure":
                    color = YELLOW
                elif self.maze[y][x]["type"] == "story":
                    color = BLUE
                elif self.maze[y][x]["type"] == "start":
                    color = GREEN
                elif self.maze[y][x]["type"] == "end":
                    color = PURPLE
                
                rect = pygame.Rect(
                    x * TILE_SIZE + SCREEN_WIDTH//4,
                    y * TILE_SIZE + SCREEN_HEIGHT//4,
                    TILE_SIZE-2,
                    TILE_SIZE-2
                )
                pygame.draw.rect(self.screen, color, rect)
                
                # Draw player
                if x == self.player["x"] and y == self.player["y"]:
                    player_rect = pygame.Rect(
                        x * TILE_SIZE + SCREEN_WIDTH//4 + TILE_SIZE//4,
                        y * TILE_SIZE + SCREEN_HEIGHT//4 + TILE_SIZE//4,
                        TILE_SIZE//2,
                        TILE_SIZE//2
                    )
                    pygame.draw.rect(self.screen, WHITE, player_rect)

        # Draw UI
        self.draw_ui()
        
        # Draw message if exists
        if self.message and self.message_timer > 0:
            msg = self.small_font.render(self.message, True, WHITE)
            self.screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, SCREEN_HEIGHT - 50))
            self.message_timer -= 1

    def draw_ui(self):
        # Draw stats
        hp_text = self.font.render(f"HP: {self.player['hp']}", True, WHITE)
        mp_text = self.font.render(f"MP: {self.player['mp']}", True, WHITE)
        element_text = self.font.render(f"Element: {self.player['element'].value}", True, WHITE)
        self.screen.blit(hp_text, (10, 10))
        self.screen.blit(mp_text, (10, 50))
        self.screen.blit(element_text, (10, 90))

    def show_message(self, text, duration=60):
        self.message = text
        self.message_timer = duration

    def handle_combat(self):
        if not self.combat_enemy:
            self.combat_enemy = {
                "hp": 50,
                "element": random.choice(list(Element))
            }
            self.show_message(f"Battle started! Enemy element: {self.combat_enemy['element'].value}")
            return

        damage = random.randint(10, 20)
        self.combat_enemy["hp"] -= damage
        self.show_message(f"You dealt {damage} damage!")
        
        if self.combat_enemy["hp"] <= 0:
            self.show_message("Enemy defeated!")
            self.state = GameState.GAME
            self.combat_enemy = None
            current_room = self.maze[self.player["y"]][self.player["x"]]
            current_room["type"] = "empty"
        else:
            player_damage = random.randint(5, 15)
            self.player["hp"] -= player_damage
            self.show_message(f"Enemy dealt {player_damage} damage!")

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.state == GameState.TITLE and event.key == pygame.K_SPACE:
                    self.state = GameState.GAME
                
                elif self.state == GameState.GAME:
                    old_x, old_y = self.player["x"], self.player["y"]
                    
                    if event.key == pygame.K_w and self.player["y"] > 0:
                        self.player["y"] -= 1
                    elif event.key == pygame.K_s and self.player["y"] < len(self.maze) - 1:
                        self.player["y"] += 1
                    elif event.key == pygame.K_a and self.player["x"] > 0:
                        self.player["x"] -= 1
                    elif event.key == pygame.K_d and self.player["x"] < len(self.maze[0]) - 1:
                        self.player["x"] += 1
                    
                    # Check room type after movement
                    if (old_x != self.player["x"] or old_y != self.player["y"]):
                        current_room = self.maze[self.player["y"]][self.player["x"]]
                        if current_room["type"] == "monster":
                            self.state = GameState.COMBAT
                        elif current_room["type"] == "treasure":
                            self.player["hp"] = min(100, self.player["hp"] + 20)
                            self.show_message("Found healing potion! +20 HP")
                            current_room["type"] = "empty"
                        elif current_room["type"] == "story":
                            self.show_message("You found a story scroll!")
                            current_room["type"] = "empty"
                        elif current_room["type"] == "end":
                            self.show_message("Congratulations! You reached the end!")
                
                elif self.state == GameState.COMBAT and event.key == pygame.K_SPACE:
                    self.handle_combat()
        
        return True

    def run(self):
        running = True
        while running:
            running = self.handle_input()
            
            if self.state == GameState.TITLE:
                self.draw_title_screen()
            elif self.state == GameState.GAME or self.state == GameState.COMBAT:
                self.draw_maze()
            
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
