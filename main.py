################### IMPORTS #####################################################
import asyncio                                                                  # Import asyncio for asynchronous programming
import configparser                                                             # Import configparser to read configuration settings
import praw                                                                     # Import PRAW for Reddit API interactions
from telethon import TelegramClient, events                                     # Import Telethon for Telegram bot interactions
from utils.reddit_handler import configure_reddit                               # Import function to configure Reddit
from utils.telegram_handler import configure_telegram, handle_telegram_events   # Import functions to configure Telegram and handle events
#################################################################################


###### VARIABLES ########
sent_posts = set()      # Keep track of sent posts to avoid resending messages
#########################

################### MAIN FUNCTION ###############################################

async def main():
    # Read the configuration file
    config = configparser.ConfigParser()
    config.read("config.ini")

    # Configure Reddit and Telegram clients
    reddit = configure_reddit()
    telegram_client = configure_telegram()

    # Extract target chat IDs from configuration
    target_chat_id = int(config["TELEGRAM"]["target_chat_id"])
    log_chat_id = int(config["TELEGRAM"]["log_chat_id"])

    # Set up Telegram event listener for new messages in the specified chat
    @telegram_client.on(events.NewMessage(chats=target_chat_id))
    async def handler(event):
        await handle_telegram_events(event, reddit, log_chat_id)  # Handle Telegram events

    # Get the subreddit name from configuration settings
    subreddit_name = config["SETTINGS"]["subreddit"]
    subreddit = reddit.subreddit(subreddit_name)

    print("Telegram bot is running...")  # Log status to the console
    await telegram_client.start(bot_token=config["TELEGRAM"]["bot_token"])

    # Monitor the Reddit moderation queue continuously
    while True:
        for item in subreddit.mod.modqueue(limit=None):
            if item.id not in sent_posts:  # Ensure posts are only sent once
                if isinstance(item, praw.models.Submission):  # Handle Reddit submissions
                    await telegram_client.send_message(
                        target_chat_id, f"Post in modqueue:\nTitle: {item.title}\nLink: {item.url}\n"
                    )
                elif isinstance(item, praw.models.Comment):  # Handle Reddit comments
                    await telegram_client.send_message(
                        target_chat_id, f"Comment in modqueue:\nAuthor: {item.author}\nBody: {item.body}\n"
                    )
                sent_posts.add(item.id)  # Mark the post as sent
        await asyncio.sleep(10)  # Wait to prevent overloading the Reddit API

    # Keep the Telegram client connected until it is disconnected
    await telegram_client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())  # Run the main asynchronous event loop
