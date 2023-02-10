import os
import requests
import argparse
from save_images_to_dir import save_img
from save_images_to_dir import get_img_extension


def fetch_spacex_last_launch(img_dir, launch_id):
    os.makedirs(img_dir, exist_ok=True)
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    img_urls = response.json()["links"]["flickr"]["original"]
    for url_number, url in enumerate(img_urls):
        save_img(url, f"{img_dir}/spacex_{url_number}{get_img_extension(url)}")


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Downloads images from the specified launch, if launch was't specified, then downloads from the last launch ")
    parser.add_argument("launch_id", nargs="?", type=str, default="latest",
                        help="Specify the spaceX launch id (dafault = latest)")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    img_dir = os.getcwd() + "/Images"
    args = get_arguments()
    fetch_spacex_last_launch(img_dir, args.launch_id)
