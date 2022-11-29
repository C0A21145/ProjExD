import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}のボタンが押されました")


def show_num_btn():
    buttons = [0 for _ in range(10)]
    r, c = 1, 0
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


def text_box():
    entry = tk.Entry(root,
                     justify="right",
                     width=10,
                     font=("", 40))
    entry.grid(row=0, column=0, columnspan=3)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("tk_calculator")
    root.geometry("300x500")

    text_box()
    show_num_btn()

    root.mainloop()
