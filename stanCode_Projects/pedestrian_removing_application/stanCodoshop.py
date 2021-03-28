"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: This program will produce a new photo removing people or object that appear only a few times
    in different positions in the similar images given by performing tasks as follow:
    1. Average the RGB of pixels of given images.
    2. Calculate the deviation(RGB difference), or so called distance, with the averaged RGB.
    3. Pick the pixels as the best pixels, which has the shortest distance, and pass it to the blank Image created.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    ans = ((pixel.red-red)**2 + (pixel.green-green)**2 + (pixel.blue-blue)**2) ** (1/2)
    return ans


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0
    green = 0
    blue = 0
    length = len(pixels)
    for pixel in pixels:
        red += pixel.red
        green += pixel.green
        blue += pixel.blue
    return [red//length, green//length, blue//length]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    dists = []
    for pixel in pixels:
        avg = get_average(pixels)
        avg_r = avg[0]
        avg_g = avg[1]
        avg_b = avg[2]
        dist = get_pixel_dist(pixel, avg_r, avg_g, avg_b)
        dists.append(dist)
    min_dist = min(dists)
    min_index = dists.index(min_dist)
    best = pixels[min_index]
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            lst = []
            for img in images:
                pixel = img.get_pixel(x, y)
                lst.append(pixel)
            best = get_best_pixel(lst)
            result_p = result.get_pixel(x, y)
            result_p.red = best.red
            result_p.green = best.green
            result_p.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images('hoover')
    solve(images)


if __name__ == '__main__':
    main()
