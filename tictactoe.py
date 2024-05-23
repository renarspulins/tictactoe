from tkinter import*
from tkinter import messagebox
mansLogs = Tk()
mansLogs.title( TicTacToe )

speletajsX = True
count = 0

def btnClick(button):
    if button["text"] == " " and speletajsX == True:
        button["text"] = "X"
        speletajsX = False
        count+=1
    elif button["text"] == " " and speletajsX == False:
        button["text"] = "O"
        speletajsX = True
        count+=1
    else:
        messagebox.showerror("TicTacToe", "Šeit ir ieklikšķināts")
def chackWinner():
    global winner
    if (btn1["text"] == "X" and btn2{"text"} == "X" and btn3{"text"} == "X" or
       btn4["text"] == "X" and btn5{"text"} == "X" and btn3{"text"} == "X" or
       btn1["text"] == "X" and btn2{"text"} == "X" and btn3{"text"} == "X" or
       btn1["text"] == "X" and btn2{"text"} == "X" and btn3{"text"} == "X" or)
        winner = True
    return False
def btnClick(button):
    global speletajsX,count
    if button["text"] == " " and speletajsX

btn1 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn1))
btn2 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn2))
btn3 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn3))
btn4 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn4))
btn5 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn5))
btn6 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn6))
btn7 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn7))
btn8 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn8))
btn9 = Button(mansLogs, text = "", width=6, height=3, font=("Helvica",24), command=lambda:btnClick(btn9))

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
