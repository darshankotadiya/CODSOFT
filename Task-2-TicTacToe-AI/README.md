🎮 Nexus-AI: Unbeatable Tic-Tac-Toe Engine (Python)
Nexus-AI is an advanced Tic-Tac-Toe game powered by the Minimax Algorithm, developed using Python. This project serves as a practical implementation of Artificial Intelligence and recursive decision-making logic.

📑 Table of Contents
Introduction

Key Features

The Minimax Algorithm

Tech Stack

Installation & Setup

📝 Introduction
While a standard Tic-Tac-Toe game involves two human players, this project pits a human user against a powerful AI engine written in Python. The AI analyzes every possible move using a game tree, ensuring it never loses, resulting in either an AI victory or a forced draw.

✨ Key Features
Unbeatable AI: Powered by the Minimax logic, making it mathematically impossible for a human to win.

Clean Interface: Built with a focus on core logic and can be integrated with UI libraries like Streamlit or Pygame.

Real-time AI Logic: Instantaneous move calculation even with deep recursive searches.

Optimized Engine: Efficiently handles the 3x3 board state evaluations.

🧠 The Minimax Algorithm
The core of this engine is the Minimax Algorithm, a recursive search method used for decision-making in zero-sum games.

Recursive Depth-First Search: The AI explores all potential future moves to evaluate the board state.

Heuristic Scoring: Wins are assigned +10, losses -10, and draws 0.

Maximizing & Minimizing: The AI acts as the "Maximizer" to get the highest score, assuming the player is the "Minimizer" playing optimally.

🛠️ Tech Stack
Language: Python 3.x

Libraries: streamlit (optional for UI)

Algorithm: Recursive Minimax

📸 Project Preview
(Note: Ensure your game screenshot is saved in your portfolio assets)

🚀 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/darshankotadiya/SocialMediaApp.git
Navigate to the project directory:

Bash
cd TASK-2-TICTACTOE-AI
Install requirements (if any):

Bash
pip install -r requirements.txt
Run the application:

Bash
python main.py
