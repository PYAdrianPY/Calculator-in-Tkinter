from tkinter import *

window = Tk()
window.geometry('250x250')

TextInOperator = StringVar()
operator = ""

def clickbutton(number):
    global operator
    operator = operator + str(number)
    TextInOperator.set(operator)
#adding
def equalbut():
    global operator
    result = str(eval(operator))
    TextInOperator.set(result)
    operator = ''
# Create an entry widget to display the input
ShowText = Entry(window, font=("Courier New", 12, 'bold'), textvariable=TextInOperator, width=20, bd=5, bg='powder blue')
ShowText.pack()

# Create buttons for numbers
But1 = Button(window, text="1", command=lambda: clickbutton(1),width=6,height=2)
But1.place(x=20,y=70)

But2 = Button(window, text="2", command=lambda: clickbutton(2),width=6,height=2)
But2.place(x=72,y=70)

But3 = Button(window, text="3", command= lambda: clickbutton(3),width=6,height=2)
But3.place(x=124,y=70)

But4 = Button(window, text="4", command= lambda: clickbutton(4),width=6,height=2)
But4.place(x=20,y=112)

But5 = Button(window,text="5",command= lambda: clickbutton(5),width=6,height=2)
But5.place(x=72,y=112)

But6 = Button(window,text="6", command = lambda: clickbutton(6), width=6, height=2)
But6.place(x=124,y=112)

But7 = Button(window, text="7", command= lambda: clickbutton(7), width=6, height=2)
But7.place(x=20,y=154)

But8 = Button(window, text="8", command= lambda: clickbutton(8),width=6,height=2)
But8.place(x=72,y=154)

But9 = Button(window,text="9", command= lambda: clickbutton(9),width=6,height=2)
But9.place(x=124,y=154)

But0 = Button(window,text="0",command=lambda:clickbutton(0),width=6,height=2)
But0.place(x=72,y=195)

AddButton = Button(window, text="+", command=lambda: clickbutton("+"),width=6,height=2)
AddButton.place(x=176,y=70)

SubButton = Button(window, text="-", command= lambda: clickbutton("-"),width=6,height=2)
SubButton.place(x=176,y=112)

MulButton = Button(window,text="*",command= lambda: clickbutton("*"),width=6,height=2)
MulButton.place(x=176,y=154)

DivButton = Button(window,text="/",command= lambda:clickbutton("/"), width=6,height=2)
DivButton.place(x=176,y=195)

DotButton = Button(window, text=".", command= lambda: clickbutton("."),width=6,height=2)
DotButton.place(x=124,y=195)


EqualButton = Button(window, text="=",command = equalbut,width=6,height=2)
EqualButton.place(x=20,y=195)
window.mainloop()
