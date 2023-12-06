import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

class ImageSmoothingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ứng dụng Lọc làm mịn ảnh")

        self.image_path = ""
        self.output_path = ""

        # Tạo các widget
        self.label = tk.Label(master, text="Chọn ảnh:")
        self.label.pack()

        self.browse_button = tk.Button(master, text="Chọn ảnh", command=self.browse_image)
        self.browse_button.pack()

        self.smooth_button = tk.Button(master, text="Làm mịn ảnh", command=self.apply_smoothing_filter)
        self.smooth_button.pack()

    def browse_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.label.config(text=f"Ảnh đã chọn: {self.image_path}")

    def apply_smoothing_filter(self):
        if not self.image_path:
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh trước.")
            return

        # Áp dụng bộ lọc làm mịn
        image = cv2.imread(self.image_path)
        smoothed_image = cv2.GaussianBlur(image, (5, 5), 0)

        # Lưu ảnh đã làm mịn (bạn có thể thay đổi đường dẫn lưu)
        self.output_path = 'output/anh_lam_min.jpg'
        cv2.imwrite(self.output_path, smoothed_image)

        # Hiển thị hộp thoại thông báo
        messagebox.showinfo("Hoàn tất", f"Ảnh đã được làm mịn và lưu tại {self.output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSmoothingApp(root)
    root.mainloop()