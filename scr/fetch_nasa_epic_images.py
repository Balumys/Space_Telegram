import argparse
import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from save_images_to_dir import save_img


def fetch_nasa_epic_images(path_to_img, token):
    os.makedirs(path_to_img, exist_ok=True)
    url = f"https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for json_number, json in enumerate(response.json()):
        img_name = json["image"] + ".png"
        date = datetime.strptime(json["date"], "%Y-%m-%d %H:%M:%S").date()
        formatted_date = date.strftime("%Y/%m/%d")
        img_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{img_name}?api_key={token}"
        save_img(img_url, f"{path_to_img}/epic_{json_number}.png")


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    path_to_img = f"{os.getcwd()}/Images"
    parser = argparse.ArgumentParser(
        description="Downloads images of the Earth from https://api.nasa.gov/EPIC/archive/")
    args = parser.parse_args()
    fetch_nasa_epic_images(path_to_img, token)
