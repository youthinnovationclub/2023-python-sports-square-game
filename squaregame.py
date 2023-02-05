# GUI based Tic Tac Toe Game
from tkinter import *
from tkinter import messagebox
window=Tk()

window.title("Welcome to ball square pool game")
window.geometry("900x700")

lbl=Label(window,text="Ball square pool game",font=('Helvetica','18'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player 1: X",font=('Helvetica','15'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2: O",font=('Helvetica','15'))
lbl.grid(row=2,column=0)
lbl=Label(window,text="Kansas City Chiefs (red)",font=('Helvetica','15'))
lbl.grid(row=5,column=0)
lbl=Label(window,text="Philadephia Eagles (green)",font=('Helvetica','15'))
lbl.grid(row=7,column=0)

turn=1; #For first person turn.

def clicked1():
    global turn
    if btn1["text"]==" ":   #For getting the text of a button
        if turn==1:
            turn =2;
            btn1["text"]="X"
        elif turn==2:
            turn=1;
            btn1["text"]="O"
        check();
def clicked2():
    global turn
    if btn2["text"]==" ":
        if turn==1:
            turn =2;
            btn2["text"]="X"
        elif turn==2:
            turn=1;
            btn2["text"]="O"
        check();
def clicked3():
    global turn
    if btn3["text"]==" ":
        if turn==1:
            turn =2;
            btn3["text"]="X"
        elif turn==2:
            turn=1;
            btn3["text"]="O"
        check();
def clicked4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
            turn =2;
            btn4["text"]="X"
        elif turn==2:
            turn=1;
            btn4["text"]="O"
        check();
def clicked5():
    global turn
    if btn5["text"]==" ":
        if turn==1:
            turn =2;
            btn5["text"]="X"
        elif turn==2:
            turn=1;
            btn5["text"]="O"
        check();
def clicked6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
            turn =2;
            btn6["text"]="X"
        elif turn==2:
            turn=1;
            btn6["text"]="O"
        check();
def clicked7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
            turn =2;
            btn7["text"]="X"
        elif turn==2:
            turn=1;
            btn7["text"]="O"
        check();
def clicked8():
    global turn
    if btn8["text"]==" ":
        if turn==1:
            turn =2;
            btn8["text"]="X"
        elif turn==2:
            turn=1;
            btn8["text"]="O"
        check();
def clicked9():
    global turn
    if btn9["text"]==" ":
        if turn==1:
            turn =2;
            btn9["text"]="X"
        elif turn==2:
            turn=1;
            btn9["text"]="O"
        check();
flag=1;
def check():
    global flag;
    b1 = btn1["text"];
    b2 = btn2["text"];
    b3 = btn3["text"];
    b4 = btn4["text"];
    b5 = btn5["text"];
    b6 = btn6["text"];
    b7 = btn7["text"];
    b8 = btn8["text"];
    b9 = btn9["text"];
    flag=flag+1;
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"]);
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"]);
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"]);
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"]);
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"]);
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn1["text"]);
    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(btn7["text"]);
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        window.destroy()

def win(player):
    ans = "Game complete " +player + " wins ";
    messagebox.showinfo("Congratulations", ans)
    window.destroy()  # is used to close the program


