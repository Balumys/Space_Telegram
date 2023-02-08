import telegram
from dotenv import load_dotenv
import os


def print_user_text_to_channel(channel, text, token):
    bot = telegram.Bot(token=token)
    bot.send_message(text=text, chat_id=channel)


def publish_user_image_to_channel(channel, img_path, token):
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=channel, photo=open(img_path, "rb"))


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    user_text = "Hello from Python"
    tg_channel = "@spacechannel1906"
    img_path = "/Users/sergeiperevera/PycharmProjects/Study/Space_Telegram/scr/Images/nasa_apod_7.jpg"
    print_user_text_to_channel(tg_channel, user_text, token)
    publish_user_image_to_channel(tg_channel, img_path, token)
