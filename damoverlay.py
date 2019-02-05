import cv2 as cv
import numpy as np
import sys

x = sys.argv[1]			#int x position
y = sys.argv[2]			#int y position
o = sys.argv[3]			#str orientation
l = sys.argv[4]			#float crack length

x = int(x)
y = int(y)
l = str(l)

unit = 300					#px
width = unit * 4
height = unit * 3
grid_color = (0, 0, 0)
line_thickness = 3			#px
font = cv.FONT_HERSHEY_PLAIN
fontsize = 5


img = np.ones((height + unit, width + unit, 3), np.uint8)
img[:,0:width + unit] = (255,255,255)

cv.line(img, (0, 0), (width, 0), grid_color, line_thickness)
cv.line(img, (0, unit), (width, unit), grid_color, line_thickness)
cv.line(img, (0, 2 * unit), (width, 2 * unit), grid_color, line_thickness)
cv.line(img, (0, height), (width, height), grid_color, line_thickness)

cv.line(img, (0, 0), (0, height), grid_color, line_thickness)
cv.line(img, (unit, 0), (unit, height), grid_color, line_thickness)
cv.line(img, (2 * unit, 0), (2 * unit, height), grid_color, line_thickness)
cv.line(img, (height, 0), (height, height), grid_color, line_thickness)
cv.line(img, (width, 0), (width, height), grid_color, line_thickness)


xpos = unit * (x - 1)
ypos = unit * (y - 1)
xbuff = unit / 5
ybuff = unit / 2
textbuff = unit / 4
c = (255,0,0)


if o == 'h':
	cv.line(img, (int(xpos + xbuff), int(ypos + ybuff)), (int(xpos + 4 * xbuff), int(ypos + ybuff)), c, line_thickness)
	cv.putText(img, l, (int(xpos + textbuff), int(ypos + textbuff)), font, fontsize, grid_color, line_thickness)
else:
	cv.line(img, (int(xpos + ybuff), int(ypos + xbuff)), (int(xpos + ybuff), int(ypos + 4 * xbuff)), c, line_thickness)
	cv.putText(img, l, (int(xpos + textbuff), int(ypos + textbuff)), font, fontsize, grid_color, line_thickness)


cv.imshow('dam overlay', img)
cv.waitKey(0)
cv.destroyAllWindows()