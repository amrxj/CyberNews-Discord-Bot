# CyberNewsBot - Discord Bot for Cybersecurity News

## Overview

**CyberNewsBot** is a personal project that fetches and shares trending cybersecurity news every 24 hours on Discord. As a student passionate about cybersecurity, I created this bot to keep myself updated on the latest events in the cybersecurity world. The bot retrieves posts from Reddit and shares them in a designated Discord channel with clickable links to each article.

I plan to host the bot on the cloud and make it available for other servers, allowing others to stay informed about cybersecurity trends.

## Features

- **Fetches Cybersecurity News**: Automatically retrieves the latest cybersecurity news from Reddit every 24 hours.
- **Embeds in Discord**: News posts are sent as rich embeds with clickable links to the articles.
- **Customizable**: Fetch posts from specific subreddits, change fetch intervals, and target specific Discord channels.
- **Personal Use & Future Deployment**: Initially for personal use, but will be deployed on the cloud and available for other Discord servers.

## Installation

### Prerequisites

1. **Python 3.12+**: Ensure Python 3.12 or higher is installed.
2. **Discord Bot Token**: Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications) to get your bot's token.
3. **Reddit API Access**: Use `praw` to fetch posts from Reddit. Set up API access if necessary.

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CyberNewsBot.git
   cd CyberNewsBot
   ```
2. create a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. install the required dependencies
   ```bash
   pip install praw
   pip install discord.py
   ```
4. since this is locally hosted, configure the bot by:
   ```
   - Add your Discord bot token to the code (in CyberNewsBot.py).
   - Update CHANNEL_ID to the Discord channel where you want the news to be posted.
   - Set FETCH_INTERVAL to 86400 for 24-hour intervals (change as needed).
   ```
6. run the bot
   ```bash
   python CyberNewsBot.py
   ```
   


