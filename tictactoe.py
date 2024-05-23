from tkinter import*
from tkinter import messagebox #paziņojumi
mansLogs=Tk()
mansLogs.title("TicTacToe")
speletajsX=True
count=0
def btnClick(button):
    global speletajsX,count
    if button["text"]==""and speletajsX==True:
        button["text"]="X"
        speletajsX=False
        count+=1
        checkWinner()
    elif button["text"]==""and speletajsX==False:
        button["text"]="0"
        speletajsX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("TicTacToe","Šeit kāds ir ieklikšķinājis!")
def disablebuttons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""
def checkWinner():
    global winner
    if(btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X" or
        btn4["text"]=="X"and btn5["text"]=="X" and btn6["text"]=="X" or
        btn7["text"]=="X"and btn8["text"]=="X" and btn9["text"]=="X" or
        btn1["text"]=="X"and btn4["text"]=="X" and btn7["text"]=="X" or
        btn2["text"]=="X"and btn5["text"]=="X" and btn8["text"]=="X" or
        btn3["text"]=="X"and btn6["text"]=="X" and btn9["text"]=="X" or
        btn1["text"]=="X"and btn5["text"]=="X" and btn9["text"]=="X" or
        btn3["text"]=="X"and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        messagebox.showinfo("TicTacToe","Speletajs X uzvarēja")
    elif(btn1["text"]=="0"and btn2["text"]=="0" and btn3["text"]=="0" or
        btn4["text"]=="0"and btn5["text"]=="0" and btn6["text"]=="0" or
        btn7["text"]=="0"and btn8["text"]=="0" and btn9["text"]=="0" or
        btn1["text"]=="0"and btn4["text"]=="0" and btn7["text"]=="0" or
        btn2["text"]=="0"and btn5["text"]=="0" and btn8["text"]=="0" or
        btn3["text"]=="0"and btn6["text"]=="0" and btn9["text"]=="0" or
        btn1["text"]=="0"and btn5["text"]=="0" and btn9["text"]=="0" or
        btn3["text"]=="0"and btn5["text"]=="0" and btn7["text"]=="0"):
        winner=True
        messagebox.showinfo("TicTacToe","Speletajs 0 uzvarēja")

       

    elif count==9:
        winner==False
        messagebox.showinfo("TicTacToe","Neizšķirts")

           