import PIL.Image

# use this set of tuple when producing high
# resolution(pixels) ascii images. eg: width=400px
# ASCII_CHARS=("@", "#", "$", "&", "%", "<", ">",
# "[", "]", "/", ";", ":", "*", ",", ".", " ")

# use this set of tuple when producing low
# resolution(pixels) ascii image (recommended)
ASCII_CHARS = ("@", "#", "$", "&", "%", "/", ";", ":", ",", ".", " ")
# color:   darkest<-------------->lightest

# ------------------------------------------
# resizing the image according to user


def resize_image(image, new_width):
    width = image.width
    height = image.height
    img_ratio = height/width
    new_height = int((img_ratio*new_width)*2/3)
    # resizing the image
    new_image = image.resize((new_width, new_height))
    return new_image

# --------------------------------------------
# converting the new_image to grayscale using convert
# check the PIL documentation and how to use it


def grayify(image):
    grayscale_image = image.convert('L')
    return grayscale_image

# ----------------------------------------------
# converting the image grayscale value to
# their corresponding ASCII symbol


def pixels_to_ascii(image):
    pixel_value = image.getdata()
    # -----------------------
    # use the code below if youre using ascii tuple
    # intended for high pixel images else comment it
    # characters = "".join([ASCII_CHARS[pixel//17] for pixel in pixel_value])
    # -----------------------
    # use the code below if you're using ascii tuple intended
    # for low pixel images (recommended) else comment it
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixel_value])
    return characters

# -------------------------------------------------
# convert pixels to a string of ASCII characters


def main():
    # attempt to opEn image from use-input
    path = input("pathname of image : \n")
    try:
        image = PIL.Image.open(path)
    except Exception:
        print(path, "Not valid path name")

    # attempt to try to get the new width
    new_width = int(input("Enter the width of ASCII art (recommended 100): "))
    # ---------------------------------------
    # convert image to ASCII
    # resizing the image using resize_image function
    resized_image = resize_image(image, new_width)
    # grayifying the resized image
    gray_image = grayify(resized_image)
    # converting the pixels to ASCII symbols for gray_image
    new_image_data = pixels_to_ascii(gray_image)
    # ---------------------------------------
    # arranging the ascii image data in correct order aka. adding new lines
    # as the image data we got were joined using ""
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        new_image_data[i:(i+new_width)] for i in range(
            0, pixel_count, new_width))
    # ----------------------------------------
    # printing result
    print(ascii_image)

    # saving result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

# ---------------------------------------------
# executing the main function


main()
