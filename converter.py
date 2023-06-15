import os
from pathlib import Path
from PIL import Image


def convert_webp(source, count):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    working_directory = f"{desktop}\images_webp"
    if not os.path.exists(working_directory):
        os.makedirs(working_directory)

    save_path = Path("images_webp")
    f_name = os.path.basename(source.with_suffix(".webp"))
    destination = f"{working_directory}\{f_name}"

    image = Image.open(source)
    image.save(destination, format="webp")

    return destination


def run_converter(folder_path):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    working_directory = folder_path
    if not os.path.exists(working_directory):
        os.makedirs(working_directory)

    paths = Path(working_directory).glob("**/*.jpg")

    i = 0
    for path in paths:
        print(path)
        webp_path = convert_webp(path, i)
        i += 1
        print(webp_path)

    paths = Path(working_directory).glob("**/*.png")

    i = 0
    for path in paths:
        print(path)
        webp_path = convert_webp(path, i)
        i += 1
        print(webp_path)

    paths = Path(working_directory).glob("**/*.heic")

    i = 0
    for path in paths:
        print(path)
        webp_path = convert_webp(path, i)
        i += 1
        print(webp_path)


# run_converter("C:/Users/nadir/Desktop/downloaded_images")

