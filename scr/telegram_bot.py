import telegram


def print_user_text_to_channel(channel, text, token):
    bot = telegram.Bot(token=token)
    bot.send_message(text=text, chat_id=channel)


def publish_user_image_to_channel(channel, img_path, token):
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=channel, photo=open(img_path, "rb"))
