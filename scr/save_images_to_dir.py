import requests
import os
from urllib import parse


def create_img_dir(img_dir):
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)


def get_img_extension(url):
    img_extension = os.path.splitext(parse.urlsplit(url, allow_fragments=True)[2])[-1]
    return img_extension


def save_img(url, img_dir):
    response = requests.get(url)
    response.raise_for_status()
    with open(img_dir, "wb") as image:
        image.write(response.content)
