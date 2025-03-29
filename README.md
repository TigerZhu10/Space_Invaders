# Space_Invaders

## Project Overview:
The game *Space Invader* is created using Pygame and is based on the original *Space Invaders* game developed by Tomohiro Nishikado in 1978 in Japan. The goal of the game is to eliminate all the aliens and achieve the highest possible score using a limited number of bullets. Players have 3 lives. After completing one wave of aliens, the game's speed increases, making it more challenging. A life is lost if an alien hits the player's ship or reaches the bottom of the screen. When all 3 lives are lost, the game ends. At that point, the player can choose to restart or exit the game.

<div style = "text-align: center;">
    <img src="./assets/readme/game_photo.png" width = 80%  height: auto>
</div>

## Coding Enviroment:
- **IDE**: VsCode
- **Language**: Python
- **Module**: Pygame
- **Running command**: 

```
python .\main.py
```
## Project Features:
- Score system: 

## File Structure:
```css
📁 assets/
├── images/
│   ├── alien.png
│   └── player_ship.png
└── sounds/
│   ├── new_round.wav
│   ├── alien_fire.wav
│   ├── player_hit.wav
│   └── alien_hit.wav
└── readme/
    ├── game_photo.png

📄 main.py
📄 settings.py
📄 ship.py
📄 alien.py
📄 bullet.py
📄 score.py
📄 round.py
📄 lives.py
📄 button.py
📄 sound.py
📄 game_functions.py
```
