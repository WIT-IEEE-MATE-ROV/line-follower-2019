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
        pimg, minx, miny, maxx, maxy = nl.drawcorners(pimg)
        cv.imshow("Corners", cv.pyrDown(pimg))

        # From the coordinates of the corners, find the dimension of the actual rectangle
        diffx = maxx - minx
        diffy = maxy - miny
        small_side = diffx if diffx < diffy else diffy
        large_side = diffx if diffx > diffy else diffy

        print(small_side, large_side)

        # We know (thanks to the rules) that the tape width is 3/4 of an inch.
        # So, the smallest side is 3/4 and we know the pixel side-- a quick ratio tells us the length.
        bluelength = (0.75 / small_side) * large_side
        print(bluelength)

        cv.waitKey()
        cv.destroyAllWindows()

    else:
        print("Couldn't find that file-- is it there?")
