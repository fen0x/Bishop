################### IMPORTS #########################
import os                                           # Import standard libraries for path handling
import configparser                                 # Import for reading configuration files
import asyncio                                      # Import for asynchronous programming
import random                                       # Import for generating random IDs
import string                                       # Import for string manipulations
import json                                         # Import for JSON parsing
from datetime import datetime                       # Import datetime for time handling
from telethon import TelegramClient, events         # Import TelegramClient and events from Telethon
#####################################################

################### UTILS #########################

# Configure Telegram client
def configure_telegram():
    """
    Configures and returns the Telegram client using settings from the config file.
    """
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
    config.read(config_path)

    telegram_client = TelegramClient(
        "bot_session",
        int(config["TELEGRAM"]["api_id"]),
        config["TELEGRAM"]["api_hash"]
    )
    return telegram_client


# Generate a random unique alphanumeric ID
def generate_unique_id():
    """
    Generates a random unique ID composed of uppercase letters and digits.
    Returns:
        str: Randomly generated unique ID
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


# Format timestamp into a readable string
def format_timestamp(ts):
    """
    Formats a datetime object into a string with the format 'YYYY-MM-DD HH:MM:SS'.
    
    Args:
        ts (datetime): The timestamp to format.
        
    Returns:
        str: Formatted timestamp string.
    """
    return ts.strftime("%Y-%m-%d %H:%M:%S")


# Load translations from a JSON locale file
def load_translations(locale):
    """
    Loads the appropriate translations from a JSON file based on the provided locale.
    
    Args:
        locale (str): The locale/language identifier (e.g., 'en', 'es').
    
    Returns:
        dict: A dictionary containing translations.
    Raises:
        ValueError: If the translation file is not found.
    """
    locales_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'locales')
    locale_file = os.path.join(locales_dir, f"{locale}.json")
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"Translation file for locale '{locale}' not found.")


# Handle Telegram events
async def handle_telegram_events(event, reddit, log_chat_id):
    """
    Handles Telegram events, such as commands sent by the bot's user, processing Reddit submissions,
    and logging information into the designated log chat.

    Args:
        event (Event): The event triggered by Telegram.
        reddit (praw.Reddit): Reddit client instance to perform Reddit API operations.
        log_chat_id (int): ID of the Telegram chat used for logging.
    """
    config = configparser.ConfigParser()
    config.read("config.ini")

    subreddit_name = config["SETTINGS"]["subreddit"]
    locale = config["SETTINGS"].get("locale", "en")  # Default to English if locale not specified
    translations = load_translations(locale)  # Load translations for error handling and user responses

    subreddit = reddit.subreddit(subreddit_name)  # Reference to the configured subreddit

    # Check if the event is a reply
    if event.is_reply:
        message = await event.get_reply_message()

        # Ensure the message is sent by the bot and contains expected link format
        if not message.out or "\nLink: " not in message.text:
            pass
            return

        try:
            original_post_url = message.text.split("\nLink: ")[1]  # Extract the Reddit link
        except IndexError:
            await event.respond(translations["invalid_post_url"])
            return

        try:
            submission = reddit.submission(url=original_post_url)  # Attempt to retrieve Reddit submission
        except Exception:
            await event.respond(translations["invalid_post_url"])
            return

        post_id = generate_unique_id()  # Generate a unique ID for tracking purposes

        # Handle the delete rule command
        if "/delrule" in event.raw_text:
            if " " not in event.raw_text:
                await event.respond(translations["missing_rule_number"])
                return

            rule_number = event.raw_text.split("/delrule ")[1].strip()

            # Path to rules directory
            rules_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rules')
            rule_file = os.path.join(rules_dir, f"{rule_number}.txt")

            # Check if the rule file exists
            if os.path.isfile(rule_file):
                with open(rule_file, 'r', encoding='utf-8') as f:
                    rule_content = f.read()
            else:
                await event.respond(translations["rule_not_found"].format(rule_number=rule_number))
                return

            try:
                # Remove Reddit post and log the removal
                submission.mod.remove()
                submission.reply(translations["post_removed"].format(rule_content=rule_content))

                # Send confirmation to Telegram
                await event.respond(translations["post_removed_ack"].format(rule_number=rule_number))
                await event.client.send_message(
                    log_chat_id,
                    translations["log_delrule"].format(
                        post_id=post_id,
                        title=submission.title,
                        url=submission.url,
                        rule_number=rule_number,
                        rule_content=rule_content
                    )
                )
            except Exception as e:
                await event.respond(translations["error_removing_post"].format(error=str(e)))

        # Handle the approve post command
        elif "/appost" in event.raw_text:
            try:
                submission.mod.approve()

                # Log approved post action
                await event.respond(translations["post_approved"])
                await event.client.send_message(
                    log_chat_id,
                    translations["log_appost"].format(
                        post_id=post_id,
                        title=submission.title,
                        url=submission.url
                    )
                )
            except Exception as e:
                await event.client.send_message(
                    log_chat_id,
                    translations["error_approving_post"].format(error=str(e))
                )
