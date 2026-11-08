🚀 Discord Bot

📖 Description

This Discord bot provides various functionalities, including fetching top news, weather updates, and managing user preferences. It also supports subscription-based notifications.

🎯 Features

Fetch top news based on user preferences and keywords

Retrieve articles based on keywords, domain, language, sorting, and page size

Get current weather details for a specific city and country

Manage your preferences (add/remove)

Subscribe or unsubscribe from our newsletter

Direct Message (DM) support for commands

📦 Installation

Prerequisites

Python 3.x installed

Discord bot token

Required dependencies (install via requirements.txt)

Steps

# Clone the repository
git clone https://github.com/yourusername/your-bot.git
cd your-bot

# Install dependencies
pip install -r requirements.txt

# Run the bot
python main.py

🔥 Usage

The bot supports the following commands:

Supported commands are:
- get-top-news "preferences" "keywords"
- get-everything "keywords" "domain" "language" "sortBy" "pageSize"
- get-weather "city" "country"
- add-preference "preference"
- remove-preference "preference"
- subscribe "email"
- unsubscribe
- help

Additional Notes:
- Put a question mark as the first character to receive the output in DMs.
- Valid sortBys: "relevancy", "popularity", "publishedAt".
- Use 2-letter codes for languages.
- Supported preferences are business, entertainment, health, science,
sports, technology

🛠️ Configuration

Create a .env file and add your bot token:

DISCORD_BOT_TOKEN=your_token_here

🏗️ Project Structure

NewsBot/
│-- main.py            # Main class
│-- src/               # Main logic
│-- README.md         # Documentation
│-- requirements.txt  # Dependencies

🤝 Contributing

Fork the repository

Create a new branch (git checkout -b feature-branch)

Commit your changes (git commit -m "Added new feature")

Push to the branch (git push origin feature-branch)

Open a Pull Request

🐛 Issues & Support

If you encounter any issues, please open an issue.

📜 License

This project is licensed under the MIT License.

🌟 Acknowledgments

Special thanks to all contributors who helped improve this bot!

