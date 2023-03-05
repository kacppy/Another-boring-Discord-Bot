# Another Boring Discord Bot

This repository contains the source code of a Discord bot written in Python. 

The bot can perform a few simple actions such as sending messages (with a copy of deleted messages by all users on the server), as well as displaying memes from various APIs or simple games.

# Usage

## Instalation

1. Clone the repository to your device.
2. Install the required libraries by running the command `pip install -r requirements.txt`.
3. And add your channel id in the format `channel_id = 123456789` at lane 6.
4. And add your Discord API token in the format `dc_token = your_token` at lane 7.
5. Run the bot.py file to start the bot.

## Usage
To use the bot, you need to add it to your Discord server and run it from the command line. The bot has a few built-in commands that you can execute by sending a text message on the channel where the bot is present.

!game - Simple "Rock, Paper, Scissors" game. If a player uses that command, then the bot randomly generates a value for each player.

!memes - Randomly downloads a meme from Reddit using a GET API.

!anime - Randomly downloads an anime-related image using a POST API.

# Special Note:
The main idea for writing this bot was to obtain extended logs if a user deletes their message from the server and send it to a hidden channel.

### But hey, wasn't that in the Nextcord examples in the documentation?

Yep, but it doesn't cover the situation when a user deletes an image or an image with text in a message together.

# License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

