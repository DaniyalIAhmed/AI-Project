
# Mind-Maze: A Turn-Based Tile Strategy Game

## Submitted By
- **Ahmed Abdullah** (22K-4449)  
- **Daniyal Ahmed** (22K-4601)  
- **Course**: Artificial Intelligence  
- **Instructor**: Miss Alishba Subhani  
- **Submission Date**: May 11, 2025  

---

## 1. Executive Summary

### Project Overview
Mind-Maze is a tile-based, turn-based strategy game implemented in Python with a GUI built using Tkinter. The game is designed as a competition between a human player and an AI opponent that uses the **Minimax algorithm with Alpha-Beta pruning** to make optimal decisions. The goal is to control tiles and accumulate the highest score by the end of the game.

---

## 2. Introduction

### Background
Inspired by classic grid-based games like Minesweeper and strategic bluff games, this project explores AI decision-making in a dynamic environment. Tkinter was chosen for its ease of GUI development, while Minimax provides a framework for simulating strategic foresight.

### Objectives
- Develop a tile-based strategic game using Python and Tkinter.
- Integrate an AI agent using the Minimax algorithm.
- Evaluate AI performance based on decision quality and response time.

---

## 3. Game Description

### Original Game Rules
The game concept mixes Minesweeper-like tile exploration with bluff mechanics. Players choose tiles to accumulate points, while avoiding hidden traps. The challenge lies in both strategic selection and unpredictability introduced by hidden elements.

### Innovations & Modifications
- Booster tiles offering bonuses like extra turns.
- Visual interface using Tkinter.
- AI decision-making through Minimax with heuristic evaluation.

---

## 4. AI Approach and Methodology

### AI Techniques Used
- **Minimax Algorithm** for evaluating possible future states.
- **Alpha-Beta Pruning** for performance optimization.

### Algorithm & Heuristic Design
- Heuristics evaluate: score difference, boosters, and tile control.
- AI alternates between maximizing and minimizing layers.
- Depth-limited search to balance decision quality and speed.

### AI Performance Evaluation
- **Average response time**: Under 2 seconds at depth 3.
- **Win rate**: ~60% in early testing, improving to ~90% against average human players.

---

## 5. Game Mechanics and Rules

### Modified Game Rules
- 6x6 grid of tiles.
- Players alternate claiming tiles.
- Some tiles offer **boosters** (e.g., extra turns), others are **traps** (-1 point).
- Game ends when:
  - All tiles are claimed **or**
  - A player reaches a point threshold (e.g., 20 points).

### Turn-Based Mechanics
- Each turn, a player can **select** a tile and decide whether to move to it.
- If a tile is skipped, it remains hidden, introducing **bluff elements**.

### Winning Conditions
- The player with the highest score at the end wins.

---

## 6. Implementation and Development

### Development Process
- Initial board and UI setup using Tkinter.
- Booster/trap tile logic added.
- AI logic built and integrated.
- Heuristic parameters refined through testing.

### Technologies Used
- **Language**: Python
- **Libraries**: 
  - Tkinter (GUI)
  - `random` (tile assignment)
- **Tools**: GitHub for version control

### Challenges Faced
- Balancing Minimax depth with GUI responsiveness.
- Preventing interface freezing during AI moves.
- Designing scalable heuristics for different grid sizes.
- Merging Minesweeper-style logic with bluff mechanics.

---

## 7. Team Contributions

### Ahmed Abdullah (22K-4449)
- Developed the Minimax algorithm.
- Integrated AI logic with the GUI.
- Managed state transitions and backend game logic.

### Daniyal Ahmed (22K-4601)
- Designed the grid layout and Tkinter interface.
- Handled booster and trap tile logic.
- Conducted testing and refined AI heuristics.

---

## 8. Results and Discussion

### AI Performance Summary
- **Win Rate**: ~90% against average human players.
- **Decision Time**: ~1.5–2 seconds (depth 2).
- **Effectiveness**: The AI avoids traps and prioritizes beneficial tiles effectively due to its heuristic model.

---

## 9. References

- Russell, S., & Norvig, P. (2009). *Artificial Intelligence: A Modern Approach*
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Minimax Algorithm – GeeksforGeeks](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory/)
- [Python Official Documentation](https://docs.python.org/3/)

---

## 10. Installation & Running Instructions

### Prerequisites
- Python 3.x
- Tkinter (usually bundled with Python)

### To Run the Game:

```bash
git clone https://github.com/your-repo/mind-maze.git
cd mind-maze
python main.py
```

---

## 11. Demo Video

[![Watch the demo](https://img.icons8.com/clouds/100/000000/video-playlist.png)](https://drive.google.com/file/d/1DBu_6roM8y1jmIr_PWCwL5uqfF8t1p2f/view?usp=sharing)

---

## 12. License

This project was developed as part of an academic course and is not licensed for commercial use. All rights reserved to the respective authors.
