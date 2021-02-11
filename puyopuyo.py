import tkinter
import random

index = 0
tugi = 0
x_cursor = 0
y_cursor = 0
x_mouse = 0
y_mouse = 0
c_mouse = 0
score = 0
timer = 0
key = 0
i = 0



def mouse_move(e):
    global x_mouse , y_mouse

    x_mouse = e.x
    y_mouse = e.y

def mouse_press(e):
    global c_mouse
    c_mouse = 1

neko = []
check = []
for i in range(10):
    neko.append([0,0,0,0,0,0,0,0])
    check.append([0,0,0,0,0,0,0,0])

def key_down(e):
    global key
    key = e.keycode

def move_neko():
    global key
    for y in range(8,-1,-1):
        for x in range(6,-1,-1):
            if neko[y][x] > 0 and neko[y+1][x] == 0:    
                if key == 39 and neko[y][x+1] == 0:
                    neko[y][x+1] = neko[y][x]
                    neko[y][x] = 0

                if key == 40:
                    neko[y+1][x] = neko[y][x]
                    neko[y][x] = 0

        for x in range(8):
            if neko[y][x] > 0 and neko[y+1][x] == 0 and neko[y][x-1] == 0:
                if key == 37:
                    neko[y][x-1] = neko[y][x]
                    neko[y][x] = 0
    key = 0
    

def change_neko():
    for y in range(8,-1,-1):
        for x in range(7):
            if neko[y][x+1] > 0 and neko[y][x] > 0 and neko[y+1][x] == 0:
                c_mouse = 0
                neko[y-1][x+1] = neko[y][x]
                neko[y][x] =0
                return
    for y in range(8,-1,-1):
        for x in range(8):
            if neko[y][x] > 0 and neko[y+1][x] == 0:    
                c_mouse = 0
                neko[y-1][x-1] = neko[y][x]
                neko[y][x] = 0
                return
    




    
def down_neko():
    for y in range(8,-1, -1):
        for x in range(8):
            if neko[y][x] > 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=neko_image[neko[y][x]], tag = "neko")

def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x]

    for y in range(1,9):
        for x in range(1,7):
            if check[y][x] > 0:
                if check[y-1][x-1] == check[y][x] and check[y+1][x+1] == check[y][x]:
                    check[y-1][x-1] = 7
                    check[y][x] = 7
                    check[y+1][x+1] = 7

                elif check[y+1][x-1] == check[y][x] and check[y-1][x+1] == check[y][x]:
                    check[y+1][x-1] = 7
                    check[y][x] = 7
                    check[y-1][x+1] = 7

    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x+1] == check[y][x] and check[y][x-1] == check[y][x]:
                    check[y][x+1] = 7
                    check[y][x] = 7
                    check[y][x-1] = 7

    for y in range(1,9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y-1][x] == check[y][x] and check[y+1][x] == check[y][x]:
                    check[y-1][x] = 7
                    check[y][x]  = 7
                    check[y+1][x] = 7

    for y in range(10):
        for x in range(8):
            neko[y][x] = check[y][x]

tugi = [[0],
        [0]
        ]
def tugi_neko():
    for y in range(2):
        tugi[y][0] = random.randint(1,6)
    

def neko_delete():
    num = 0
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 7:
                neko[y][x]= 0
                num = num + 1


    for i in range(10):
        for y in range(8,-1,-1):
            for x in range(8):
                if neko[y+1][x] == 0 and neko[y][x] > 0 :
                    neko[y+1][x] = neko[y][x]
                    neko[y][x] = 0
    return num


def over():
    over_neko = False
    for x in range(8):
        if neko[0][x] > 0:
            over_neko = True

    return over_neko



def draw_txt(txt,x,y,siz,col,tg):
    fnt = ("Times New Roman",siz,"bold")
    cvs.create_text(x+2,y+2,text=txt,fill="black",font=fnt,tag=tg)

def game_main():
    global index,timer,score,tugi,c_mouse,x_mouse,y_mouse,x_cursor,y_cursor,key,i
    if index == 0:
        draw_txt("ねこねこ",312,240,100,"violet","TITLE")
        draw_txt("Click to start",312,560,50,"orange","TITLE")
        index = 1
        c_mouse = 0
        key = 0
    elif index == 1:
        if c_mouse == 1:
            timer = 0
            score = 0
            c_mouse = 0
            x_mouse = 0
            y_mouse = 0
            x_cursor = 0
            y_cursor = 0
            key = 0
            tugi_neko()
            draw_neko()
            cvs.delete("TITLE")
            index = 2
            i = 0

    elif index == 2:
        tugi_neko()
        cvs.delete("neko")
        draw_neko()
        if neko[1][3] == 0 and neko[0][3] ==0:
            neko[1][3] = tugi[1][0]
            neko[0][3] = tugi[0][0]
            index = 3
        else :
            neko[0][3] = tugi[0][0]
            index = 5
        cvs.delete(neko)
        draw_neko()
        index = 3

    elif index == 3:

        if int(i) < 10:
            if c_mouse == 1:
                change_neko()
                c_mouse = 0
            down_neko()
            move_neko()
            cvs.delete("neko")
            draw_neko()
            i += 1
            index = 3 

        else:
            i = 0
            index = 4

    elif index == 4:
        check_neko()
        cvs.delete("neko")
        draw_neko()
        num = neko_delete()
        sc = num*10
        score += sc
        cvs.delete("neko")
        draw_neko()

        index = 5

    elif index == 5:
        if over() == False:
            cvs.delete(neko)
            draw_neko()

            index = 2
        else:
            index = 6

    elif index == 6:

        timer += 1
        if timer == 1:
            draw_txt("GAME OVER",312,348,60,"red","over")

        if timer == 50:
            cvs.delete("over")
            index == 0

    cvs.delete("INFO")
    draw_txt("SCORE"+str(score),160,60,32,"blue","INFO")
    if True:
        for y in range(1):
            cvs.create_image(752,128,image = neko_image[tugi[y][0]],tag = "INFO")

    root.after(1000, game_main)

root = tkinter.Tk()
root.title("落ち物パズル「ネコネコ」")
root.resizable(True,True)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
root.bind("<KeyPress>",key_down)
cvs = tkinter.Canvas(root,width = 912,height = 768)
cvs.pack()


bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file = "neko_cursor.png")
neko_image = [
    None,
    tkinter.PhotoImage(file = "neko1.png"),
    tkinter.PhotoImage(file = "neko2.png"),
    tkinter.PhotoImage(file = "neko3.png"),
    tkinter.PhotoImage(file = "neko4.png"),
    tkinter.PhotoImage(file = "neko5.png"),
    tkinter.PhotoImage(file = "neko6.png"),
    tkinter.PhotoImage(file = "neko_niku.png")
    ]
cvs.create_image(456,384,image = bg)
game_main()
root.mainloop()

    
            
            
        
        
