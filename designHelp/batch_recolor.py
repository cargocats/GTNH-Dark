import numpy as np
import os
from PIL import Image

def replace_color(image, color_mappings):
    data = image.load()

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            r, g, b, a = data[x, y]

            for target_color, replacement_color in color_mappings.items():
                if (r == target_color[0] and g == target_color[1] and b == target_color[2] and a == 255):
                    data[x, y] = replacement_color

    return image

def batch_recolor(directory, output_directory, color_mappings):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            image_path = os.path.join(directory, filename)
            image = Image.open(image_path)

            print(filename)

            recolored_image = replace_color(image, color_mappings)

            output_path = os.path.join(output_directory, filename)
            recolored_image.save(output_path)

            print(f"Processed {filename} and saved to {output_path}")

input_directory = "avaritia/textures/gui"

output_directory = "./output"
color_mappings = {
    (24, 32, 37): (79, 79, 79, 255),
    (27, 40, 47): (102, 102, 102, 255),
    (19, 22, 23): (34, 34, 34, 255),

    (35, 53, 62): (102, 102, 102, 255),
    (31, 43, 49): (79, 79, 79, 255),
    (24, 29, 30): (34, 34, 34, 255),

    (21, 25, 27): (56, 56, 56, 255)
}

batch_recolor("../assets/" + input_directory, output_directory, color_mappings)