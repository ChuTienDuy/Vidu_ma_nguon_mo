import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, Canvas
from tkinter import filedialog
from PIL import Image, ImageTk

class DataAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Analyzer")

        # Tạo biến lưu trữ dữ liệu
        self.data = None
        # Tạo các thành phần giao diện
        self.create_widgets()

    def create_widgets(self):
        # Nút chọn dữ liệu
        select_data_button = Button(self.root, text="Chọn dữ liệu", command=self.select_data)
        select_data_button.pack(pady=10)

        # Nút phân tích dữ liệu
        analyze_button = Button(self.root, text="Phân tích dữ liệu", command=self.analyze_data)
        analyze_button.pack(pady=10)

        # Hiển thị đồ thị
        self.canvas = Canvas(self.root, width=400, height=300)
        self.canvas.pack()

    def select_data(self):
        def select_data(self):
            file_path = filedialog.askopenfilename(title="Chọn tệp dữ liệu", filetypes=[("Text files", "*.csv")])
            if file_path:
                # Bỏ qua dòng tiêu đề khi tải dữ liệu
                self.data = np.loadtxt(file_path, skiprows=1)
                print("Dữ liệu đã được tải từ:", file_path)

    def analyze_data(self):
        if self.data is not None:
            # Tìm giá trị lớn nhất, nhỏ nhất và trung bình
            max_value = np.max(self.data)
            min_value = np.min(self.data)
            mean_value = np.mean(self.data)

            # Vẽ histogram
            plt.hist(self.data, bins=20, color='blue', edgecolor='black')
            plt.title('Phân phối dữ liệu')
            plt.xlabel('Giá trị')
            plt.ylabel('Số lần xuất hiện')

            # Hiển thị đồ thị trong giao diện
            self.display_plot()

            # In kết quả
            result_text = f'Giá trị lớn nhất: {max_value}\nGiá trị nhỏ nhất: {min_value}\nGiá trị trung bình: {mean_value}'
            result_label = Label(self.root, text=result_text)
            result_label.pack()

    def display_plot(self):
        # Hiển thị đồ thị trong giao diện
        plt.savefig('plot.png')
        plot_image = Image.open('plot.png')
        plot_image = ImageTk.PhotoImage(plot_image)
        self.canvas.config(width=plot_image.width(), height=plot_image.height())
        self.canvas.create_image(0, 0, anchor='nw', image=plot_image)
        self.canvas.image = plot_image

def main():
    root = Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()