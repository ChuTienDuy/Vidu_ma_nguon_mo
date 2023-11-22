import tkinter as tk
from tkinter import Canvas, Label, Button, Entry

class GeometryLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phần Mềm Học Hình Học")
        self.canvas = Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.label = Label(root, text="Vẽ hình:")
        self.label.pack()

        self.shape_entry = Entry(root, width=20)
        self.shape_entry.pack()

        self.draw_button = Button(root, text="Vẽ", command=self.draw_shape)
        self.draw_button.pack()

    def draw_shape(self):
        shape = self.shape_entry.get()
        if shape == "hình tròn" :
            self.canvas.create_oval(50, 50, 200, 200, fill="blue")
        elif shape == "hình vuông":
            self.canvas.create_rectangle(250, 50, 400, 200, fill="green")
        elif shape == "tam giác":
            self.canvas.create_polygon(450, 50, 600, 50, 525, 200, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometryLearningApp(root)
    root.mainloop()