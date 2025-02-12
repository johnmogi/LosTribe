Below is a **detailed Game Design Document (GDD)** for *The LosTribe*, structured to cover core mechanics, screens, and systems. This will serve as a blueprint for the MVP.

---

# **Game Design Document: The LosTribe**  
**Genre**: 2D Low-Poly RPG  
**Engine**: Python (Pygame recommended)  
**Target Platform**: PC (MVP)  

---

## **1. Core Game Overview**  
- **Premise**: A hero from an alternate dimension must navigate a procedurally generated maze, battling monsters, solving puzzles, and uncovering lore to escape.  
- **Unique Hook**: Elemental "Rock-Paper-Scissors" combat using a **4-element pyramid system** combined with environmental interactions.  

---

## **2. Screens & Flow**  

### **1. Loading Screen**  
- **Art**: Low-poly animation (e.g., rotating pyramid) with "JOHN MOGI Studio" text.  
- **Duration**: 3 seconds (non-skippable for MVP).  

### **2. Mockup Image (Title Screen)**  
- **Art**: Static low-poly scene with the game’s subtitle: *"The Lost Tribe: Adventure from an Alternate Dimension"*.  
- **Interaction**: Press any key to proceed.  

### **3. Options Screen**  
- **Menu Options**:  
  - **Start New Game**: Proceeds to Character Generation.  
  - **Options**:  
    - **Sound**: Toggle SFX/music volume sliders.  
    - **Controls**: Display key bindings (WASD for movement, Space/Enter for interactions).  
  - **About**: Credits and lore snippet.  
  - **Donate**: Link to a donation page.  
  - **Exit**: Close the game.  

### **4. Character Generation**  
- **Classes**:  
  1. **Fire Archer Amazon** (Ranged DPS, fire affinity).  
  2. **Wind Hammer Paladin Gypsy** (Tank, air affinity).  
  3. **Water Viking Atlantean Battlemage** (Magic DPS, water affinity).  
  4. **Babylonian Earth Shield Minotaur** (Defense/CC, earth affinity).  
- **Customization**:  
  - **Randomize**: Assign random stats/appearance.  
  - **Tweak**: Adjust stats (HP, Magic, Speed) via sliders (total points capped).  

### **5. Board Screen (Main Game)**  
- **Maze Structure**:  
  - Grid-based tiles (rooms).  
  - Procedurally generated with a start and exit.  
  - Fog of War hides unexplored tiles.  
- **Room Types**:  
  - **Monster**: Triggers combat.  
  - **Trap**: Lose HP or resources (dodge via quick-time event).  
  - **Story**: Lore snippets or hints.  
  - **Vacant**: Safe zone (restore 10% HP).  
  - **Treasure**: Loot (healing stones, equipment).  

### **6. Combat Screen**  
- **Turn-Based Combat**:  
  - **Player Stats**: HP, Magic, Healing Stones.  
  - **Actions**:  
    - **Attack**: Use elemental affinity.  
    - **Magic**: Consume MP for class-specific skills.  
    - **Heal**: Use a Healing Stone (limited inventory).  
    - **Escape**: 50% success chance (failure skips turn).  
- **Elemental Pyramid Mechanics**:  
  - **Elements**: Fire 🔥 > Air 🌪️ > Earth 🌍 > Water 🌊 > Fire (loop).  
  - **Dice Rolls**: Player rolls 3 virtual dice (4-sided, each face an element).  
  - **Combat Flow**:  
    1. Player selects 1 of 3 rolled elements.  
    2. Enemy selects a random element.  
    3. **Interaction Rules**:  
      - **Strong Element**: Deals 2x damage (e.g., Fire beats Air).  
      - **Weak Element**: Takes 2x damage (e.g., Fire vs. Water).  
      - **Neutral**: Base damage (1x).  
    4. **Environment Modifiers**:  
      - Forest 🌳: Fire attacks may self-inflict 10% damage.  
      - Cave 🕳️: Earth attacks gain +1 damage.  
      - Ocean 🌊: Water heals 5% HP.  

---

## **3. Core Mechanics**  

### **Elemental Combat System**  
- **Pyramid Hierarchy**:  
  ```  
  Fire 🔥 → Air 🌪️ → Earth 🌍 → Water 🌊 → Fire  
  ```  
- **Special Interactions**:  
  - **Steam** (Fire + Water): Deals damage over time (2 turns).  
  - **Dust Storm** (Air + Earth): Reduces enemy accuracy.  
  - **Lava** (Fire + Earth): Extra AoE damage.  

### **Progression**  
- **Loot**:  
  - **Healing Stones**: Restore 25% HP (max 3 carried).  
  - **Magic Potions**: Restore 50% MP.  
  - **Equipment**: Class-specific boosts (e.g., Fire Archers get +1 attack range).  
- **Permadeath**:  
  - On death, player can restart with the same character (stats reset) or create a new one.  

---

## **4. Technical Specifications**  
- **Python Libraries**: Pygame (graphics/input), JSON (save files).  
- **Save System**: Save character stats and maze seed on exit.  
- **UI**: Mouse + keyboard controls.  

---

## **5. Art & Sound**  
- **Style**: Low-poly 2D (use flat colors and geometric shapes).  
- **Assets Needed**:  
  - Character sprites (4 classes).  
  - Maze tilesets (forest, cave, ruins).  
  - Elemental VFX (fire, water, etc.).  
- **Sound**: Retro SFX (8-bit) for combat, footsteps, and menus.  

---

## **6. Development Timeline (MVP)**  
1. **Phase 1 (2 weeks)**: Core systems (maze generation, combat loop).  
2. **Phase 2 (1 week)**: UI and menus.  
3. **Phase 3 (1 week)**: Art/sound integration.  
4. **Phase 4 (1 week)**: Playtesting and balancing.  

