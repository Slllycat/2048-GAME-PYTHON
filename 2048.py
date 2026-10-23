#2048 the game my mother loved
import tkinter as tk
import random
import math

#press Arrows to play :O and 0 for autoplay
biggnes=50      #50 standart ( pixel size)
mx=0
my=0
amount=3        #3 standart
size=6        #6 standart
size2 = size**2


#window setup
window = tk.Tk()
window.title("BLEH")
window.geometry(str(size * biggnes) + "x" + str(size * biggnes+50))
canvas = tk.Canvas(window, width=(size * biggnes), height=(size * biggnes+50), bg="black")
canvas.pack()


#resets
def reset():
    global size,size2,blocks
    blocks = []
    for i in range(size2):
        blocks.append(0)
reset()


def render():
    global cube,blocks,size
    x = 0
    y = biggnes*size
    weg = 0
    canvas.delete("all")
    # RENDER BLOCKS
    for i in range(size):
        for i in range(size):
            if blocks[weg]==0:
                cube = canvas.create_rectangle(x+(biggnes//10), y-(biggnes//10), x + biggnes-(biggnes//10), y - biggnes+(biggnes//10), fill="grey")

            else:

                color = ["#FFF4C2","#FFD68A","#FFB35E","#FF8E3A","#FF6622","#FF2F1A","#FF0000","#D3006A","#A0009A","#7200C0","#5000E0","#FFFFFF"]
                if int(math.log2(blocks[weg]))-1<=11:
                    farbe= color[int(math.log2(blocks[weg]))-1]
                else:
                    farbe=color[11]
                cube = canvas.create_rectangle(x+(biggnes//10), y-(biggnes//10), x + biggnes-(biggnes//10), y - biggnes+(biggnes//10), fill=farbe)
                canvas.create_text(x+biggnes/2, y-biggnes/2, text=(blocks[weg]), fill="BLACK", font=("Arial Black", biggnes//5))

            weg = weg + 1
            x = x + biggnes
        x = 0
        y = y - biggnes
    score()


def tick(direction):
    global size,size2,blocks
    for i in range(size*4):
        for i in range(size2):
            if blocks[i]!=0:
                if 0<=(i+direction)<size2 and (i//size == (i+direction)//size or i%size == (i+direction)%size):
                    if blocks[i+direction]==0:
                        blocks[i+direction]=blocks[i]
                        blocks[i]=0
                    elif blocks[i]==blocks[i+direction]:
                        blocks[i+direction]=blocks[i]+blocks[i+direction]
                        blocks[i]=0
    new()


def new():
    global size2,blocks
    for i in range(random.randint(1,1)):
        d=0
        weg=0
        while (d==0 or blocks[weg]!=0) and d<250:
            weg=random.randint(0,size2-1)
            d+=1
        if d<250:
            """
            if random.randint(1,10)>=8:
                blocks[weg]=4
            else:
                blocks[weg]=2
            """
            blocks[weg]=2


def score():
    global blocks,size,biggnes
    score=0
    for i in range(size2):
        score+=blocks[i]
    canvas.create_text(50, size * biggnes+20, text=("Score:"), fill="red", font=("Arial", 20))
    canvas.create_text(120, size * biggnes+20, text=(int(score)), fill="red", font=("Arial", 20))


#TASTEN
def move(event):
    global mx, my,size
    if event.keysym == "Up":
        tick(size)
    if event.keysym == "Down":
        tick(-size)
    if event.keysym == "Right":
        tick(1)
    if event.keysym == "Left":
        tick(-1)
    if event.keysym == "a":
        auto()
    render()

window.bind("<Key>", move)


def auto():
    global blocks
    lo=-1
    err=0
    while lo != blocks and err<1000000:
        lo = blocks[:]
        type1=1
        if type1 == 1:
            tick(-1)
            tick(-size)
        elif type1 == 2:
            tick(size)
            tick(1)
            tick(-size)
            tick(-1)
            print(err)
        elif type1==3:
            tick(-1)
            tick(-size)
            tick(1)
        err+=1
    render()





new()
render()
window.mainloop()
