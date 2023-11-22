import tkinter as tk
from tkinter import END, Scrollbar, Text
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = np.array(df)

# Tạo bảng màu
bang_mau = ['#FF5733', '#33FF57', '#3377FF', '#FFFF33', '#FF33AF', '#33FFAF', '#AA55FF', '#00CC66']

# Danh sách lớp
ds_lop = ['Lớp 1', 'Lớp 2', 'Lớp 3', 'Lớp 4', 'Lớp 5', 'Lớp 6', 'Lớp 7', 'Lớp 8', 'Lớp 9']

# Thiết lập các chức năng trong báo cáo

# Tổng số sinh viên khop tính số sinh viên đạt và thi trượt , tính tỷ lệ
def tongsv():
    sv = in_data[:, 1]
    tongsv = np.sum(sv)
    result_text.insert(END, "Tổng số sinh viên đi thi: " + str(tongsv) + " sinh viên\n")

    svtruot = in_data[:, 10]
    tongsvtruot = np.sum(svtruot)
    tongsvdat = tongsv - tongsvtruot

    tyle_dat = round((tongsvdat / tongsv) * 100, 2)
    tyle_truot = round((tongsvtruot / tongsv) * 100, 2)

    result_text.insert(END, "Tổng số sinh viên qua môn: " + str(tongsvdat) + " sinh viên (" + str(tyle_dat) + "%)\n")
    result_text.insert(END, "Tổng số sinh viên trượt môn: " + str(tongsvtruot) + " sinh viên (" + str(tyle_truot) + "%)\n\n")
    values1 = np.sum(in_data[0:9, 2:10], axis=1).flatten()
    values2 = in_data[:, 10]

    fig, ax1 = plt.subplots(figsize=(8, 18))

    ax1.bar(ds_lop, values1, color='blue', label="Sinh viên đạt")
    ax1.bar(ds_lop, values2, bottom=values1, color='red', label="Sinh viên trượt")

    for i, (v1, v2) in enumerate(zip(values1, values2)):
        ax1.text(i, v1/2, str(v1), ha='center', va='bottom', color='white', fontweight='bold')
        ax1.text(i, v1 + v2/2, str(v2), ha='center', va='bottom', color='white', fontweight='bold')

    ax1.set_title('Biểu đồ số sinh viên đạt, trượt của từng lớp')
    ax1.set_ylabel('Số sinh viên')
    ax1.legend(loc='upper right')

    plt.subplots_adjust(hspace=0.5)
    plt.show()

# Số sinh viên đạt điểm A
def svdatA():
    diemA = in_data[:, 3]
    maxa = diemA.max()
    i = np.argmax(diemA)
    result_text.config(state=tk.NORMAL)
    result_text.insert(END, 'Lớp có nhiều sinh viên đạt điểm A nhất là lớp {0} có {1} sinh viên\n'.format(in_data[i, 0], maxa))
    values1 = in_data[:, 3]

    plt.figure(4)
    bars = plt.bar(ds_lop, values1, label="Lớp có nhiều sinh viên điểm A nhất", color=bang_mau)
    plt.title('Biểu đồ số sinh viên đạt điểm A của các lớp')
    plt.ylabel('Số sinh viên')
    plt.legend(loc='upper right')

    for bar, value in zip(bars, values1):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, value, ha='center', va='bottom')

    plt.show()

