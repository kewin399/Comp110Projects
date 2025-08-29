"""
Module: collage_creator

A program to create an Andy Warhol-style collage.

Authors:
1) Cavin Nguyen - cavinnguyen@sandiego.edu
2) Jessica Cervantes - jessicacervantes@sandiego.edu
"""

import comp110_image




def copy_to(src_img, dest_img, start_x, start_y):
    """
    Copies one image into another, start at the given starting coordinate.

    DO NOT MODIFY THIS FUNCTION!!!

    Parameters:
    src_img (type: Picture) - The picture to copy.
    dest_img (type: Picture) - The picture to copy into.
    start_x (type: int) - The column where we start copying to dest_img.
    start_y (type: int) - The row where we start copying to dest_img.
    """
    for x in range(src_img.getWidth()):
        for y in range(src_img.getHeight()):
            srcPixel = src_img.getPixel(x,y)
            dest_img.setPixel(x + start_x, y + start_y, srcPixel)

    
def unique_filter(img):
    ''' creates a copy of an image and applies a unique filter to it that enhances the original image's saturation

    parameters: img (type: Picture) the original image
    returns: img_copy (type: Picture) new copy of original image with the applied filter 
    '''
    img_copy = img.copy()
    

    for row in range(img_copy.getHeight()):
        for col in range(img_copy.getWidth()):
            copy_pix = img_copy.getPixel(col,row)
                
            if copy_pix.getRed() < 200:
                copy_pix.setRed(255)
            else:
                pass
            if copy_pix.getGreen() < 200:
                copy_pix.setGreen(255)
            else:
                pass
            if copy_pix.getBlue() < 200:
                copy_pix.setBlue(255)
            else:
                pass
    return img_copy

def convolution_filter(img, kernel):
    """
    Performs convolution on all non-border pixels in the img, using the given
    convolution kernel.

    Params:
    img (type: Picture) - The picture to modify.
    kernel (type: 2D list of int) - The kernel to apply.

    Return:
    img_copy (type: Picture) - copy of original image with applied convolution filter
    """
    img_copy = img.copy()
    for row in range(1, img_copy.getHeight()-1):
        for col in range(1, img_copy.getWidth()-1):
            copy_pix = img_copy.getPixel(col,row)
            red_sum = 0
            green_sum = 0
            blue_sum = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    copy_pix = img.getPixel(col+j,row+i)
                    # To do: Get the correct neighborhood pixel
                    red = copy_pix.getRed()
                    green = copy_pix.getGreen()
                    blue = copy_pix.getBlue()
                    # indexes start at 0 and end at 2
                    red_sum += red * kernel[i+1][j+1]
                    green_sum += green * kernel[i+1][j+1]
                    blue_sum += blue * kernel[i+1][j+1]
                    
            if red_sum < 0:
                red_sum = 0
            if green_sum < 0:
                green_sum = 0
            if blue_sum < 0:
                blue_sum = 0
            if red_sum > 255:
                red_sum = 255
            if green_sum > 255:
                green_sum = 255
            if blue_sum > 255:
                blue_sum = 255

            img_copy.setPixel(col, row, (red_sum, green_sum, blue_sum))
    
    return img_copy

