import argparse
import os
import requests
from dotenv import load_dotenv
from save_images_to_dir import create_img_dir
from save_images_to_dir import save_img
from save_images_to_dir import get_img_extension


def fetch_nasa_apod_images(img_dir, count, token):
    create_img_dir(img_dir)
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": token,
               "count": count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for dictionary_number, dictionary in enumerate(response.json()):
        if dictionary["media_type"] == "image":
            img_url = dictionary["url"]
            save_img(img_url,
                     f"{img_dir}/nasa_apod_{dictionary_number}{get_img_extension(img_url)}")


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Download image of the day from https://apod.nasa.gov/apod/astropix.html")
    parser.add_argument("--count", default=1, help="You can specify how many images you want (dafault = 1)")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    img_dir = os.getcwd() + "/Images"
    args = get_arguments()
    fetch_nasa_apod_images(img_dir, args.count, token)
