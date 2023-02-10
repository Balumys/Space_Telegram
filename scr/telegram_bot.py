import telegram


def publish_user_image_to_channel(channel, img_path, token):
    bot = telegram.Bot(token=token)
    with open(img_path, "rb") as image:
        bot.send_photo(chat_id=channel, photo=image)
