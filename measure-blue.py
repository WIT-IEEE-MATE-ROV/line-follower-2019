# Simple program to test the ability to measure a blue rectangle.
# It relies on the knowledge that the tape is 3/4 of an inch (so a 
# quick ratio can determine the actual size once it's measured in pixels)
import sys
import cv2 as cv
import niproclines as nl


# Read image output as listed in command line
for uin in sys.argv[1:]:
    print("Loading image: ", uin)
    img = cv.imread(uin)

    if img is not None:
        cv.imshow("Original Image", cv.pyrDown(img))
        # Process image by pulling out just the blue bits
        pimg = nl.pullblue(img)

        # Show the blue isolated image, then get a listing of the corner-coordinates
        cv.imshow("Blue isolated Image", cv.pyrDown(pimg))
        pimg = nl.drawcorners(pimg)
        cv.imshow("Corners", cv.pyrDown(pimg))

        cv.waitKey()
        cv.destroyAllWindows()

    else:
        print("Couldn't find that file-- is it there?")
