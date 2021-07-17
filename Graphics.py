import tkinter as tk
import threading
#from Square import Square
root = tk.Tk()
def main(S):
    
    #root points to main components of graphics

    drawParent(root)#parent window
    rootLabel(root)#the label on the parent window

    box = tk.Canvas(root, highlightthickness = 0, highlightbackground = "#ff0000", 
                    bg = "#ffffff")
    box.config(width = 428, height = 428)
    #creates white background to put squares on

    # for j in range (0, 7):
    #      for i in range(0, 7):
    #          drawSquare(i, j, box)#draws 8*8 of squares
    for i in range (0, len(S)):
        drawSquare(i, 0, box, S)

    root.mainloop()#displays everything

    

#Creates a parent container containing all my drawings a window) belonging to the TK root
def drawParent(p):
    p.geometry('500x500')#size of parent
    p.configure(bg = '#000000')#background colour
    p.title("Euler's Square")#title at top of window

#adds label to form (parent, i.e., the root)
def rootLabel(r):
    string=tk.Label(r, text = "Now assign a square to a drawn rectangle", bg = '#fff')
    string.pack()

def redrawSquare(i, S):
    drawSquare(S[i].locindex[0], S[i].locindex[1], root , S)


#draws a single square on box
def drawSquare(i, j, r, S):
    r.create_rectangle(10 + i * 60, 10 + j * 60, 10 + S[i].size[0] + i * 60, 10 + S[i].size[1] + j * 60, fill=S[i].colour)
    r.pack()

#timer stopper
def timertest():
    print("stop")