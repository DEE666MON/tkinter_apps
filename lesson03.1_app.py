import tkinter as tk

entryText = ""
num1Text = ""
num2Text = ""
operatorText = ""
countClickForOperators = False
result = 0.0
def all_clear(flag = True):
    global entryText, num1Text, num2Text, operatorText, countClickForOperators, result
    if flag:
        print(f"{entryText}|{num1Text}|{num2Text}|{operatorText}|{countClickForOperators}|{result}")
        entryText = ""
        num1Text = ""
        num2Text = ""
        operatorText = ""
        countClickForOperators = False
        result = 0.0
    else:
        entryText = ""
        num1Text = ""
        num2Text = ""
        operatorText = ""
        countClickForOperators = False
        # print(result)
def btn0_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("0", end="")
    if num1Text != "" and operatorText == "":
        entryText += "0"
        num1Text += "0"
    elif num2Text != "" and operatorText != "":
        entryText += "0"
        num2Text += "0"
    entry.config(text=entryText)
def btn1_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("1", end="")
    if operatorText == "":
        entryText += "1"
        num1Text += "1"
    elif operatorText != "":
        entryText += "1"
        num2Text += "1"
    entry.config(text=entryText)
def btn2_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("2", end="")
    if operatorText == "":
        entryText += "2"
        num1Text += "2"
    elif operatorText != "":
        entryText += "2"
        num2Text += "2"
    entry.config(text=entryText)
def btn3_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("3", end="")
    if operatorText == "":
        entryText += "3"
        num1Text += "3"
    elif operatorText != "":
        entryText += "3"
        num2Text += "3"
    entry.config(text=entryText)
def btn4_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("4", end="")
    if operatorText == "":
        entryText += "4"
        num1Text += "4"
    elif operatorText != "":
        entryText += "4"
        num2Text += "4"
    entry.config(text=entryText)
def btn5_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("5", end="")
    if operatorText == "":
        entryText += "5"
        num1Text += "5"
    elif operatorText != "":
        entryText += "5"
        num2Text += "5"
    entry.config(text=entryText)
def btn6_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("6", end="")
    if operatorText == "":
        entryText += "6"
        num1Text += "6"
    elif operatorText != "":
        entryText += "6"
        num2Text += "6"
    entry.config(text=entryText)
def btn7_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("7", end="")
    if operatorText == "":
        entryText += "7"
        num1Text += "7"
    elif operatorText != "":
        entryText += "7"
        num2Text += "7"
    entry.config(text=entryText)
def btn8_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("8", end="")
    if operatorText == "":
        entryText += "8"
        num1Text += "8"
    elif operatorText != "":
        entryText += "8"
        num2Text += "8"
    entry.config(text=entryText)
def btn9_Click():
    global entryText, num1Text, num2Text, operatorText
    # print("9", end="")
    if operatorText == "":
        entryText += "9"
        num1Text += "9"
    elif operatorText != "":
        entryText += "9"
        num2Text += "9"
    entry.config(text=entryText)
def btnPlus_Click():
    global entryText, num1Text, num2Text, operatorText, countClickForOperators, result
    # if not countClickForOperators:
    #     print("\n+")
    # if countClickForOperators:
    #     print("\n=")
    if num1Text != "" and not countClickForOperators:
        entryText += " + "
        operatorText = "+"
        countClickForOperators = True
    if operatorText != "+" and operatorText != "":
        operatorText = "+"
        countClickForOperators = True
        entryText = f"{num1Text} {operatorText} {num2Text}"
    entry.config(text=entryText)
def btnMinus_Click():
    global entryText, num1Text, num2Text, operatorText, countClickForOperators, result
    # if not countClickForOperators:
    #     print("\n-")
    # if countClickForOperators:
    #     print("\n=")
    if num1Text != "" and not countClickForOperators:
        entryText += " - "
        operatorText = "-"
        countClickForOperators = True
    if operatorText != "-" and operatorText != "":
        operatorText = "-"
        countClickForOperators = True
        entryText = f"{num1Text} {operatorText} {num2Text}"
    entry.config(text=entryText)
def btnMultiply_Click():
    global entryText, num1Text, num2Text, operatorText, countClickForOperators, result
    # if not countClickForOperators:
    #     print("\n*")
    # if countClickForOperators:
    #     print("\n=")
    if num1Text != "" and not countClickForOperators:
        entryText += " * "
        operatorText = "*"
        countClickForOperators = True
    if operatorText != "*" and operatorText != "":
        operatorText = "*"
        countClickForOperators = True
        entryText = f"{num1Text} {operatorText} {num2Text}"
    entry.config(text=entryText)
