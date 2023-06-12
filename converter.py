import os
from pathlib import Path
from PIL import Image


def convert_webp(source, count):
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    working_directory = f"{desktop}/images_webp"
    if not os.path.exists(working_directory):
        os.makedirs(working_directory)

    save_path = Path("images_webp")
    destination = f"{working_directory}/image_{count}.webp"

    image = Image.open(source)
    image.save(destination, format="webp")

    return destination


def run_converter():
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    working_directory = f"{desktop}/images_jpgs"
    paths = Path(working_directory).glob("**/*.jpg")
    i = 0
    for path in paths:
        webp_path = convert_webp(path, i)
        i += 1
        print(webp_path)

