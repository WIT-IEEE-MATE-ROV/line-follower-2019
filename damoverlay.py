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
width = unit * 4
height = unit * 3
grid_color = (0, 0, 0)
line_thickness = 3			#px
font = cv.FONT_HERSHEY_PLAIN
fontsize = 10


img = np.ones((height, width, 3), np.uint8)
img[:,0:width] = (255,255,255)

cv.line(img, (0, 0), (width, 0), grid_color, line_thickness)
cv.line(img, (0, unit), (width, unit), grid_color, line_thickness)
cv.line(img, (0, 2 * unit), (width, 2 * unit), grid_color, line_thickness)
cv.line(img, (0, height), (width, height), grid_color, line_thickness)

cv.line(img, (0, 0), (0, height), grid_color, line_thickness)
cv.line(img, (unit, 0), (unit, height), grid_color, line_thickness)
cv.line(img, (2 * unit, 0), (2 * unit, height), grid_color, line_thickness)
cv.line(img, (height, 0), (height, height), grid_color, line_thickness)
cv.line(img, (width, 0), (width, height), grid_color, line_thickness)


xpos = unit * x
ypos = unit * y
xbuff = unit / 5
ybuff = unit / 2
textbuff = unit / 4
c = (255,0,0)


if o == 'h':
	cv.line(img, (xpos + xbuff, ypos + ybuff), (xpos + 4 * xbuff, ypos + ybuff), c, line_thickness)
else:
	cv.line(img, (xpos + ybuff, ypos + xbuff), (xpos + ybuff, ypos + 4 * xbuff), c, line_thickness)

	
l = str(l)
cv.putText(img, l, (xpos + textbuff, ypos + textbuff), font, fontsize, grid_color, cv.LINE_AA)

cv.imshow('dam overlay', img)
cv.waitKey(0)
cv.destroyAllWindows()