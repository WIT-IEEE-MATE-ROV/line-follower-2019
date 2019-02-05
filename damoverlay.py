import cv2 as cv
import numpy as np
import sys

x = sys.argv[1]			#int x position
y = sys.argv[2]			#int y position
o = sys.argv[3]			#str orientation
l = sys.argv[4]			#float crack length

x = int(x)
y = int(y)

unit = 300					#px
grid_color = (0, 0, 0)
line_thickness = 3			#px
font = cv.FONT_HERSHEY_PLAIN
fontsize = 10

xpos = unit * x
ypos = unit * y
xbuff = unit / 5
ybuff = unit / 2
c = (255,0,0)

img = np.ones((3 * unit, 4 * unit, 3), np.uint8)
img[:,0:unit * 4] = (255,255,255)

cv.line(img, (0, 0), (4 * unit, 0), grid_color, line_thickness)
cv.line(img, (0, unit), (4 * unit, unit), grid_color, line_thickness)
cv.line(img, (0, 2 * unit), (4 * unit, 2 * unit), grid_color, line_thickness)
cv.line(img, (0, 3 * unit), (4 * unit, 3 * unit), grid_color, line_thickness)

cv.line(img, (0, 0), (0, 3 * unit), grid_color, line_thickness)
cv.line(img, (unit, 0), (unit, 3 * unit), grid_color, line_thickness)
cv.line(img, (2 * unit, 0), (2 * unit, 3 * unit), grid_color, line_thickness)
cv.line(img, (3 * unit, 0), (3 * unit, 3 * unit), grid_color, line_thickness)
cv.line(img, (4 * unit, 0), (4 * unit, 3 * unit), grid_color, line_thickness)


if o == 'h':
	cv.line(img, (x * unit + unit / 5, y * unit + unit / 2), (x * unit + 4 * unit / 5, y * unit + unit / 2), c, line_thickness)
else:
	cv.line(img, (x * unit + unit / 2, y * unit + unit / 5), (x * unit + unit / 2, y * unit + 4 * unit / 5), c, line_thickness)

	
l = str(l)
cv.putText(img, l, (unit * x + unit / 4, unit * y + unit / 4), font, fontsize, grid_color, cv.LINE_AA)

cv.imshow('dam overlay', img)
cv.waitKey(0)
cv.destroyAllWindows()