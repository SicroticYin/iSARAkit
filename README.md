# iSARA Telegram Bot

This is a simple Telegram bot built with [python-telegram-bot](https://python-telegram-bot.org/) and asyncio.

## Features
- Responds to `/start` command
- Easy to extend for more commands

## Requirements
- Python 3.11.9 (or compatible)
- `python-telegram-bot==20.7`
- `nest_asyncio`

## Local Setup
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python main.py
   ```

## Deployment on Render.com

Render is a cloud platform for easily deploying web services and bots.

### 1. Python Version on Render
- **Render does NOT use `runtime.txt` for Python version.**
- Instead, add a file named `.python-version` to your repo root with your desired version (e.g., `3.11.9`).
- Alternatively, set the `PYTHON_VERSION` environment variable in the Render dashboard.

### 2. Deploy Steps
1. Push your code to a GitHub/GitLab/Bitbucket repository.
2. Go to [Render.com](https://render.com/) and create a new Web Service.
3. Connect your repository and select the Python runtime.
4. (Recommended) Add a `.python-version` file with your Python version:
   ```
   3.11.9
   ```
5. Set your bot token as an environment variable (never commit secrets):
   - Key: `BOT_TOKEN`
   - Value: `<your-telegram-bot-token>`
6. Set the Start Command to:
   ```
   python main.py
   ```
7. Click Deploy.

### 3. Environment Variables
- Store sensitive data like your Telegram bot token in Render's Environment tab, not in code.

## Notes
- If you previously used `runtime.txt` (for Heroku), switch to `.python-version` for Render.
- For more, see [Render Python Version Docs](https://render.com/docs/python-version)

## License
MIT 