def flip_filter(img):
    """ creates a copy of a given image that is flipped vertically
    Parameters: img (type: Picture) original image to base modifications 

    Return: img_copy (type: Picture) copy of original image with modifications applied
    """
    img_copy = img.copy()

    w = img_copy.getWidth()
    h = img_copy.getHeight()

    for x in range(w):
        for y in range(h // 2):
            top_pixel = img.getPixel(x, y)
            bottom_pixel = img.getPixel(x, h - y - 1)
            img_copy.setColor(x, y, bottom_pixel.getColor())
            img_copy.setColor(x, h - y - 1, top_pixel.getColor())
    
    return img_copy

def red_scale_filter(img):
    """ creates a copy of a given image that has a red filter
    parameters: img (type: Picture) the original image
    returns: img_copy (type: Picture) new copy of original image with the applied filter    """
    img_copy = img.copy()
    

    for row in range(img_copy.getHeight()):
        for col in range(img_copy.getWidth()):
            copy_pix = img_copy.getPixel(col,row)
                
            newred = copy_pix.getRed()
            newgreen = 0
            newblue = 0
            copy_pix.setRed(newred)
            copy_pix.setGreen(newgreen)
            copy_pix.setBlue(newblue)

    return img_copy

def desaturated_filter(img):
    """ creates a copy of a given image but lowers the saturation
    parameters: img (type: Picture) the original image
    returns: img_copy (type: Picture) new copy of original image with the applied filter 
    """
    img_copy = img.copy()
    for row in range(img_copy.getHeight()):
        for col in range(img_copy.getWidth()):
            copy_pix = img_copy.getPixel(col,row)
            red = copy_pix.getRed()
            green = copy_pix.getGreen()
            blue = copy_pix.getBlue()


            copy_pix.setRed(red//3)
            copy_pix.setGreen(green//3)
            copy_pix.setBlue(blue//3)
    
    return img_copy

def grayscale_filter(img):
    """ creates a copy of a given image that is in grayscale
    parameters: img (type: Picture) the original image
    returns: img_copy (type: Picture) new copy of original image with the applied filter 
    """
    img_copy = img.copy()
    for row in range(img_copy.getHeight()):
        for col in range(img_copy.getWidth()):
            pix = img_copy.getPixel(col, row)
            avg = (pix.getRed() + pix.getGreen() + pix.getBlue()) / 3
            pix.setRed(avg)
            pix.setGreen(avg)
            pix.setBlue(avg)
    
    return img_copy

def create_filtered_pics(img):
    """ creates 6 new filtered images based off a given image
    parameters: img (type: Picture) the original image
    returns: (unique, convolution, flipped, red, desaturated, grayscale) (type: tuple) tuple of 6 new images with applied filters 
    """
    unique = unique_filter(img)
    convolution = convolution_filter(img, [[0,-1,0],[-1,5,-1],[0,-1,0]])
    flipped = flip_filter(img)
    red = red_scale_filter(img)
    desaturated = desaturated_filter(img)
    grayscale = grayscale_filter(img)

    return (unique, convolution, flipped, red, desaturated, grayscale)
    

def assemble_collage(filtered_pics):
    """ creates a collage of 6 filtered images based off a given image
    parameters: filtered_pics (type: tuple) tuple of 6 filtered images
    returns: canvas (type: Picture) picture of collage of images    """
    canvas = comp110_image.Picture(filtered_pics[0].getWidth()*3, filtered_pics[0].getHeight()*2)

    for row in range(2):
        for col in range(3):
            index = row*3 + col
            if index < len(filtered_pics):

                filtpic = filtered_pics[index]
                
                copy_to(filtpic, canvas, col * filtpic.getWidth(), row * filtpic.getHeight())
    
    return canvas


def shrink(img, scale_factor):
    """ creates a scaled copy of a given image based off a given scale factor
    parameters: img (type: Picture) original image
                scale_factor (type: int) the factor used to scale the height and width of the original image to determine the height and width of the new image
    returns: smaller_img (type: Picture) a new image that is the smaller scale version of the original image
    """
    img_copy = img.copy()
    smaller_img = comp110_image.Picture(img_copy.getWidth()//scale_factor, img_copy.getHeight()//scale_factor)
    for x in range(smaller_img.getWidth()):
        for y in range(smaller_img.getHeight()):
            orig_x = x * scale_factor
            orig_y = y * scale_factor
            orig_pixel = img_copy.getPixel(orig_x, orig_y)
            smaller_img.setPixel(x, y, orig_pixel)

    return smaller_img



def get_shrink_factor(img, max_width, max_height):
    """ finds the factor that should be used to scale the original image (used in the shrink function) based on the original image's max width and max height
    parameters: img (type: Picture) original image to base scaling
                max_width (type: int) - maximum allowed width after shrinking
                max_height (type: int) - maximum allowed height after shrinking
    returns: ratio_w or ratio_h (type: int) - the scale factor based on the height or width
    """
    width = img.getWidth()
    height = img.getHeight()

    if width <= max_width and height <= max_height:
        return 1
    
    ratio_w = width/max_width
    ratio_h = height/max_height
    
    #used to round up without using round()
    if int(ratio_w) < ratio_w:
        ratio_w = int(ratio_w) + 1
    if int(ratio_h) < ratio_h:
        ratio_h = int(ratio_h) + 1

    if int(ratio_w) > int(ratio_h):
        return int(ratio_w)
    else:
        return int(ratio_h)



def main():
    """ calls the user to input the filename for an image, the filname for a collage name, and the max heigth and width of the collage
        then creates a collage of 6 filtered images based off the given image
    """
    img_name = input("Enter the name of the original image file: ")
    img = comp110_image.Picture(filename=img_name)
    collage_name = input("Enter the filename you will save the collage to: ")
    max_collage_width = int(input("Enter the maximum collage width: "))
    max_collage_height = int(input("Enter the maximum collage height: "))

  
    max_height = max_collage_height // 2
    max_width = max_collage_width // 3
   
    shrink_factor = get_shrink_factor(img, max_width, max_height)
    small_img = shrink(img, shrink_factor)
    filtered_pics = create_filtered_pics(small_img)
    collage = assemble_collage(filtered_pics)
    collage.show()

    collage.save(collage_name)

if __name__ == "__main__":
    main()
