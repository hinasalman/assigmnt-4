
## Overview

Humo is a simple Discord bot built with Python using the discord.py library. This bot provides basic interaction capabilities through commands and can be extended to create a more feature-rich Discord server experience.

## Purpose

The bot was created to:

- Demonstrate how to build a Discord bot using Python
- Provide a foundation that can be expanded with more advanced features
- Offer simple utility commands for Discord server members
- Serve as a learning tool for Python and Discord API integration

## Features

### Current Commands

- `!ping` - Checks if the bot is responsive (returns "Pong! 🎣")
- `!hello` - Greets the user who sent the command
- `!echo [message]` - Repeats whatever message the user sends after the command

### Technical Implementation

- Built with discord.py library
- Uses environment variables for secure token storage
- Implements Discord's Intents system for message content access
- Provides basic command handling through discord.ext.commands

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Discord account and a registered application/bot
- Required Python packages (see requirements.txt)

### Installation Steps

1. Clone or download the bot code
2. Install required dependencies:

```plaintext
pip install -r requirements.txt
```

3. Create a `.env` file with your Discord bot token:

```plaintext
DISCORD_TOKEN=your_token_here
```

4. Enable privileged intents in the Discord Developer Portal:

1. Go to [https://discord.com/developers/applications/](https://discord.com/developers/applications/)
2. Select your application
3. Go to the "Bot" tab
4. Enable "MESSAGE CONTENT INTENT"

5. Run the bot:

```plaintext
python app.py
```

## Use Cases

### Educational

- Learning Python programming
- Understanding API integrations
- Exploring Discord bot development

### Community Management

- Basic server interaction
- Foundation for moderation tools
- User engagement through simple commands

### Entertainment

- Simple games and interactions
- Custom responses to user messages
- Server-specific functionality

## Extending the Bot

The current implementation is minimal but can be extended with:

- Moderation commands (kick, ban, timeout)
- Music playback features
- Server management tools
- Custom reaction roles
- Games and entertainment features
- API integrations with external services

## Security Notes

- Never share your bot token publicly
- Use environment variables for sensitive information
- Regularly update dependencies for security patches
- Implement proper permission checks for administrative commands

## Technical Details

- **Language**: Python
- **Main Library**: discord.py
- **Environment Management**: python-dotenv
- **Required Intents**: message_content (privileged)
