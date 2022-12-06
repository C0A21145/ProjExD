import tkinter as tk
import maze_maker


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global key, mx, my
    old_place = [mx, my]

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

    canvas.coords("kokaton", mx*50+25, my*50+25)
    root.after(100, main_proc)


if __name__ == "__main__":
    # 初期位置設定
    mx, my = 1, 1
    # 押されているキー保管場所
    key = ""

    root = tk.Tk()
    root.title("Tkinter")
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

    # 動き実装関数
    main_proc()

    root.mainloop()
