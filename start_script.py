from aws_studio import * 
from start_chrome import start
import random
from time import sleep
import subprocess
from xdotool_commands import * 
import subprocess
import os
import argparse
from argparse import ArgumentError
from titles_db import titles 
# from titles_db_sandeep import titles 



# from ytdeb.main import yt_engine
from ytdeb_content.main import yt_engine


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--acc",
        dest="acc",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-z",
        "--slot",
        dest="slot",
        type=str,
        required=True,
    ) 
    
    # parser.add_argument(
    #     "-y",
    #     "--target_url",
    #     dest="target_url",
    #     type=str,
    #     required=True,
    # ) 

    parser.add_argument(
        "-a",
        "--type_content",
        dest="type_content",
        type=str,
        required=True,
    ) 
    return parser


def set_slot():
    with open("/home/circleci/project/res.txt", 'r') as f:
        text = f.read()


    _slot = text

    _valid_slots = ["day_A", "night_A", "day_B","night_B", "day_C", "night_C"]

    if _valid_slots.index(_slot) == len(_valid_slots) -1:
        _slot = "day_A"
    else:
        _slot = _valid_slots[_valid_slots.index(_slot) + 1]


    _format = f"{_slot}"
    with open("/home/circleci/project/res.txt", 'w') as f:
        f.write(_format)


def setup_chrome_acc(_acc):
    # _lor = os.environ["target_url"]
    _targetxio = f"https://github.com/abhiprojectz/ytdeb/releases/download/v1/chrome_data_G.zip" 
    print(_targetxio)

    subprocess.run(f"sudo wget --directory-prefix=/home/circleci/project/ {_targetxio}", shell=True)
    sleep(2)
    subprocess.run(f"unzip -q /home/circleci/project/chrome_data_{_acc}.zip -d /home/circleci/project/", shell=True)
    sleep(2)

    # initial start
    start()
    sleep(10)
    subprocess.run("sudo killall chrome", shell=True)
    sleep(3)

    subprocess.run("sudo rm -r /root/.config/google-chrome/Default", shell=True)
    sleep(3)
    subprocess.run("sudo mv /home/circleci/project/root/.config/google-chrome/Default /root/.config/google-chrome/", shell=True)
    sleep(3)


def upload():
    ts = titles
    parser = get_arg_parser()
    args = parser.parse_args()

    _acc = args.acc
    _slot = args.slot
    _type_content = args.type_content

    # # Setup right slot 
    # with open("/home/circleci/project/res.txt", 'r') as f:
    #     _slot = f.read()
    # _slot_time = _slot.split("_")[0]
    # _acc = _slot.split("_")[1]

    # _lor = args.target_url
    # setting up chrome data folder
    setup_chrome_acc(_acc)

    # subprocess.run("sudo rm /root/*.mp4", shell=True)


    if _slot == "day":
        # ss = ["01:00", "03:00", "06:00", "09:00", "07:00", "08:00"]
        # ss = ["05:00", "07:00"]
        ss = ["05:00"]
    else: 
        ss = ["13:00", "15:00", "18:00", "21:00", "19:00", "20:00"]


    # Imagemagick fix
    # with open(r'/etc/ImageMagick-6/policy.xml', 'r') as file:
    #     data = file.read()
    #     data = data.replace('<policy domain="path" rights="none" pattern="@*" />', "")
  
    # with open(r'/etc/ImageMagick-6/policy.xml', 'w') as file:
    #     file.write(data)
    # print("Fixed imagemagick")


    # Generate content 
    # for i in ss:
    #     yt_engine(_type_content)
    #     sleep(5)


    # Starting chrome...
    # start()

    # sleep(5)
    # scrot_()
    # close_all_popups()
    # make_chrome_default()
    # # scrot_()
    
    # for i in ss:
    #     print(f"Uploading {ss.index(i) + 1} of shorts...")
    #     tss = random.choice(ts) 
    #     _title = tss + " #shorts #trending"

    #     _time = i
    #     _date = None
    #     _item = ss.index(i)

    #     studio_main(_title, _time, _date, _item)
    #     sleep(10)
     
def main():
    # subprocess.run("sudo su -", shell=True)
    # Uploading short
    upload()

    # Updating the slot
    print("Process completed.")


if __name__ == "__main__":
    main()