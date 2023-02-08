import argparse
import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from save_images_to_dir import create_img_dir
from save_images_to_dir import save_img


def fetch_nasa_epic_images(img_dir, token):
    create_img_dir(img_dir)
    url = f"https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for dictionary_number, dictionary in enumerate(response.json()):
        img_name = dictionary["image"] + ".png"
        date = datetime.strptime(dictionary["date"], "%Y-%m-%d %H:%M:%S").date()
        formatted_date = date.strftime("%Y/%m/%d")
        img_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{img_name}?api_key={token}"
        save_img(img_url, f"{img_dir}/epic_{dictionary_number}.png")


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    img_dir = os.getcwd() + "/Images"
    parser = argparse.ArgumentParser(
        description="Downloads images of the Earth from https://api.nasa.gov/EPIC/archive/")
    fetch_nasa_epic_images(img_dir, token)
