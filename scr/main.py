import requests
import os
from dotenv import load_dotenv
from urllib import parse
import datetime


def get_img_extension(url):
    img_extension = os.path.splitext(parse.urlsplit(url, allow_fragments=True)[2])[-1]
    return img_extension


def save_img(url, img_dir):
    response = requests.get(url)
    response.raise_for_status()
    with open(img_dir, "wb") as image:
        image.write(response.content)


def fetch_spacex_last_launch(img_dir):
    response = requests.get("https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a")
    response.raise_for_status()
    img_urls = response.json()["links"]["flickr"]["original"]
    for url_number, url in enumerate(img_urls):
        save_img(url, f"{img_dir}/spacex_{url_number}{get_img_extension(url)}")


def fetch_nasa_apod_images(img_dir, token):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": token,
               "count": 5}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for dictionary_number, dictionary in enumerate(response.json()):
        if dictionary["media_type"] == "image":
            img_url = dictionary["url"]
            save_img(img_url,
                     f"{img_dir}/nasa_apod_{dictionary_number}{get_img_extension(img_url)}")


def fetch_nasa_epic_images(img_dir, token):
    url = f"https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for dictionary_number, dictionary in enumerate(response.json()):
        img_name = dictionary["image"] + ".png"
        date = datetime.datetime.strptime(dictionary["date"], "%Y-%m-%d %H:%M:%S").date()
        formatted_date = date.strftime("%Y/%m/%d")
        img_url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{img_name}?api_key={token}"
        save_img(img_url, f"{img_dir}/epic_{dictionary_number}.png")


def create_img_dir(img_dir):
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)


def main():
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    img_dir = "/Users/sergeiperevera/PycharmProjects/Study/Space_Telegram/images"
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

    create_img_dir(img_dir)
    save_img(url, f"{img_dir}/Hubble{get_img_extension(url)}")
    fetch_spacex_last_launch(img_dir)
    fetch_nasa_apod_images(img_dir, token)
    fetch_nasa_epic_images(img_dir, token)


if __name__ == "__main__":
    main()
