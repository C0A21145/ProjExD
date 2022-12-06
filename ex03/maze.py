import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker
import random


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def put_coin():
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    for i in range(coin_limit):
        x = random.randint(1, 28)
        y = random.randint(1, 16)
        if maze_list[x][y] == 1:
            for p in range(4):
                if maze_list[x+XP[p]][y+YP[p]] == 0:
                    x = x+XP[p]
                    y = y+YP[p]
        coin_img = tk.PhotoImage(file="fig/small_coin.png")
        canvas.create_image(x*50+25, y*50+25, image=coin_img)


def main_proc():
    global key, mx, my, time_limit, coin_limit, get_coin
    old_place = [mx, my]
    flag = 0

    if key == "Up":
        my -= 1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1

    if maze_list[mx][my] == 1:
        mx = old_place[0]
        my = old_place[1]

    canvas.coords("timer", 0, 0, time_limit, 25)
    if [mx, my] in coin_place:
        coin_position = coin_place.index([mx, my])
        canvas.delete(f"coin_{coin_position}")
        coin_place[coin_position] = [0, 0]
        get_coin += 1

    canvas.coords("kokaton", mx*50+25, my*50+25)
    time_limit -= 5
    if time_limit < 0 or get_coin >= coin_limit:
        flag = 1
    if flag == 0:
        root.after(100, main_proc)
    elif get_coin >= coin_limit:
        if tkm.showinfo("おめでとう", "Game Clear") == "ok":
            root.destroy()
    else:
        if tkm.showerror("残念", "Game Over") == "ok":
            root.destroy()


if __name__ == "__main__":
    # 初期位置設定
    mx, my = 1, 1
    # 押されているキー保管場所
    key = ""
    # 制限時間
    time_limit = 1500
    # コイン配置枚数
    coin_limit = 10
    # コイン取得枚数
    get_coin = 0

    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    # 迷路リスト作成、描画
    maze_list = maze_maker.make_maze(30, 18)
    maze_maker.show_maze(canvas, maze_list)

    # こうかとん描画
    photo = tk.PhotoImage(file="fig/small_0.png")
    canvas.create_image(mx*50+25, my*50+25, image=photo, tag="kokaton")

    # 押されたボタンの取得
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    # タイマーの初期図形配置
    canvas.create_rectangle(
        0, 0, 1500, 25, outline="black", fill="red", tag="timer")

    # コイン配置
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1,  0]
    coin_place = [[0, 0] for _ in range(coin_limit)]
    coin_imgs = []
    for i in range(coin_limit):
        x = random.randint(1, 28)
        y = random.randint(1, 16)
        if maze_list[x][y] == 1:
            for p in range(4):
                if maze_list[x+XP[p]][y+YP[p]] == 0:
                    x = x+XP[p]
                    y = y+YP[p]
        coin_img = tk.PhotoImage(file="fig/small_coin.png")
        coin_imgs.append(coin_img)
        coin_place[i] = [x, y]
        canvas.create_image(x*50+25, y*50+25, image=coin_img, tag=f"coin_{i}")

    # 動き実装関数
    main_proc()

    root.mainloop()
