from pathlib import Path
from PIL import Image


def convert_webp(source, count):
    save_path = Path("images_webp")
    destination = (f"images_webp/image_{count}.webp")

    image = Image.open(source)
    image.save(destination, format="webp")

    return destination


def run_converter():
    paths = Path("images_jpgs").glob("**/*.jpg")
    i = 0
    for path in paths:
        webp_path = convert_webp(path, i)
        i += 1
        print(webp_path)

