<h1 align="center">Quiz for Telegram bot in Python(Aiogram)</h1>

<h2 align="center">Used Libraries</h2>
 <div align="center">
  <a href="https://www.sqlite.org/index.html" target="_blank" rel="noreferrer"> <img src="https://github.com/devicons/devicon/blob/master/icons/sqlite/sqlite-original-wordmark.svg" alt="python" width="60" height="60"/> </a>
 <!-- AIOGRAM -->
 <a href="https://docs.aiogram.dev/en/latest/index.html" target="aiogram"><img src="https://docs.aiogram.dev/en/latest/_static/logo.png" alt="aiogram" width="60" height="60"/></a>
 <!-- PYTHON -->
 <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/> </a>
 </div>

## Installation dependencies

````bash
# install package
$ pip install aiogram
````


## Running the app

```bash
# start in linux and mac
$ python3 main.py

# start in windows 
$ python main.py
```

# Bot Command Description

## Bot Name

Bot Username: `@TetroMancer_bot`  
Link to Bot: [@TetroMancer_bot](https://web.telegram.org/k/#@TetroMancer_bot)

### /start

This command starts the bot and greets the user. Upon invoking the command, the bot sends a welcome message and offers to start the game.


### /quiz

This command starts the quiz. The bot sends a message to start the quiz and provides the first question.

### Start Game

This button, displayed in the main menu, starts the quiz when the user clicks "Start Game."

### confirm_answer_{index}

Each button with this `callback_data` binds to the selected answer. `index` indicates the number of the selected answer.

### confirm_yes

Button to confirm the selected answer. After pressing, the bot checks the correctness of the answer and sends a message about whether it is correct or incorrect.

### confirm_no

Button to cancel the selection and redisplay the current question.

## Usage Example

1. Use the `/start` command to initiate the bot.
2. Click the "Start Game" button to begin the quiz.
3. Select an answer to the question.
4. Confirm your choice or cancel it using the appropriate buttons.

