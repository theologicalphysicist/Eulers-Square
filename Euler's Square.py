from Square import Square
import Graphics as gr
import random as rand
import time
# import os
# import sys

Squares = [Square(0, 10, False, (50, 50), '#000000', (0, 0), 0)]

for i in range (1, 7):
    t = rand.randint(1, 9)
    Squares.append(Square(0, t, False, (50, 50), '#000000', (i, 0), 0)) 
    
print("Square initialization successful")
gr.main(Squares)

#timer initializer

now = time.time()
print(now)
while time.time() < now + 10:
    #print(time.time())
    for i in range(0, 7):
        if time.time() - now == Squares[i].time:
            print("Square " + i + " has ran out of time!")
            Squares[i].count += 1
            cols = [rand.randint(1, 9), rand.randint(1, 9), 
            rand.randint(1, 9), rand.randint(1, 9), 
            rand.randint(1, 9), rand.randint(1, 9)]
            Squares[i].colour == "#" + cols[0] + cols[1] + cols[2] + cols[3] + cols[4] + cols[5]
            gr.redrawSquare(i, Squares)
            Squares[i].time = rand.randint(1, 9)
            

#Next:
#Assign square to drawn rectangle 
#initialize and use a timer 
#allow for colour changes to be shown in square
#show number of colour changes
#loading screen 
#Buttons and menu, like an actual app