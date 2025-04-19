# Setting Up a Discord Server and Adding a Bot

This README provides a step-by-step guide on how I created a new Discord server, added a bot, and generated an invite link using OAuth2. This document serves as a reference for future use.

## 1. Creating a New Discord Server

1. Open the Discord application on my PC.
2. Click on the **+ (Add a Server)** button on the left sidebar.
3. Select **"Create My Own"** to start a new server from scratch.
4. Enter a name for the server (e.g., `MyBotServer`).
5. Choose a region (if needed) and click **Create**.
6. The new server is now set up and visible on the left sidebar.

## 2. Creating and Adding a Bot to the Server

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications/).
2. Click **"New Application"** and give it a name (e.g., `HumoBot`).
3. Navigate to the **"Bot"** section in the left menu.
4. Click **"Add Bot"** and confirm the action.
5. Customize bot settings:
   - Set bot name and profile picture.
   - Enable the **Message Content Intent** (for reading messages).
   - Copy the **Bot Token** and store it securely (never share it).

## 3. Generating an OAuth2 Invite Link

1. In the Discord Developer Portal, go to the **OAuth2** section.
2. Click **"URL Generator"** and select:
   - `bot` under **Scopes**.
   - Under **Bot Permissions**, select:
     - `Read Messages`
     - `Send Messages`
     - `Use Slash Commands`
     - Any other permissions required for my bot.
3. Copy the generated OAuth2 link.
4. Open the link in a web browser.
5. Select the newly created server (`MyBotServer`) from the dropdown.
6. Click **"Authorize"** and complete the captcha.

## 4. Running the Bot

1. Install necessary dependencies:

   ```sh
   pip install -r requirements.txt
   ```

2. Store the bot token securely in a `.env` file:

   ```sh
   DISCORD_TOKEN=your_bot_token_here
   ```

3. Run the bot:

   ```sh
   python app.py
   ```

4. Once the bot is online, test it in Discord by using commands like `!ping`.

## 5. Deleting a Server (If Needed)

1. Open Discord and go to **Server Settings**.
2. Scroll down to **Delete Server**.
3. Confirm deletion by entering the server name.
4. Click **Delete Server** (Requires being the server owner).

This guide serves as a quick reference to replicate the setup process in the future. 🚀
## 🎉 Bot Commands

| Command         | Description |
|---------------|-------------|
| `!ping`       | Checks if the bot is responsive. |
| `!hello`      | Greets the user. 😊 |
| `!echo [message]` | Repeats the user's message. |
| `!userinfo`   | Shows details about a user. |
| `!serverinfo` | Displays server details. |
| `!clear [number]` | Deletes the specified number of messages (requires admin permission). 🗑️ |
| `!joke`       | Sends a random joke. 😂 |
| `!roll`       | Rolls a dice (1-6). 🎲 |
| `!flip`       | Flips a coin (Heads or Tails). 🪙 |
| `!rps [rock/paper/scissors]` | Play Rock Paper Scissors with the bot! ✊📄✂️ |
| `!riddle`     | Asks a fun riddle. 🤔 |
| `!fact`       | Shares an interesting random fact. 📚 |
