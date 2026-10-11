# Stone Paper Scissor | Player vs Bot

A simple command-line **Stone Paper Scissor** game developed using Python. Play against a computer bot that randomly selects stone, paper, or scissor in each round.

The game features score tracking, random computer choices, and a 3-round match. It is a beginner-friendly project created to practice Python fundamentals and basic game logic.

## 🎮 Features

- 👤 **Player vs Bot:** Challenge the computer in a classic game.
- 🤖 **Random Computer Choices:** The bot selects a choice using Python's `random` module.
- 🏆 **Score Tracking:** Keeps track of the player's and computer's scores.
- 🔄 **3-Round Match:** Play three rounds against the bot.
- 📊 **Live Scoreboard:** Displays the current score after each round.
- 🐍 **Simple Python Code:** Great for beginners learning programming fundamentals.

## 🛠️ Technologies Used

- **Python 3**
- `random` module
- `input()` for user interaction
- `while` loops
- `if-elif-else` conditional statements
- Variables and basic data structures

## 📋 Game Rules

The game has three possible choices:

- 🪨 **Stone** beats Scissor.
- 📄 **Paper** beats Stone.
- ✂️ **Scissor** beats Paper.

If the player and computer choose the same option, the round is a tie.

Each round winner earns one point. The player with the higher score at the end of the match wins.

## 🚀 How to Run

### 1. Install Python

Install Python 3 if it is not already installed.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/STP-Player-vs-Bot.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 3. Navigate to the Project Folder

```bash
cd STP-Player-vs-Bot
```

### 4. Run the Game

If your Python file is named `main.py`, run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## 🎯 How to Play

1. Run the Python program.
2. Enter `stone`, `paper`, or `scicor` when prompted.
3. The computer randomly chooses its move.
4. The program displays the round result and current score.
5. Repeat until all three rounds are completed.

**Important:** Enter the choices exactly as shown: `stone`, `paper`, or `scicor`.

## 📂 Project Structure

```text
STP-Player-vs-Bot/
├── main.py
└── README.md
```

## 📚 What I Learned

This project helped me practice:

- Taking input from the user.
- Generating random choices with Python.
- Using conditional statements to compare choices.
- Repeating actions with `while` loops.
- Tracking scores using variables.
- Building a simple interactive command-line game.

## 🔮 Future Improvements

- Fix round numbering to display the correct round.
- Validate user input and reject invalid choices.
- Display the final winner after all three rounds.
- Handle ties in the final score.
- Add difficulty levels for the computer bot.
- Create a graphical user interface (GUI).

## 👨‍💻 Author

Created as a beginner Python project to practice programming fundamentals and build a simple Player vs Bot game.

## 📄 License

This project is open source and can be used for learning, experimentation, and further development.
