import tkinter as tk

global cx, cy, key


def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    cx = 300
    cy = 400
    photo = tk.PhotoImage(file="fig/0.png")
    canvas.create_image(cx, cy, image=photo)

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    root.mainloop()
