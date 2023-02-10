import requests
import os
from urllib import parse


def get_img_extension(url):
    img_extension = os.path.splitext(parse.urlsplit(url, allow_fragments=True)[2])[-1]
    return img_extension


def save_img(url, img_dir):
    response = requests.get(url)
    response.raise_for_status()
    with open(img_dir, "wb") as image:
        image.write(response.content)
