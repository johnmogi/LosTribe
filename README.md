# **The LosTribe**  
*A 2D Low-Poly RPG Adventure*  

---

## **Table of Contents**  
1. [Overview](#overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Gameplay](#gameplay)  
5. [Controls](#controls)  
6. [Story](#story)  
7. [Development](#development)  
8. [Contributing](#contributing)  
9. [License](#license)  

---

## **Overview**  
*The LosTribe* is a 2D low-poly RPG where you play as a hero navigating a fractured, elemental world to rescue a trapped game developer. The game combines maze exploration, turn-based combat, and a rich narrative inspired by fantasy and digital chaos. Built in Python using Pygame, it’s designed to be lightweight, modular, and easy to extend.

---

## **Features**  
- **Procedural Maze Generation**: Explore a unique maze every playthrough.  
- **Elemental Combat System**: Rock-paper-scissors meets a 4-element pyramid (Fire, Air, Earth, Water).  
- **Dynamic Environments**: Biomes affect combat and exploration (e.g., forests boost fire, oceans heal water).  
- **Rich Lore**: Uncover the story of Adam Douglas, a 12-year-old game developer trapped in his own creation.  
- **Class-Based Heroes**: Choose from 4 unique classes, each with elemental affinities and abilities.  
- **Permadeath with Progression**: Restart with the same character or create a new one after death.  

---

## **Installation**  
1. **Prerequisites**:  
   - Python 3.8+  
   - Pygame (`pip install pygame`)  

2. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/yourusername/the-lostribe.git  
   cd the-lostribe  
   ```  

3. **Run the Game**:  
   ```bash  
   python main.py  
   ```  

---

## **Gameplay**  
### **Exploration**  
- Navigate a 10x10 grid maze with procedurally generated rooms.  
- Room types: Monster, Trap, Story, Treasure, Vacant.  
- Use fog of war to uncover new areas.  

### **Combat**  
- Turn-based battles with elemental dice rolls.  
- Each class has unique abilities (e.g., Fire Archers use flaming arrows).  
- Environmental effects (e.g., forests risk self-inflicted fire damage).  

### **Progression**  
- Collect loot (healing stones, magic potions, equipment).  
- Solve puzzles to unlock new areas and abilities.  

---

## **Controls**  
- **Movement**: `WASD`  
- **Interact**: `Spacebar`  
- **Combat Actions**:  
  - `1`: Attack  
  - `2`: Magic  
  - `3`: Heal  
  - `4`: Escape  
- **Menu Navigation**: Arrow keys + `Enter`  

---

## **Story**  
Adam Douglas, a 12-year-old chess prodigy, coded *The LosTribe* as an escape from his lonely reality. But when he accidentally trapped himself in the game, his mind became the prize in a war between elemental tribes and a rogue AI called the Sugar King.  

As one of Adam’s invented heroes, you must:  
- Unite the fractured realms of Erth.  
- Master the elemental pyramid system.  
- Rescue Adam before the Sugar King corrupts his mind—and the game itself.  

---

## **Development**  
### **Tech Stack**  
- **Language**: Python  
- **Library**: Pygame (graphics, input, sound)  
- **Tools**: JSON (save files), Random (maze generation)  

### **File Structure**  
```  
the-lostribe/  
├── assets/            # Images, sounds, fonts  
├── src/               # Source code  
│   ├── main.py        # Entry point  
│   ├── maze.py        # Maze generation  
│   ├── combat.py      # Combat system  
│   ├── player.py      # Player class and stats  
│   ├── enemies.py     # Enemy classes  
│   └── ui.py          # Menus and HUD  
├── README.md          # This file  
└── requirements.txt   # Dependencies  
```  

---

## **Contributing**  
We welcome contributions! Here’s how to get started:  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/YourFeature`).  
3. Commit your changes (`git commit -m 'Add some feature'`).  
4. Push to the branch (`git push origin feature/YourFeature`).  
5. Open a pull request.  

---

## **License**  
*The LosTribe* is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

---

**Enjoy the game, and may your dice rolls be ever in your favor!**