---

## **7. Monetization & Future Features**  
- **Donate Button**: Optional supporter perks (cosmetic skins).  
- **Post-MVP**: Multiplayer co-op, expanded classes, quest system.  

GDD Extension: Exploration & Combat Mechanics
For "The LosTribe" MVP

I. Exploration Mechanics
1. Maze Structure & Movement
Grid System:

Maze is a 10x10 grid (adjustable for MVP balance).

Each tile represents a "room" with predefined dimensions (e.g., 800x600 pixels).

Start/Exit: Start at (0,0), exit at (9,9).

Procedural Generation:

Use a randomized Prim’s algorithm to ensure a solvable maze with one clear path.

Randomly assign room types (monster, trap, story, treasure, vacant) to non-critical-path tiles.

Movement:

WASD to move between adjacent tiles.

Fog of War: Unexplored tiles are hidden; explored tiles remain visible.

Path Clarity: Critical path tiles glow faintly (hint for players).

2. Room Exploration
When entering a new room:

Reveal Animation: Fog lifts, room type icon pulses (e.g., skull for monster).

Room Types:

Monster Room: Triggers combat (see Combat Mechanics).

Trap Room:

Types: Spikes (HP loss), Poison (DoT), Confusion (reversed controls for 3 moves).

Quick-Time Event (QTE): Press Spacebar within 1 second to dodge (60% success).

Story Room:

Displays lore text (e.g., "The Minotaur’s shield bears the mark of Babylon...").

Grants a clue about the maze (e.g., "Beware the third tile east of the lava pool").

Treasure Room:

Loot table: Healing Stone (30%), Magic Potion (20%), Class-specific gear (10%).

Vacant Room:

Restore 10% HP (non-stackable).

Safe zone (no encounters).

3. Environmental Interactions
Biomes: Each room has a biome affecting gameplay:

Biome	Effect
Forest 🌳	Fire attacks risk 10% self-damage.
Cave 🕳️	Earth attacks deal +2 damage.
Ocean 🌊	Water heals 5% HP at combat start.
Desert 🏜️	Air attacks have +25% accuracy.
Dynamic Hazards:

Lava pools (DoT if stepped on), collapsing ceilings (dodge QTE).

II. Combat Mechanics (Deep Dive)
1. Combat Flow
Initiation: Player enters a Monster Room.

Combat Screen:

Top-down view of hero vs. monster (e.g., Fire Archer vs. Rock Golem).

UI Elements: HP/MP bars, dice pool, action buttons.

Turn Phases:

Player Turn:

Roll 3 elemental dice (faces: Fire, Air, Earth, Water).

Select 1 element to attack.

Enemy Turn:

Randomly selects 1 element (weighted by biome; e.g., Cave = 40% Earth).

2. Elemental Pyramid System
Hierarchy:

Copy
Fire 🔥 > Air 🌪️ > Earth 🌍 > Water 🌊 > Fire  
Damage Multipliers:

Attacker → Defender	Fire	Air	Earth	Water
Fire	1x	2x	0.5x	0.5x
Air	0.5x	1x	2x	0.5x
Earth	0.5x	0.5x	1x	2x
Water	2x	0.5x	0.5x	1x
Special Combos:

Steam (Fire + Water): Deals 1.5x damage + 5% DoT for 2 turns.

Dust Storm (Air + Earth): Reduces enemy accuracy by 30%.

Lava (Fire + Earth): Deals 2x damage to all enemies (AoE).

3. Player Actions
Attack: Use selected element (damage based on hierarchy).

Magic: Class-specific ability (consumes MP):

Class	Magic Ability
Fire Archer Amazon	Flaming Volley: 3x fire arrows (5 MP).
Wind Hammer Paladin	Cyclone Guard: Block 50% damage (4 MP).
Water Battlemage	Tidal Wave: Push enemy back 1 turn (3 MP).
Earth Minotaur	Quake Stomp: Stun enemy for 1 turn (6 MP).
Heal: Use a Healing Stone (restores 25% HP; max 3 stones).

Escape: 50% success chance; failure skips next turn.

4. Enemy Design
Monster Types:

Rock Golem (Earth): High HP, weak to Water.

Storm Wisp (Air): Evasive, weak to Earth.

Lava Slime (Fire): Splits into smaller slimes on hit.

Aqua Phantom (Water): Heals 5% HP per turn in Ocean biomes.

AI Behavior:

Prioritize elements strong against the player’s class.

Use environment bonuses (e.g., Lava Slime self-heals in Forest).

5. Post-Combat Resolution
Victory:

Loot: 1-2 items (e.g., Healing Stone + random gear).

Progress: Unlock adjacent rooms.

Defeat:

Permadeath Option: Restart with same class (stats reset) or new character.

Recovery: If escaping with <10% HP, return to last Vacant Room.

III. Technical Implementation Notes
Dice Roll System:

Use random.randint(1,4) to simulate 4-sided dice (1=Fire, 2=Air, etc.).

Display dice results as icons in the combat UI.

Biome Detection:

Assign biome per room during maze generation (store in a 2D array).

Combat Log:

Text output at bottom of screen (e.g., "Fire 🔥 beats Air 🌪️! 12 damage!").

IV. Balancing & Testing
Player HP: Start at 100 HP (scales with class).

Enemy Tuning:

Early enemies: 30-50 HP.

Final boss (exit guardian): 150 HP + 2 elements.

Playtest Focus:

Ensure elemental combos feel impactful.

Adjust QTE timing for traps (aim for 60% success rate).