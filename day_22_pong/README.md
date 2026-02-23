# Pong (Day 22)

A simple two-player Pong clone built with Python's `turtle` graphics. Includes smoother paddle movement, adjustable starting speed, dynamic bounce angles, a start screen, and a game-over condition.

## How to run
1. From this folder run: `python3 main.py`
2. Click the window to focus, then press **SPACE** to start.

## Controls
- Right paddle: **Up / Down**
- Left paddle: **W / S**
- Exit: close the window or Ctrl+C in the terminal

## Gameplay details
- Ball starts with `STARTING_SPEED` (see `main.py`) and speeds up slightly on each paddle hit, capped to stay playable.
- Bounce angle varies based on where the ball hits the paddle (edge hits deflect more).
- Paddles are clamped to the playfield and won’t drift off-screen.
- First to 10 points wins; a “GAME OVER” message appears.
- A dotted center line is drawn at startup.

## Tweaks
- **Starting speed:** adjust `STARTING_SPEED` in `main.py` (lower values are faster).
- **Paddle colors:** change `R_COLOR` and `L_COLOR` in `main.py`.
- **Win score:** update the threshold in `Scoreboard.check_winner()`.

## Project structure
- `main.py` – game loop and bindings
- `game_screen.py` – screen setup, center net, start screen, input bindings
- `paddle.py` – paddle movement and bounds
- `ball.py` – ball physics, speed, and bounces
- `scoreboard.py` – score tracking and win check