# Tính Phổ điểm
def phodiem():
    labels = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
    diems = in_data[:, 3:11]
    tong_cacdiem = diems.sum(axis=0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Vẽ biểu đồ tròn
    ax1.pie(tong_cacdiem, labels=labels, autopct='%1.1f%%', colors=bang_mau)
    ax1.axis('equal')
    ax1.set_title('Phổ điểm ')

    # Vẽ Biểu đồ cột
    ax2.bar(labels, tong_cacdiem, color=bang_mau)
    ax2.set_xlabel('Điểm')
    ax2.set_ylabel('Số lượng sinh viên')
    ax2.set_title('Phổ điểm')
    for i, v in enumerate(tong_cacdiem):
        ax2.annotate(str(v), (i, v), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

# số sv đạt chuẩn  L1 L2 của từng lớp
def svdat_L1_L2():
    # Tính toán số lượng sv đạt chuẩn
    l2 = in_data[:, 1] - in_data[:, 10] - in_data[:, 9] - in_data[:, 8]  # L2 = số sv - F - D - D+
    SVD = in_data[:, 9] + in_data[:, 8]  # số sv đạt D + (D+)
    SVF = in_data[:, 10]  # số sv đạt F

    plt.figure(figsize=(10, 6))

    # tạo biểu đồ cột
    bars = plt.bar(ds_lop, l2, width=0.4, label='Số sinh viên đạt L2', color='blue')
    plt.bar(ds_lop, SVD, width=0.4, label='Số sinh viên đạt D và D+', color='red', bottom=l2)
    plt.bar(ds_lop, SVF, width=0.4, label='Số sinh viên đạt F', color='green', bottom=l2 + SVD)

    # Thêm chỉ số
    for i, bar in enumerate(bars):
        l2_count = l2[i]
        l3_count = SVD[i]
        l4_count = SVF[i]

        plt.text(bar.get_x() + bar.get_width() / 2, l2_count / 2, str(l2_count), ha='center', va='bottom', color='white', fontweight='bold')
        plt.text(bar.get_x() + bar.get_width() / 2, l2_count + l3_count / 2, str(l3_count), ha='center', va='bottom', color='white', fontweight='bold')
        plt.text(bar.get_x() + bar.get_width() / 2, l2_count + l3_count + l4_count / 2, str(l4_count), ha='center', va='bottom', color='white', fontweight='bold')

    # thêm tổng sv
    for i, bar in enumerate(bars):
        total_count = l2[i] + SVD[i] + SVF[i]
        plt.text(bar.get_x() + bar.get_width() / 2, total_count + 2, str(total_count), ha='center', va='bottom', color='black')

    plt.xlabel('Lớp')
    plt.ylabel('Số lượng sinh viên')
    plt.title('SỐ SINH VIÊN ĐẠT CHUẨN')
    plt.legend()
    plt.show()

# Reset kết quả
def reset():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, END)
    plt.close('all')
    result_text.config(state=tk.DISABLED)

# Tạo cửa sổ giao diện window
window = tk.Tk()
window.title("BÁO CÁO KẾT QUẢ THI")

# Tạo tiêu đề
# Tạo tiêu đề
tieude = tk.Label(window, text="BÁO CÁO KẾT QUẢ THI", font=("Helvetica", 24), fg="red")
tieude.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Thiết lập kích thước , phông chữ cho nút nhấn
button_width = 10
button_font = ('Arial', 15)

tongsv_button = tk.Button(window, text="TỔNG SỐ SINH VIÊN DỰ THI", command=tongsv, width=button_width, font=button_font)
svdatA_button = tk.Button(window, text="LỚP CÓ NHIỀU SV ĐẠT A NHẤT", command=svdatA, width=button_width, font=button_font)
phodiem_button = tk.Button(window, text="PHỔ ĐIỂM CỦA 9 LỚP", command=phodiem, width=button_width, font=button_font)
svdat_L1_L2_button = tk.Button(window, text="SINH VIÊN ĐẠT CHUẨN L1/L2 ", command=svdat_L1_L2, width=button_width, font=button_font)

reset_button = tk.Button(window, text="RESET", command=reset, width=button_width, font=button_font)

# Thiết lập kết quả hiển thị
result_text = Text(window, wrap="word", height=20, width=200)
result_text_scrollbar = Scrollbar(window, command=result_text.yview)
result_text.config(yscrollcommand=result_text_scrollbar.set)

# Thiết lập thông số cho button
tongsv_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
svdatA_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
phodiem_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
svdat_L1_L2_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Đặt widget hiển thị kết quả
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew") # Mở rộng và lấp đầy ô lưới

# Thiết lập button reset
reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# chạy
window.mainloop()