def btnDivide_Click():
    global entryText, num1Text, num2Text, operatorText, countClickForOperators, result
    # if not countClickForOperators:
    #     print("\n/")
    # if countClickForOperators:
    #     print("\n=")
    if num1Text != "" and not countClickForOperators:
        entryText += " / "
        operatorText = "/"
        countClickForOperators = True
    if operatorText != "/" and operatorText != "":
        operatorText = "/"
        countClickForOperators = True
        entryText = f"{num1Text} {operatorText} {num2Text}"
    entry.config(text=entryText)
def btnEqual_Click():
    global entryText, num1Text, num2Text, operatorText, countClickForOperators, result
    if num1Text != "" and num2Text != "" and countClickForOperators:
        if operatorText == "+":
            result = float(num1Text) + float(num2Text)
        if operatorText == "-":
            result = float(num1Text) - float(num2Text)
        if operatorText == "*":
            result = float(num1Text) * float(num2Text)
        if operatorText == "/":
            result = float(num1Text) / float(num2Text)
        entry.config(text=f"{result}")
        countClickForOperators = False
        all_clear(False)
def btnClear_Click():
    # print("\nC")
    all_clear()
    entry.config(text=entryText)

root = tk.Tk()
root.title("Калькулятор")
window_w, window_h = 335, 365
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (screen_w - window_w) // 2, (screen_h - window_h) // 2
root.geometry(f"{window_w}x{window_h}+{x}+{y}")
root.resizable(False, False)
entry = tk.Label(root, text=entryText, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
btn0 = tk.Button(root, text="0", command=btn0_Click, font=("Arial", 18), width=5, height=2)
btn1 = tk.Button(root, text="1", command=btn1_Click, font=("Arial", 18), width=5, height=2)
btn2 = tk.Button(root, text="2", command=btn2_Click, font=("Arial", 18), width=5, height=2)
btn3 = tk.Button(root, text="3", command=btn3_Click, font=("Arial", 18), width=5, height=2)
btn4 = tk.Button(root, text="4", command=btn4_Click, font=("Arial", 18), width=5, height=2)
btn5 = tk.Button(root, text="5", command=btn5_Click, font=("Arial", 18), width=5, height=2)
btn6 = tk.Button(root, text="6", command=btn6_Click, font=("Arial", 18), width=5, height=2)
btn7 = tk.Button(root, text="7", command=btn7_Click, font=("Arial", 18), width=5, height=2)
btn8 = tk.Button(root, text="8", command=btn8_Click, font=("Arial", 18), width=5, height=2)
btn9 = tk.Button(root, text="9", command=btn9_Click, font=("Arial", 18), width=5, height=2)
btnOperationPlus = tk.Button(root, text="+", command=btnPlus_Click, font=("Arial", 18), width=5, height=2)
btnOperationMinus = tk.Button(root, text="-", command=btnMinus_Click, font=("Arial", 18), width=5, height=2)
btnOperationMultiply = tk.Button(root, text="*", command=btnMultiply_Click, font=("Arial", 18), width=5, height=2)
btnOperationDivide = tk.Button(root, text="/", command=btnDivide_Click, font=("Arial", 18), width=5, height=2)
btnOperationEqual = tk.Button(root, text="=", command=btnEqual_Click, font=("Arial", 18), width=5, height=2)
btnOperationClear = tk.Button(root, text="C", command=btnClear_Click, font=("Arial", 18), width=5, height=2)
btn9.grid(row= 1, column= 2, padx=2, pady=2)
btn8.grid(row= 1, column= 1, padx=2, pady=2)
btn7.grid(row= 1, column= 0, padx=2, pady=2)
btnOperationPlus.grid(row= 1, column= 3, padx=2, pady=2)
btn6.grid(row= 2, column= 2, padx=2, pady=2)
btn5.grid(row= 2, column= 1, padx=2, pady=2)
btn4.grid(row= 2, column= 0, padx=2, pady=2)
btnOperationMinus.grid(row= 2, column= 3, padx=2, pady=2)
btn3.grid(row= 3, column= 2, padx=2, pady=2)
btn2.grid(row= 3, column= 1, padx=2, pady=2)
btn1.grid(row= 3, column= 0, padx=2, pady=2)
btnOperationMultiply.grid(row= 3, column= 3, padx=2, pady=2)
btnOperationClear.grid(row= 4, column= 0, padx=2, pady=2)
btn0.grid(row= 4, column= 1, padx=2, pady=2)
btnOperationEqual.grid(row= 4, column= 2, padx=2, pady=2)
btnOperationDivide.grid(row= 4, column= 3, padx=2, pady=2)
root.mainloop()