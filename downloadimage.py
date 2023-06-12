import urllib
import urllib.request
from PIL import Image
import requests

# file_name = "images_over_100_kb - images_over_100_kb.csv"


def download_images(file_name, num):
    with open("{0}".format(file_name), 'r') as csvfile:
        # iterate on all lines

        i = 0
        for line in csvfile:
            # splitted_line = line.split(',')
            # check if we have an image URL
            if line != '' and line != "\n":
                urllib.request.urlretrieve(line, f"images_jpgs/image{str(i)}.jpg")
                print("Image saved for {0}".format(line))
                i += 1
                num = i
                print(num)
            else:
                print("No result for {0}".format(line))



# img_url = 'https://teammax.uk.com/wp-content/uploads/2019/12/cover-1-1-1024x576.jpg'
# file_name = "images_over_100_kb - images_over_100_kb.csv"
#
#
# with open("{0}".format(file_name), 'r') as csvfile:
#
#     i = 0
#     for line in csvfile:
#
#         if line != '' and line != "\n":
#
#             img = Image.open(requests.get(line, stream=True).raw)
#             img.save(f'images_jpgs/image-{i}.jpg')
#             print("Image saved for {0}".format(line))
#         else:
#             print("No result for {0}".format(line))
#
#         i += 1
