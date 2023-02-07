import requests
import os


def save_picture(url, img_dir):
    response = requests.get(url)
    response.raise_for_status()
    with open(f"{img_dir}/test.jpg", "wb") as image:
        image.write(response.content)


def fetch_spacex_last_launch(img_dir):
    response = requests.get("https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a")
    response.raise_for_status()
    urls = response.json()["links"]["flickr"]["original"]
    for url_number, url in enumerate(urls):
        save_picture(url, f"{img_dir}/spacex_{url_number}.jpg")


def fetch_nasa_today_image(img_dir):
    url = "https://api.nasa.gov/planetary/apod"

    pass


def main():
    img_dir = "/Users/sergeiperevera/PycharmProjects/Study/Space_Telegram/images"
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)
    fetch_spacex_last_launch(img_dir)





if __name__ == "__main__":
    main()
