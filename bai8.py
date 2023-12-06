import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog

class TachBienAnhApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chương trình Tách biên ảnh")

        self.image_path = ""
        self.output_path = ""

        self.label = Label(master, text="Chọn ảnh:")
        self.label.pack()

        self.browse_button = Button(master, text="Chọn ảnh", command=self.browse_image)
        self.browse_button.pack()

        self.tach_bien_button = Button(master, text="Tách biên ảnh", command=self.tach_bien_anh)
        self.tach_bien_button.pack()

    def browse_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.label.config(text=f"Ảnh đã chọn: {self.image_path}")

    def tach_bien_anh(self):
        if not self.image_path:
            self.show_error("Vui lòng chọn ảnh trước.")
            return

        # Đọc ảnh từ đường dẫn
        image = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)

        # Áp dụng bộ lọc Sobel để tìm biên
        sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

        # Tính toán biên độ tổng hợp
        gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

        # Chuyển về định dạng uint8 (8-bit) để hiển thị được với OpenCV
        gradient_magnitude = np.uint8(gradient_magnitude)

        # Hiển thị ảnh gốc và ảnh đã tách biên
        plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray')
        plt.title('Ảnh Gốc'), plt.xticks([]), plt.yticks([])

        plt.subplot(1, 2, 2), plt.imshow(gradient_magnitude, cmap='gray')
        plt.title('Ảnh Tách biên'), plt.xticks([]), plt.yticks([])

        plt.show()

        # Lưu ảnh đã tách biên (tùy chọn)
        self.output_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                           filetypes=[("PNG files", "*.png")])
        if self.output_path:
            cv2.imwrite(self.output_path, gradient_magnitude)
            self.show_info(f"Ảnh đã được tách biên và lưu tại {self.output_path}")

    def show_error(self, message):
        messagebox.showerror("Lỗi", message)

    def show_info(self, message):
        messagebox.showinfo("Thông báo", message)

if __name__ == "__main__":
    root = Tk()
    app = TachBienAnhApp(root)
    root.mainloop()