import os
from export_credentials import ExportCredentials
from internet_speed_twitter_bot import InternetSpeedTwitterBot

ExportCredentials().setup_environment()

TWITTER_EMAIL = os.environ.get('TWITTER_EMAIL')
TWITTER_PASSWORD = os.environ.get('TWITTER_PASSWORD')

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)
