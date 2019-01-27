import sys
import cv2 as cv
import numpy as np
import niproclines as nl

# Read image input as listed in command line
for uin in sys.argv[1:]:
    print("Loading image: ", uin)
    img = cv.imread(uin)
    img = cv.resize(img,256,144)

    if img is not None:
        cv.imshow("Original Image", cv.pyrDown(img))
        # Load image and process it by pulling out just the red bits
        rpimg = nl.pullred(img)

        # Show red isolated image and figure out which way to go
        rpimg = cv.pyrDown(rpimg)
        cv.imshow("Red isolated image", rpimg)
        nl.finddirection(rpimg)

        # Now-- grab blue mask
        bpimg = nl.pullblue(img)
        cv.imshow("Blue isolated Image", cv.pyrDown(bpimg))
        bpimg, minx, miny, maxx, maxy = nl.drawcorners(bpimg)
        cv.imshow("Corners", cv.pyrDown(bpimg))

        # Just a quick sanity check: -1 means no corners, 0 means something wasn't processed right
        if maxx > 0:
            print(minx, miny, maxx, maxy)
            # Using the coordinates of the corners, find the actual rectangle dimensions
            diffx = maxx - minx
            diffy = maxy - miny
            small_side = diffx if diffx < diffy else diffy
            large_side = diffx if diffx > diffy else diffy

            # The rules tell us the tape width is 3/4 of an inch. So now we know the smaller
            # length is 3/4 of an inch, and we know both dimensions in pixels.
            # With this knowledge, a quick ratio gives the length of the unknown side.
            bluelength = (0.75 / small_side) * large_side
            print(bluelength, '"')
        else:
            print("Didn't find a blue section there.")

        cv.waitKey()
        cv.destroyAllWindows()

    else:
        print("Couldn't find that file-- is it there?")
