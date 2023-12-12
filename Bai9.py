import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEnhancerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Enhancer")

        # Tạo các biến lưu trữ ảnh
        self.original_image = None
        self.enhanced_image = None

        # Tạo các biến điều chỉnh độ sáng
        self.alpha_var = tk.DoubleVar(value=1.5)
        self.beta_var = tk.IntVar(value=30)

        # Tạo các thành phần giao diện
        self.create_widgets()

    def create_widgets(self):
        # Nút chọn ảnh
        select_image_button = tk.Button(self.root, text="Chọn ảnh", command=self.select_image)
        select_image_button.pack(pady=10)

        # Thanh trượt điều chỉnh alpha
        alpha_label = tk.Label(self.root, text="Alpha:")
        alpha_label.pack()
        alpha_slider = tk.Scale(self.root, from_=0.1, to=3.0, resolution=0.1, orient=tk.HORIZONTAL, variable=self.alpha_var)
        alpha_slider.pack()

        # Thanh trượt điều chỉnh beta
        beta_label = tk.Label(self.root, text="Beta:")
        beta_label.pack()
        beta_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, variable=self.beta_var)
        beta_slider.pack()

        # Nút tăng cường ảnh
        enhance_button = tk.Button(self.root, text="Tăng cường ảnh", command=self.enhance_image)
        enhance_button.pack(pady=10)

        # Hiển thị ảnh gốc và ảnh được tăng cường
        self.original_label = tk.Label(self.root, text="Ảnh gốc")
        self.original_label.pack()
        self.original_canvas = tk.Canvas(self.root)
        self.original_canvas.pack()

        self.enhanced_label = tk.Label(self.root, text="Ảnh được tăng cường")
        self.enhanced_label.pack()
        self.enhanced_canvas = tk.Canvas(self.root)
        self.enhanced_canvas.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.show_image(self.original_image, self.original_canvas)

    def enhance_image(self):
        if self.original_image is not None:
            alpha = self.alpha_var.get()
            beta = self.beta_var.get()
            self.enhanced_image = self.enhance_brightness(self.original_image, alpha, beta)
            self.show_image(self.enhanced_image, self.enhanced_canvas)

    def enhance_brightness(self, image, alpha=1.5, beta=30):
        enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
        return enhanced_image

    def show_image(self, image, canvas):
        if image is not None:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image=image)
            canvas.config(width=photo.width(), height=photo.height())
            canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            canvas.image = photo

def main():
    root = tk.Tk()
    app = ImageEnhancerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()