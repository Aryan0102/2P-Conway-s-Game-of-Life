# Conway's Game of Life

## Description

This project is a grid-based game simulation involving two players. The grid is represented as a dictionary, with each cell having values that indicate different states, such as `0` for empty, `1` for player 1, and `2` for player 2. The game includes functions for creating a blank grid, advancing generations, checking game rules, and allowing players to interact with the grid by making moves.

### Key Features

- **Interactive Grid**: Players can destroy and add cells based on rules.
- **Generational Advancement**: The game advances through generations where the state of the grid evolves based on neighboring cells.
- **Pattern Loader**: Load preset patterns onto the grid.
- **Turn-based Gameplay**: Each player takes turns destroying and adding cells.
  
## Tech Stack

- **Python 3.x**
- Uses basic libraries like `time` and `copy`.

## Gameplay

- The game starts with an empty grid.
- Players take turns destroying and adding cells.
- The game advances through generations according to a set of rules based on neighboring cells.
  
## Pattern Loader

The game allows loading a predefined pattern of cells to jump-start the gameplay. Patterns are stored in `.txt` files and can be loaded onto the grid.

Example pattern file:

```txt
[1, 2]
[2, 3]
