import argparse
import os
import random
from dotenv import load_dotenv
from telegram_bot import publish_user_image_to_channel


def get_arguments():
    path_to_img = os.getcwd() + "/Images"
    parser = argparse.ArgumentParser(description="Publishing user defined image to telegram channel")
    parser.add_argument("img_path", nargs="?", default=f"{path_to_img}/{random.choice(os.listdir(path_to_img))}",
                        help="Path to image to be published (default = random image from Images folder)")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    tg_channel = os.getenv("TELEGRAM_CHANNEL")
    args = get_arguments()
    publish_user_image_to_channel(tg_channel, args.img_path, token)
