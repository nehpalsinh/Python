import tkinter as tk


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")


expression = ""
input_text = tk.StringVar()


def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    input_text.set("")


entry = tk.Entry(root, textvariable=input_text, font=('Arial', 20), bd=10, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2,
                  command=equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2,
                  command=lambda t=text: press(t)).grid(row=row, column=col)


tk.Button(root, text="C", width=20, height=2, command=clear).grid(row=5, column=0, columnspan=4)


root.mainloop()
