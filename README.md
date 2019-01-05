# line-follower
This code uses image recognition to:
- See which direction a red line is pointing
- See if there's any blue line
  - If there is, measure it and figure out how big it is in inches
 
 ## How it works
 ### Line following
 - The image is converted to HSV and converted to a red mask.
 - Using the mask, the top, bottom, left, and right are checked to see if the line goes through that respective side.
 - With the knowledge of what sides are passed through, we know where the line is going.
 Context tells us what it means: for example, a horizontal line means either 'keep going left' or 'keep going right',
 knowing if we're going right or left at the moment answers that question.
 
 ### Line measuring
 - The image is converted to HSV and made into a blue mask.
 - goodFeaturesToTrack() is used to pick out corners. If no corners are found, then there's nothing to measure and
 we're done here.
 - If corners are found, we pick out two opposing corners and find the difference between them. This produces the 
 dimension of the blue rectangle in pixels.
 - The rules tell us the width of the tape is 3/4". With this information, and the dimensions in pixels, a ratio 
 allows the length of the unknown side to be calculated.
