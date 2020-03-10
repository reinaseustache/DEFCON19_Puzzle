# DEFCON19_Puzzle

### Solving DEF CON Redacted Puzzle – Honors Option Report

Step 1: To solve problem, I first extracted the 35 frames from the redacted-puzzle.gif file and saved each of the frames as a PNG file.  

Step 2: Since all the frames that were extracted were black, no information can be gathered from them.  I used the putpalette method and converted each frame to RGB so that the shapes can be differentiated.  I overwrote the previously saved frames to these new frames with the reset color table.

Step 3: After inspecting some of the frames, we saw that each frame made up pieces of an octagon.  I then researched the formula for an octagon and after some trial and error with the angles was able to plot squares where the eight points for the octagon are on all the frames.  

Step 4: I then checked the background pixels for the squares and if there was at least one blue pixel that made up the shape in the image, I store a one in the array and zero otherwise.  

Step 5: After shifting the array by all the 8 positions, I then saw that the numbers were too large to correspond to a position in the flag alphabet.  So, I decided to split the bits into sections of 5 since there were 32 characters and tried again in the forward and reverse direction.  In the reverse direction, with a rotation by 3 positions I was able to retrieve the beginning of the string. 

Step 6: After again examining the frames, it seems that the squares where the 8 points were located were shifting away from the corners then again becoming in sync since rotation 2 gave me the end of the message. I split the frames into 3 sections and did some trial and error with the degree of the 8 points so that they rotate as well while iterating through the frames.  This combination was able to retrieve the full message hidden in the frames.

The final output should be: OOO{FORCES-GOVERN+TUBE+FRUIT_GROUP=FALLREMEMBER_WEATHER}
