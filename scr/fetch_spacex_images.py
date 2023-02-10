import os
import requests
import argparse
from save_images_to_dir import save_img
from save_images_to_dir import get_img_extension


def fetch_spacex_last_launch(path_to_img, launch_id):
    os.makedirs(path_to_img, exist_ok=True)
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    img_urls = response.json()["links"]["flickr"]["original"]
    for url_number, url in enumerate(img_urls):
        save_img(url, f"{path_to_img}/spacex_{url_number}{get_img_extension(url)}")


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Downloads images from the specified launch, if launch was't specified, then downloads from the last launch ")
    parser.add_argument("launch_id", nargs="?", type=str, default="latest",
                        help="Specify the spaceX launch id (dafault = latest)")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    path_to_img = os.getcwd() + "/Images"
    args = get_arguments()
    fetch_spacex_last_launch(path_to_img, args.launch_id)
