import cv2 as cv
import numpy as np
from PIL import Image
import math


def pullred(image):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Because of the way HSV wraps around on red, we need to make two masks and merge them.
    range_low1 = np.array([0, 70, 50])
    range_high1 = np.array([10, 255, 255])
    range_low2 = np.array([170, 70, 50])
    range_high2 = np.array([180, 255, 255])

    # With ranges sorted, we make the two masks here:
    mask1 = cv.inRange(hsv_image, range_low1, range_high1)
    mask2 = cv.inRange(hsv_image, range_low2, range_high2)

    # Return the result of two merged masks
    return cv.add(mask2, mask1)


def pullblue(image):
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Getting the range for acceptable blue values
    range_low = np.array([110, 50, 50])
    range_high = np.array([130, 255, 255])

    return cv.inRange(hsv_image, range_low, range_high)


def finddirection(img):
    # We have an image that's black where there's no red, and white where there is.
    # So-- we pick out the edges that have masking (with a bit of a buffer for safety),
    # and figure out if we're looking at a straight or turning line. Context tells us
    # what that line means (A horizontal line means to go left or go right, if we're 
    # going right then that's what it means).

    # Dimensions of the shape we're looking at
    height, width = img.shape[:2]
    centerx = math.floor(width/2)
    centery = math.floor(height/2)
    top_pos = [centerx, height - 1]
    right_pos = [width - 1, centery]
    bottom_pos = [centerx, 1]
    left_pos = [1, centery]

    #TODO: For the sake of safety, it makes more sense to turn these into a range.
    # Fine for testing on simple images where everything's already centered, though.
    right = True if img[centerx, height-1] == 255 else False
    bottom = True if img[width - 1, centery] == 255 else False
    left = True if img[centerx, 1] == 255 else False
    top = True if img[1, centery] == 255 else False

    if left and right:
        print("--")
    elif top and bottom:
        print("|")
    elif top and right:
        print("|_")
    elif top and left:
        print("_|")
    elif bottom and right:
        print(" _")
        print("| ")
    elif bottom and left:
        print("_ ")
        print(" |")
    print("")


def drawcorners(image):
    corners = cv.goodFeaturesToTrack(image, 4, .01, 10)
    if corners is not None:
        corners = np.int0(corners)
    else:
        return image, -1, -1, -1, -1

    maxx = 0
    maxy = 0
    miny, minx = image.shape[:2]

    for corner in corners:
        x,y = corner.ravel()
        maxx = x if x >= maxx else maxx
        minx = x if x <= minx else minx
    
        miny = y if y <= miny else miny
        maxy = y if y >= maxy else maxy

        cv.circle(image, (x, y), 10, 100, -1)
    
    cv.circle(image, (minx, miny), 10, 255, -1)
    cv.circle(image, (maxx, maxy), 10, 255, -1)

    #print(minx, maxx, miny, maxy)
    return image, minx, miny, maxx, maxy
