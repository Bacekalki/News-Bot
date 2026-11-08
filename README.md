# 🚀 Discord News Bot

A Discord bot offering news aggregation, weather updates, user preference management, and subscription-based notifications.

## 📖 Features

- **Top News:** Fetch top news articles based on user preferences and keywords.
- **News Search:** Retrieve articles using keywords, domain, language, sorting, and page size.
- **Weather Updates:** Get current weather details for a specific city and country.
- **Preference Management:** Add or remove preferred news categories.
- **Newsletter Subscriptions:** Subscribe or unsubscribe from notifications.
- **Direct Messages:** Receive command responses directly in DMs.

## 📦 Installation

### Prerequisites

- Python 3.x
- Discord bot token
- Required dependencies listed in `requirements.txt`

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Bacekalki/News-Bot.git
   cd NewsBot
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your environment variables by creating a `.env` file:

   ```env
   DISCORD_BOT_TOKEN=your_token_here
   ```

4. Run the bot:

   ```bash
   python main.py
   ```

## 🔥 Usage

The bot supports the following commands:

| Command | Description |
|---|---|
| `get-top-news "preferences" "keywords"` | Fetch top news based on preferences and keywords. |
| `get-everything "keywords" "domain" "language" "sortBy" "pageSize"` | Retrieve articles using specified search parameters. |
| `get-weather "city" "country"` | Get current weather for a specific location. |
| `add-preference "preference"` | Add a news preference. |
| `remove-preference "preference"` | Remove a news preference. |
| `subscribe "email"` | Subscribe to the newsletter. |
| `unsubscribe` | Unsubscribe from the newsletter. |
| `help` | Display available commands. |

### Additional Notes

- Start a command with `?` to receive its output in DMs.
- Valid `sortBy` values:
  - `relevancy`
  - `popularity`
  - `publishedAt`
- Use two-letter language codes.
- Supported news preferences:
  - `business`
  - `entertainment`
  - `health`
  - `science`
  - `sports`
  - `technology`

## 🛠️ Configuration

Create a `.env` file in the project root and add your Discord bot token:

```env
DISCORD_BOT_TOKEN=your_token_here
```

## 🏗️ Project Structure

```text
NewsBot/
│
├── main.py              # Main class
├── src/                 # Main logic
├── README.md            # Documentation
└── requirements.txt     # Dependencies
```

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-branch
   ```

3. Commit your changes:

   ```bash
   git commit -m "Added new feature"
   ```

4. Push to your branch:

   ```bash
   git push origin feature-branch
   ```

5. Open a Pull Request.

## 🐛 Issues & Support

If you encounter any issues, please open an issue in the repository.

## 📜 License

This project is licensed under the MIT License.

## 🌟 Acknowledgments

Special thanks to all contributors who helped improve this bot!
