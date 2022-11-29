import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("tk_calculator")
root.geometry("300x500")


def show_btn():
    buttons = [0 for _ in range(10)]
    r, c = 0, 0
    for i in range(10):
        buttons[i] = tk.Button(root,
                               text=f"{abs(9-i)}",
                               width=4, height=2,
                               font=("", 30))

        buttons[i].grid(row=r, column=c)
        buttons[i].bind("<1>", button_click)

        c += 1
        if c % 3 == 0:
            r += 1
            c = 0


show_btn()

root.mainloop()
