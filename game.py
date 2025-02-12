import arcade
import random
import math
from dataclasses import dataclass
from typing import Optional, List, Dict
from enum import Enum, auto

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "The Lost Tribe"

# Scaling constants
SPRITE_SCALING = 0.5
TILE_SCALING = 0.5

# Movement speed and physics
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.5
PLAYER_JUMP_SPEED = 12

class GameState(Enum):
    TITLE = auto()
    PLAYING = auto()
    COMBAT = auto()
    DIALOGUE = auto()
    GAME_OVER = auto()

class Element(Enum):
    FIRE = "Fire"
    AIR = "Air"
    EARTH = "Earth"
    WATER = "Water"

    def get_color(self):
        colors = {
            Element.FIRE: (255, 0, 0),      # Red
            Element.AIR: (255, 255, 255),    # White
            Element.EARTH: (139, 69, 19),    # Brown
            Element.WATER: (0, 0, 255)       # Blue
        }
        return colors[self]

@dataclass
class Character:
    x: float
    y: float
    hp: int
    max_hp: int
    element: Element
    sprite: Optional[arcade.Sprite] = None
    
    def update_position(self, dx: float, dy: float):
        if self.sprite:
            self.sprite.center_x += dx
            self.sprite.center_y += dy
            self.x = self.sprite.center_x
            self.y = self.sprite.center_y

class LostTribe(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Initialize game state
        self.game_state = GameState.TITLE
        
        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.background_list = None
        self.foreground_list = None
        self.enemy_list = None
        
        # Player sprite
        self.player = None
        self.player_character = None
        
        # Physics engine
        self.physics_engine = None
        
        # Track the current state
        self.current_element = Element.FIRE
        
        # UI elements
        self.ui_manager = None
        self.dialogue_box = None
        
        # Set background color
        arcade.set_background_color((32, 32, 32))  # Dark gray

    def setup(self):
        """Set up the game and initialize variables."""
        # Create sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.background_list = arcade.SpriteList()
        self.foreground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        
        # Create player sprite using a colored rectangle for now
        self.player = arcade.SpriteSolidColor(30, 30, arcade.color.WHITE)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player_list.append(self.player)
        
        # Create player character data
        self.player_character = Character(
            x=self.player.center_x,
            y=self.player.center_y,
            hp=100,
            max_hp=100,
            element=Element.FIRE,
            sprite=self.player
        )
        
        # Create sample level
        self.create_level()
        
        # Create physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            self.wall_list,
            gravity_constant=GRAVITY
        )

    def create_level(self):
        """Create a basic level layout."""
        # Create ground
        for x in range(0, SCREEN_WIDTH + 64, 64):
            ground = arcade.SpriteSolidColor(64, 64, arcade.color.DARK_GREEN)
            ground.center_x = x
            ground.center_y = 32
            self.wall_list.append(ground)
        
        # Create some platforms
        platforms = [
            (400, 200),
            (600, 300),
            (800, 400),
            (200, 250)
        ]
        
        for x, y in platforms:
            platform = arcade.SpriteSolidColor(128, 32, arcade.color.DARK_GREEN)
            platform.center_x = x
            platform.center_y = y
            self.wall_list.append(platform)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        
        if self.game_state == GameState.TITLE:
            self.draw_title_screen()
        else:
            # Draw all sprite lists
            self.background_list.draw()
            self.wall_list.draw()
            self.player_list.draw()
            self.enemy_list.draw()
            self.foreground_list.draw()
            
            # Draw UI elements
            self.draw_ui()

    def draw_title_screen(self):
        """Draw the title screen."""
        arcade.draw_text(
            "The Lost Tribe",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 50,
            arcade.color.WHITE,
            64,
            anchor_x="center"
        )
        arcade.draw_text(
            "Press SPACE to Start",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 - 30,
            arcade.color.WHITE,
            24,
            anchor_x="center"
        )

    def draw_ui(self):
        """Draw UI elements."""
        # Draw health bar background
        arcade.draw_lrbt_rectangle_filled(
            20, 220, SCREEN_HEIGHT - 40,
            SCREEN_HEIGHT - 20,
            arcade.color.RED
        )
        
        # Draw health bar
        health_width = 200 * (self.player_character.hp / self.player_character.max_hp)
        arcade.draw_lrbt_rectangle_filled(
            20, 20 + health_width,
            SCREEN_HEIGHT - 40,
            SCREEN_HEIGHT - 20,
            arcade.color.GREEN
        )
        
        # Draw current element
        element_color = self.current_element.get_color()
        arcade.draw_text(
            f"Element: {self.current_element.value}",
            10, SCREEN_HEIGHT - 60,
            element_color,
            18
        )

        # Draw debug information
        debug_info = [
            f"Player Position: ({self.player.center_x:.1f}, {self.player.center_y:.1f})",
            f"Player Velocity: ({self.player.change_x:.1f}, {self.player.change_y:.1f})",
            f"Can Jump: {self.physics_engine.can_jump()}",
            f"Game State: {self.game_state.name}"
        ]
        
        for i, text in enumerate(debug_info):
            arcade.draw_text(
                text,
                10, SCREEN_HEIGHT - 100 - (i * 20),
                arcade.color.YELLOW,
                12
            )

    def update(self, delta_time):
        """Movement and game logic."""
        if self.game_state == GameState.PLAYING:
            # Update physics engine
            self.physics_engine.update()
            
            # Update player character position to match sprite
            self.player_character.x = self.player.center_x
            self.player_character.y = self.player.center_y
            
            # Check for falling off the screen
            if self.player.center_y < 0:
                self.player.center_x = SCREEN_WIDTH // 2
                self.player.center_y = SCREEN_HEIGHT // 2
                self.player.change_x = 0
                self.player.change_y = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if self.game_state == GameState.TITLE:
            if key == arcade.key.SPACE:
                self.game_state = GameState.PLAYING
                self.setup()
        
        elif self.game_state == GameState.PLAYING:
            if key == arcade.key.UP or key == arcade.key.W:
                if self.physics_engine.can_jump():
                    self.player.change_y = PLAYER_JUMP_SPEED
            elif key == arcade.key.LEFT or key == arcade.key.A:
                self.player.change_x = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player.change_x = PLAYER_MOVEMENT_SPEED
            
            # Element switching
            elif key == arcade.key.KEY_1:
                self.current_element = Element.FIRE
                self.player_character.element = Element.FIRE
            elif key == arcade.key.KEY_2:
                self.current_element = Element.AIR
                self.player_character.element = Element.AIR
            elif key == arcade.key.KEY_3:
                self.current_element = Element.EARTH
                self.player_character.element = Element.EARTH
            elif key == arcade.key.KEY_4:
                self.current_element = Element.WATER
                self.player_character.element = Element.WATER

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        if key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            self.player.change_x = 0

def main():
    window = LostTribe()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
