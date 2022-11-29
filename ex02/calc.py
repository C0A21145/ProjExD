import tkinter as tk
import tkinter.messagebox as tkm
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# ボタンが押された際に呼び出される関数


def button_click(event):
    global count
    btn = event.widget
    txt = btn["text"]

    if txt == "ans":
        ans = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)

    elif txt == "AC":
        entry.delete(0, tk.END)

    elif txt == "Graph":
        imgfilePath = calc_graph(entry.get())
        # print(imgfilePath)
        image = tk.PhotoImage(file=imgfilePath)
        canvas = tk.Canvas(width=300, height=300)
        canvas.create_image(0, 0, image=image)
        canvas.place(x=100, y=100)
        #canvas.grid(row=1, column=5, columnspan=4, rowspan=4)
        # print(canvas)

    elif txt == "=" or txt == "x" or txt == "y":
        entry.insert(tk.END, txt)

    else:
        try:
            a = int(txt)
            entry.insert(tk.END, txt)
            count = 0
        except ValueError:
            if count == 0:
                entry.insert(tk.END, txt)
                count += 1
            else:
                pass

# 数字ボタン


def show_num_btn():
    buttons = [0 for _ in range(10)]
    r, c = 1, 1
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

# 四則演算、特殊記号


def show_symbol_btn():
    # 足し算(+)
    buttons = tk.Button(root,
                        text=f"+",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=1, column=3)
    buttons.bind("<1>", button_click)

    # 引き算(-)
    buttons = tk.Button(root,
                        text=f"-",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=2, column=3)
    buttons.bind("<1>", button_click)

    # 掛け算(x)
    buttons = tk.Button(root,
                        text=f"*",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=3, column=3)
    buttons.bind("<1>", button_click)

    # 割り算(/)
    buttons = tk.Button(root,
                        text=f"/",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=4, column=3)
    buttons.bind("<1>", button_click)

    # y
    buttons = tk.Button(root,
                        text=f"y",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=1, column=4)
    buttons.bind("<1>", button_click)

    # x
    buttons = tk.Button(root,
                        text=f"x",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=2, column=4)
    buttons.bind("<1>", button_click)

    # =ボタン
    buttons = tk.Button(root,
                        text=f"=",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=3, column=4)
    buttons.bind("<1>", button_click)

    # 答えボタン
    buttons = tk.Button(root,
                        text=f"ans",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=4, column=2)
    buttons.bind("<1>", button_click)

    # ACボタン
    buttons = tk.Button(root,
                        text=f"AC",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=1, column=0)
    buttons.bind("<1>", button_click)

    # graph button
    buttons = tk.Button(root,
                        text=f"Graph",
                        width=4, height=2,
                        font=("", 30))
    buttons.grid(row=4, column=4)
    buttons.bind("<1>", button_click)


def calc_graph(siki):
    graph_label = siki
    siki = list(siki)
    # 傾きの値
    katamuki = ""
    seppen = ""
    num = 2
    if "+" in siki:
        seppen_place = siki.index("+")
        seppen = siki[seppen_place+1:]
        seppen = int("".join(seppen))

    while True:
        if siki[num].isdecimal():
            katamuki += siki[num]
            num += 1
        else:
            break

    # デバッグ用
    print(f"katamuki {katamuki}")
    print(f"seppen {seppen}")

    katamuki = int(katamuki)

    # グラフ描画
    # グラフ画像保存先
    filepath = "./ex02/graph2.png"

    # グラフ座標情報取得
    x = [i for i in range(-10, 11, 1)]
    # try:
    #   y = [(i*katamuki) + seppen for i in range(-10, 11, 1)]
    # except:
    #   y = [i*katamuki for i in range(-10, 11, 1)]
    y = [i*katamuki for i in range(-10, 11, 1)]
    print(x)
    print(y)

    plt.figure(figsize=(3, 3))
    plt.plot(x, y, label=graph_label)
    plt.savefig(filepath)

    return filepath


# ---------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    root.title("tk_calculator")
    root.geometry("900x500")

    # global変数
    count = 0

    # text Box
    entry = tk.Entry(root,
                     justify="right",
                     width=10,
                     font=("", 40))
    entry.grid(row=0, column=0, columnspan=5)

    show_num_btn()
    show_symbol_btn()

    root.mainloop()