btn11 = Button(window, text=" ",bg="gray", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn11.grid(column=1, row=1)
btn21 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn21.grid(column=2, row=1)
btn31 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn31.grid(column=3, row=1)
btn41 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn41.grid(column=4, row=1)
btn51 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn51.grid(column=5, row=1)
btn61 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn61.grid(column=6, row=1)
btn71 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn71.grid(column=7, row=1)
btn81 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn81.grid(column=8, row=1)
btn91 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn91.grid(column=9, row=1)
btn101 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn101.grid(column=10, row=1)
btn111 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn111.grid(column=11, row=1)

btn12 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn12.grid(column=1, row=2)
btn22 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn22.grid(column=2, row=2)
btn32 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn32.grid(column=3, row=2)
btn42 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn42.grid(column=4, row=2)
btn52 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn52.grid(column=5, row=2)
btn62 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn62.grid(column=6, row=2)
btn72 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn72.grid(column=7, row=2)
btn82 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn82.grid(column=8, row=2)
btn92 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn92.grid(column=9, row=2)
btn102 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn102.grid(column=10, row=2)
btn112 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn112.grid(column=11, row=2)

btn13 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn13.grid(column=1, row=3)
btn23 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn23.grid(column=2, row=3)
btn33 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn33.grid(column=3, row=3)
btn43 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn43.grid(column=4, row=3)
btn53 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn53.grid(column=5, row=3)
btn63 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn63.grid(column=6, row=3)
btn73 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn73.grid(column=7, row=3)
btn83 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn83.grid(column=8, row=3)
btn93 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn93.grid(column=9, row=3)
btn103 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn103.grid(column=10, row=3)
btn113 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn113.grid(column=11, row=3)

btn14 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn14.grid(column=1, row=4)
btn24 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn24.grid(column=2, row=4)
btn34 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn34.grid(column=3, row=4)
btn44 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn44.grid(column=4, row=4)
btn54 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn54.grid(column=5, row=4)
btn64 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn64.grid(column=6, row=4)
btn74 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn74.grid(column=7, row=4)
btn84 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn84.grid(column=8, row=4)
btn94 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn94.grid(column=9, row=4)
btn104 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn104.grid(column=10, row=4)
btn114 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn114.grid(column=11, row=4)

btn15 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn15.grid(column=1, row=5)
btn25 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn25.grid(column=2, row=5)
btn35 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn35.grid(column=3, row=5)
btn45 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn45.grid(column=4, row=5)
btn55 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn55.grid(column=5, row=5)
btn65 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn65.grid(column=6, row=5)
btn75 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn75.grid(column=7, row=5)
btn85 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn85.grid(column=8, row=5)
btn95 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn95.grid(column=9, row=5)
btn105 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn105.grid(column=10, row=5)
btn115 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn115.grid(column=11, row=5)

btn16 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn16.grid(column=1, row=6)
btn26 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn26.grid(column=2, row=6)
btn36 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn36.grid(column=3, row=6)
btn46 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn46.grid(column=4, row=6)
btn56 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn56.grid(column=5, row=6)
btn66 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn66.grid(column=6, row=6)
btn76 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn76.grid(column=7, row=6)
btn86 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn86.grid(column=8, row=6)
btn96 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn96.grid(column=9, row=6)
btn106 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn106.grid(column=10, row=6)
btn116 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn116.grid(column=11, row=6)

btn17 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn17.grid(column=1, row=7)
btn27 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn27.grid(column=2, row=7)
btn37 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn37.grid(column=3, row=7)
btn47 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn47.grid(column=4, row=7)
btn57 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn57.grid(column=5, row=7)
btn67 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn67.grid(column=6, row=7)
btn77 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn77.grid(column=7, row=7)
btn87 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn87.grid(column=8, row=7)
btn97 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn97.grid(column=9, row=7)
btn107 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn107.grid(column=10, row=7)
btn117 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn117.grid(column=11, row=7)

btn18 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn18.grid(column=1, row=8)
btn28 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn28.grid(column=2, row=8)
btn38 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn38.grid(column=3, row=8)
btn48 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn48.grid(column=4, row=8)
btn58 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn58.grid(column=5, row=8)
btn68 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn68.grid(column=6, row=8)
btn78 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn78.grid(column=7, row=8)
btn88 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn88.grid(column=8, row=8)
btn98 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn98.grid(column=9, row=8)
btn108 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn108.grid(column=10, row=8)
btn118 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn118.grid(column=11, row=8)

btn19 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn19.grid(column=1, row=9)
btn29 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn29.grid(column=2, row=9)
btn39 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn39.grid(column=3, row=9)
btn49 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn49.grid(column=4, row=9)
btn59 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn59.grid(column=5, row=9)
btn69 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn69.grid(column=6, row=9)
btn79 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn79.grid(column=7, row=9)
btn89 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn89.grid(column=8, row=9)
btn99 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn99.grid(column=9, row=9)
btn109 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn109.grid(column=10, row=9)
btn119 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn119.grid(column=11, row=9)

btn110 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn110.grid(column=1, row=9)
btn210 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn210.grid(column=2, row=9)
btn310 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn310.grid(column=3, row=9)
btn410 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn410.grid(column=4, row=9)
btn510 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn510.grid(column=5, row=9)
btn610 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn610.grid(column=6, row=9)
btn710 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn710.grid(column=7, row=9)
btn810 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn810.grid(column=8, row=9)
btn910 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn910.grid(column=9, row=9)
btn1010 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn1010.grid(column=10, row=9)
btn1110 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn1110.grid(column=11, row=9)

btn111 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn111.grid(column=1, row=10)
btn211 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn211.grid(column=2, row=10)
btn311 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn311.grid(column=3, row=10)
btn411 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn411.grid(column=4, row=10)
btn511 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn511.grid(column=5, row=10)
btn611 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn611.grid(column=6, row=10)
btn711 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn711.grid(column=7, row=10)
btn811 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn811.grid(column=8, row=10)
btn911 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn911.grid(column=9, row=10)
btn1011 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn1011.grid(column=10, row=10)
btn1111 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn1111.grid(column=11, row=10)

btn112 = Button(window, text=" ",bg="green", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn112.grid(column=1, row=11)
btn212 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn212.grid(column=2, row=11)
btn312 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn312.grid(column=3, row=11)
btn412 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn412.grid(column=4, row=11)
btn512 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn512.grid(column=5, row=11)
btn612 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn612.grid(column=6, row=11)
btn712 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
btn712.grid(column=7, row=11)
btn812 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn812.grid(column=8, row=11)
btn912 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn912.grid(column=9, row=11)
btn1012 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
btn1012.grid(column=10, row=11)
btn1112 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
btn1112.grid(column=11, row=11)

window.mainloop()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
