import tkinter as tk

global cx, cy

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tkinter")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    root.mainloop()
