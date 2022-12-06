import tkinter as tk
import maze_maker


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy, key, mx, my
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

    canvas.coords("kokaton", mx*100+50, my*100+50)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_list = maze_maker.make_maze(15, 9)
    maze_maker.show_maze(canvas, maze_list)

    mx, my = 1, 1
    cx = 250
    cy = 250
    photo = tk.PhotoImage(file="fig/0.png")
    canvas.create_image(cx, cy, image=photo, tag="kokaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()
