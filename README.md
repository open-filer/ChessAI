# ChessAI

Welcome to my ChessAI project!

## Project Overview
This project aims to develop a chess-playing AI using Python. It is being built as part of my journey to participate in the ChessAI competition sponsored by FIDE, Google, and Kaggle.

## Progression:
1. It's been a while since I last worked in Python, so I’ve started by revisiting the basics. I’ve set up the development environment and tested the `python-chess` library to handle chess board creation and basic moves.
2. I learnt basic function such as creating a board and moving pieces [basic_fun.py](basic_fun.py) and created a skeleton game btw user (with white piece) and computer (with black piece) which displays checkmate , stalemate and draws [com_prog.py](com_prog.py).
3. [g_state_det.py](g_state_det.py) is for detemining the state of game.
4. Implementing basic evaluation for position scoring , adding positional scoring with Piece-Square tables and decting game.

### Goals:
- Develop a chess-playing AI.
- Focus on efficiency due to strict CPU and memory limitations in the competition.
  
## Installation

1. Clone this repository.
   ```bash
   git clone https://github.com/open-filer/ChessAI.git
   ```
3. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:  
      ```bash
      venv\Scripts\activate
      ```
   - On Mac:
     ```bash
     venv/bin/activate
     ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, test, and give feedback!

