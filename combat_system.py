import random
from enum import Enum

class Element(Enum):
    FIRE = "🔥"
    AIR = "🌪️"
    EARTH = "🌍"
    WATER = "🌊"

class CombatSystem:
    def __init__(self):
        self.element_advantages = {
            Element.FIRE: Element.AIR,
            Element.AIR: Element.EARTH,
            Element.EARTH: Element.WATER,
            Element.WATER: Element.FIRE
        }
        
    def roll_dice(self, num_dice=3):
        """Roll elemental dice"""
        elements = list(Element)
        return [random.choice(elements) for _ in range(num_dice)]
        
    def calculate_damage(self, attacker_element, defender_element, base_damage=10):
        """Calculate damage based on elemental advantages"""
        if self.element_advantages[attacker_element] == defender_element:
            return base_damage * 2  # Super effective
        elif self.element_advantages[defender_element] == attacker_element:
            return base_damage // 2  # Not very effective
        return base_damage  # Normal damage
        
    def apply_environmental_effects(self, element, environment, damage):
        """Apply environmental modifiers to damage"""
        if environment == "FOREST" and element == Element.FIRE:
            return damage, damage * 0.1  # Return damage and self-damage
        elif environment == "CAVE" and element == Element.EARTH:
            return damage + 2, 0  # Bonus damage in caves
        elif environment == "OCEAN" and element == Element.WATER:
            return damage, -5  # Healing in water
        return damage, 0  # No environmental effects
        
    def generate_enemy(self, difficulty=1):
        """Generate an enemy with random element and stats"""
        return {
            "hp": 50 * difficulty,
            "element": random.choice(list(Element)),
            "name": f"Level {difficulty} Enemy"
        }
        
    def process_turn(self, player_element, enemy, environment="NORMAL"):
        """Process a single turn of combat"""
        # Roll dice for player
        player_rolls = self.roll_dice()
        
        # Enemy selects random element
        enemy_element = random.choice(list(Element))
        
        # Calculate base damage
        player_damage = self.calculate_damage(player_element, enemy_element)
        enemy_damage = self.calculate_damage(enemy_element, player_element)
        
        # Apply environmental effects
        player_damage, player_self_damage = self.apply_environmental_effects(
            player_element, environment, player_damage)
        enemy_damage, enemy_self_damage = self.apply_environmental_effects(
            enemy_element, environment, enemy_damage)
            
        return {
            "player_rolls": player_rolls,
            "enemy_element": enemy_element,
            "player_damage": player_damage,
            "player_self_damage": player_self_damage,
            "enemy_damage": enemy_damage,
            "enemy_self_damage": enemy_self_damage
        }
