################### IMPORTS #########################
import os                                           # Import OS for path manipulations
import praw                                         # Import PRAW for Reddit API
import configparser                                 # Import configparser to read configuration
#####################################################

################### UTILS #########################

# Function to configure Reddit with credentials
def configure_reddit():
    # Parse configuration
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.ini')
    config.read(config_path)

    # Set up Reddit client with authentication credentials
    reddit = praw.Reddit(
        check_for_async=False,
        client_id=config["REDDIT"]["client_id"],
        client_secret=config["REDDIT"]["client_secret"],
        username=config["REDDIT"]["username"],
        password=config["REDDIT"]["password"],
        user_agent=config["REDDIT"]["user_agent"]
    )
    return reddit
