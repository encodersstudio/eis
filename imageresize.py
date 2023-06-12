from PIL import Image
from pandas import *

filename = "name-src"

data = read_csv("name-src.csv")

orig_name = data['name'].tolist()

data['name'] = data['name'].str.cat(data.ext)

product_name = data['name'].tolist()



# for i in product_name:
#     print(i)

for i in product_name:

    image = Image.open(i)
    new_image = image.resize((1000, 1000))
    new_image.save('resized_'+i)
    print('Image '+ i + ' resized')

