# Space Telegram
Space Telegram is a pack of different console scripts which allows you to download images from 3 different resources:
[https://api.spacexdata.com/](https://api.spacexdata.com/), [https://api.nasa.gov/EPIC/api/natural/images](https://api.nasa.gov/EPIC/api/natural/images) and [https://api.nasa.gov/planetary/apod](https://api.nasa.gov/planetary/apod) and
publishing them in your telegram channel.

## How to install
### Pre-requests
1. Get a free API Key at [https://api.nasa.gov](https://api.nasa.gov)
2. Get a telegram [bot](https://sendpulse.com/knowledge-base/chatbot/telegram/create-telegram-chatbot) and give to bot admin rights on your telegram [channel](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)

### Installation
Python3 should be already installed

You need **3** additional libraries: python-dotenv, python-telegram-bot, requests.

To install them use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```
Place API tokens in **.env** file.

```
NASA_TOKEN=Your token
TELEGRAM_TOKEN=Your token
```

## Usage
As described above, pack of different console scripts give to you a more flexibility.
You can download images separately and publish only a specified/random image, or publish the whole directory in infinity loop.

### Scripts to fetching images
All scripts downloading images in `/scr/Images` folder if directory doesn't exist it will make one.

#### fetch_nasa_apod_images.py
Console script allows you fetching images from [NASA APOD](https://api.nasa.gov/planetary/apod) with optional argument `--count` which specifying how many images you want to download.
By default `--count` set to 1.

Example:

![](../../../Desktop/Screenshot 2023-02-09 at 17.07.41.png)
#### fetch_nasa_epic_images.py
Console script allows you fetching images from [NASA EPIC](https://api.nasa.gov/EPIC/api/natural/images). No arguments in this script.

Example:

![](../../../Desktop/Screenshot 2023-02-09 at 17.09.59.png)
#### fetch_spacex_images.py
Console script allows you fetching images from [SpaceX]( https://api.spacexdata.com/) with position argument `launch_id`.
If `launch_id` wasn't specified, script fetching images from **latest** launch.

Example:
![](../../../Desktop/Screenshot 2023-02-09 at 17.10.36.png)


### Scripts to publish images in to telegram channel
#### publish_user_image.py
Publishing user defined image to channel, if image wasn't specified than take a random picture from `/scr/Images`.

Example:

![](../../../Desktop/Screenshot 2023-02-09 at 17.23.09.png)


#### publish_all_images.py
Publishing all images from `/scr/Images` in infinity loop with positional argument time `delay`.
If all images was published than script randomly shuffle them and start publishing again.

Example:

![](../../../Desktop/Screenshot 2023-02-09 at 17.23.37.png)

### Additional files
#### save_images_to_dir.py
Contain functions to get image extension and save images in folder. 
#### telegram_bot.py
Contain telegram bot functions.

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).