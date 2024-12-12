# Bishop

Bishop is a Telegram bot designed to send queued posts from a specific subreddit directly to Telegram. Users can then approve or delete posts using simple commands.

![GitHub Repo stars](https://img.shields.io/github/stars/fen0x/Bishop?style=flat-square) 
![GitHub License](https://img.shields.io/github/license/fen0x/Bishop?style=flat-square) 

## Features

Currently, Bishop supports two main commands:

- **/appost**: approves the sent post.
- **/delrule (rule)**: deletes the post based on the specified rule.

The project is still in the alpha phase and is actively under development. As it is in its early stages, bugs or unexpected behaviors may occur. Feedback and suggestions are welcome!

## Technologies Used

- Language: **Python**
- Library Management: **Poetry**
- Libraries: Telethon, PRAW

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fen0x/Bishop.git
   cd Bishop
   ```

2. **Install dependencies:**
   Make sure you have Python and Poetry installed, then run:
   ```bash
   poetry install
   ```

3. **Configure the bot:**
   Edit `config.ini.example` file with your Telegram bot token and other necessary configurations (e.g., subreddit to monitor) and name it `config.ini`.

4. **Run the bot:**
   ```bash
   poetry run python main.py
   ```

## Contributing

Bishop is open source and free. If you want to contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request when done.

## License

This project is distributed under the MIT license. See the `LICENSE` file for more details.

---

Thank you for your interest in Bishop! We hope to continuously improve this bot with the help of the community.

