# The Gambit (Flask Edition)

A polished, fully playable choice-based adventure game in Python 3 with a Flask backend and animated web frontend.

## Features

- Full branching narrative with 72 playable scenes
- Major story branches preserved:
  - study vs continue chess
  - pawn vs bishop line
  - hospital vs side hustle
  - Germany vs stay
  - sketchy vs regular flight
  - subway vs taxi
  - Frankfurt / Cologne / Munich city routes
  - chess tournament route
  - island adventure arc
  - Victor Hale rivalry
  - final chess puzzle and giant-board ending
- 22 endings total (good, bad, neutral, secret)
- Inventory and branch-flag state system
- Save/load slots (file-based under `instance/saves`)
- Path tracker + ending summary modal
- Typewriter text effect + transitions + animated background
- Responsive layout for laptop and smaller screens

## Project Structure

```text
story3/
  app.py
  requirements.txt
  README.md
  gambit/
    __init__.py          # Flask app factory + API routes
    game_engine.py       # Scene manager, conditions, effects, state transitions
    models.py            # Dataclasses for Scene / Choice / State
    story_data.py        # Full narrative graph and branching content
  templates/
    index.html           # Main single-page game UI shell
  static/
    css/
      style.css          # Visual theme, animations, responsive styles
    js/
      game.js            # Frontend scene renderer + API integration
  instance/
    saves/               # Save slot files written at runtime
```

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python3 app.py
```

4. Open:

- [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How to Play

- Click **Start Game** for a fresh run.
- Use **Continue** to resume current browser session state.
- Use **Save** to create a named slot file.
- Use **Load** to restore from a save slot.
- Use **Restart** to reset current run.
- Endings show a modal summary with your recent path.

## Architecture (Short)

- Backend is authoritative for story logic and validation.
- Frontend handles rendering, animation, text pacing, and interaction.
- Story graph is data-driven in `story_data.py` and separated from logic.
- Engine enforces branch conditions, applies effects, logs path, and computes progress.
- API endpoints provide clean game actions (`start`, `choice`, `state`, `save`, `load`, `restart`).

## Notes on Scope

- Chess interactions are scripted decision puzzles (not full chess engine).
- Ambient audio hook exists in the UI (`#ambient-audio`) and can be connected to a sound file later.
- Asset usage is intentionally minimal and code-first.

## Future Improvements

1. Add optional full chess-engine-backed tactical mini-games for selected scenes.
2. Add accessibility toggles (text speed, font size, reduced motion mode).
3. Add achievement system and branching map visualization.
4. Add autosave snapshots per chapter and multiple profile support.
5. Add optional voice-over + ambient soundtrack packs.

