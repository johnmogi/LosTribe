# Lost Tribe Game

A browser-based Pygame game using Pygbag for WebAssembly compilation.

## Development Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the game locally with Pygbag:
```bash
python -m pygbag main.py
```

3. Open your browser and navigate to `http://localhost:8000`

## Building for Production

To build the game for web deployment:
```bash
python -m pygbag --build main.py
```

The built files will be in the `build/web` directory.

## Resource Management

The game implements dynamic resource loading to stay under the 10MB limit:
- Resources are loaded on demand when entering new game sections
- Previous resources are unloaded when no longer needed
- Textures and audio are compressed appropriately for web delivery
# LosTribe
