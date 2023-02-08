import argparse
import os
import random
import time
from dotenv import load_dotenv
from telegram_bot import publish_user_image_to_channel


def get_arguments():
    parser = argparse.ArgumentParser(description="Publishing all images from folder to telegram channel")
    parser.add_argument("delay", nargs="?", type=int, default=3600,
                        help="Set time interval for images to be published (default = 3600 sec(4 hours))")
    args = parser.parse_args()
    return args


def get_shuffled_images(img_list):
    return random.shuffle(img_list)


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    tg_channel = "@spacechannel1906"
    img_dir = os.getcwd() + "/Images"
    img_list = os.listdir(img_dir)
    args = get_arguments()
    while True:
        for image_number, image in enumerate(img_list):
            if image_number == len(img_list)-1:
                get_shuffled_images(img_list)
                break
            else:
                publish_user_image_to_channel(tg_channel, f"{img_dir}/{image}", token)
                time.sleep(args.delay)

