import sys
import cv2 as cv
import numpy as np
import niproclines as nl

# Read image input as listed in command line
for uin in sys.argv[1:]:
    print("Loading image: ", uin)
    img = cv.imread(uin)

    if img is not None:
        cv.imshow("Original Image", cv.pyrDown(img))
        # Load image and process it by pulling out just the red bits
        pimg = img
        pimg = nl.pullred(pimg)

        # Show red isolated image and figure out which way to go
        pimg = cv.pyrDown(pimg)
        cv.imshow("Red isolated image", pimg)
        nl.finddirection(pimg)

        cv.waitKey()
        cv.destroyAllWindows()

    else:
        print("Couldn't find that file-- is it there?")
