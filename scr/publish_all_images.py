import argparse
import os
import random
import time
from dotenv import load_dotenv
from telegram_bot import publish_user_image_to_channel


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Publishing all images from folder to telegram channel (For exit press ctr+C)")
    parser.add_argument("delay", nargs="?", type=int, default=3600,
                        help="Set time interval for images to be published (default = 3600 sec(4 hours))")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    tg_channel = "@spacechannel1906"
    path_to_img = os.getcwd() + "/Images"
    img_list = os.listdir(path_to_img)
    args = get_arguments()
    while True:
        for image_number, image in enumerate(img_list):
            if image_number == len(img_list) - 1:
                random.shuffle(img_list)
                break
            else:
                publish_user_image_to_channel(tg_channel, f"{path_to_img}/{image}", token)
                time.sleep(args.delay)
