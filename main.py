from tkinter import *

# Making window
root = Tk()
root.title("Calculator")

canvas_width = 420
canvas_height = 660

root.geometry(f"{canvas_width}x{canvas_height}")
root.resizable(0, 0)


# Changing Screen
def setInpVal(value):
    global inpVal
    inpVal.set(value)
    screen.update()


# Taking Input
def inputEnter(event):
    global inpVal
    global isError
    keyList = ['+', '-', '*', '/', '.', '(', ')']
    specialKeyList = ['c', 'C', '\x08', '=', '\r']
    inputEntered = event.char
    for i in range(10):
        keyList.append(f"{i}")

    if inputEntered in keyList:
        if isError:
            setInpVal(inputEntered)
        else:
            setInpVal(inpVal.get() + inputEntered)
        isError = False
    elif inputEntered == specialKeyList[0] or inputEntered == specialKeyList[1]:
        setInpVal("")
        isError = False
    elif inputEntered == specialKeyList[2] and not isError:
        setInpVal(inpVal.get()[:-1])
        isError = False
    elif inputEntered == specialKeyList[3] or inputEntered == specialKeyList[4]:
        try:
            setInpVal(eval(inpVal.get()))  # Calculating Result
            isError = False
        except Exception as e:
            setInpVal("Syntax Error")  # If error occurs
            isError = True


# Clicking a Button
def click(event):
    global inpVal
    global isError
    text = event.widget.cget("text")  # Getting text of clicked button
    if text == "=":
        try:
            setInpVal(eval(inpVal.get()))  # Calculating Result
            isError = False
        except Exception as e:
            setInpVal("Syntax Error")  # If error occurs
            isError = True
    elif text == "C":
        setInpVal("")  # Clearing Screen
        isError = False
    elif text == "<":
        if not isError:
            setInpVal(inpVal.get()[:-1])  # Backspace Button
            isError = False
    else:
        if isError:
            setInpVal(text)
        else:
            setInpVal(inpVal.get() + text)  # Other Buttons
        isError = False


# Input Screen
inpVal = StringVar()
inpVal.set("")

# Making Screen
screen = Label(root, textvar=inpVal, font="lucida 40 bold", relief=SUNKEN, bg="#6C7B6E", fg="white", anchor="w")
screen.pack(fill=X, padx=10, pady=10)
root.bind("<Key>", inputEnter)

# Making frames for rows of buttons
f0 = Frame(root, bg="grey")
f0.pack()
f1 = Frame(root, bg="grey")
f1.pack()
f2 = Frame(root, bg="grey")
f2.pack()
f3 = Frame(root, bg="grey")
f3.pack()
f4 = Frame(root, bg="grey")
f4.pack()

# List of Buttons
numList = ["9", "8", "7", "+",
           "6", "5", "4", "-",
           "3", "2", "1", "*",
           ".", "0", "=", "/",
           "<", "(", ")", "C"]

# Making Buttons
for i in range(len(numList)):
    b = Button(f0, text=numList[i], padx=10, font="lucida 35 bold")
    if i // 4 == 0:
        b = Button(f0, text=numList[i], padx=10, font="lucida 35 bold")
    elif i // 4 == 1:
        b = Button(f1, text=numList[i], padx=10, font="lucida 35 bold")
    elif i // 4 == 2:
        b = Button(f2, text=numList[i], padx=10, font="lucida 35 bold")
    elif i // 4 == 3:
        b = Button(f3, text=numList[i], padx=10, font="lucida 35 bold")
    elif i // 4 == 4:
        b = Button(f4, text=numList[i], padx=10, font="lucida 35 bold")

    # Equalizing size of some buttons
    if numList[i] == "(" or numList[i] == ")":
        b = Button(f4, text=numList[i], padx=15, font="lucida 35 bold")
    elif numList[i] == ".":
        b = Button(f3, text=numList[i], padx=17, font="lucida 35 bold")

    # Packing Buttons
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)

# Starting Window
isError = False
root.mainloop()