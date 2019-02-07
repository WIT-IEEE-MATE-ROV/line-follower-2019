import cv2 as cv
import numpy as np
import sys
from decimal import Decimal

x = sys.argv[1]			#int x position
y = sys.argv[2]			#int y position
o = sys.argv[3]			#str orientation
l = sys.argv[4]			#float crack length

x = int(x)
y = int(y)
l = float(l)
l = round(l, 1)
l = str(l)

unit = 300								#px
width = unit * 4
height = unit * 3
grid_color = (0, 0, 0)
line_thickness = 2						#px
font = cv.FONT_HERSHEY_PLAIN
fontsize = 3


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


xpos = unit * (x - 1)
ypos = unit * (y - 1)
xbuff = unit / 5				#buffer to space blue line
ybuff = unit / 2				#buffer to space blue line
textbuff = unit / 3				#buffer to space text
c = (255,0,0)


if o == 'h':
	cv.line(img, (int(xpos + xbuff), int(ypos + ybuff)), (int(xpos + 4 * xbuff), int(ypos + ybuff)), c, 5)
	cv.putText(img, l, (int(xpos + textbuff), int(ypos + textbuff)), font, fontsize, grid_color, 3)
else:
	cv.line(img, (int(xpos + ybuff), int(ypos + xbuff)), (int(xpos + ybuff), int(ypos + 4 * xbuff)), c, 5)
	cv.putText(img,l + ' cm', (int(xpos + xbuff), int(ypos + unit / 7)), font, fontsize, grid_color, 3)


cv.imshow('dam overlay', img)
cv.waitKey(0)
cv.destroyAllWindows()