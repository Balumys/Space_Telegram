import telegram
from dotenv import load_dotenv
import os


def print_user_text_to_channel(text, token):
    bot = telegram.Bot(token=token)
    bot.send_message(text=text, chat_id="@spacechannel1906")


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    user_text = "Hello from Python"
    print_user_text_to_channel(user_text, token)
