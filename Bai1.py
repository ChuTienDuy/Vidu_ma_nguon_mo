import numpy as np
import tkinter as tk
from tkinter import messagebox

def solve_linear_system(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        return None  # Trường hợp ma trận không khả nghị hoặc không xác định

def solve_button_click():
    # Lấy dữ liệu từ các trường nhập liệu
    n = int(entry_n.get())
    try:
        A = np.zeros((n, n))
        b = np.zeros(n)

        for i in range(n):
            for j in range(n):
                A[i, j] = float(entry_A[i][j].get())
            b[i] = float(entry_b[i].get())

        # Giải hệ phương trình
        solution = solve_linear_system(A, b)

        if solution is not None:
            result_text.config(text="Kết quả:")
            for i in range(n):
                result_text.config(text=result_text.cget("text") + f"\nx{i + 1} = {solution[i]}")
        else:
            messagebox.showerror("Lỗi", "Hệ phương trình không có nghiệm hoặc có nhiều nghiệm.")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên cho n và số thực cho các hệ số.")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Giải hệ phương trình tuyến tính")

# Tạo các widget
label_n = tk.Label(root, text="Nhập số lượng phương trình và ẩn:")
label_n.pack()

entry_n = tk.Entry(root)
entry_n.pack()

label_equations = tk.Label(root, text="Nhập các hệ số:")
label_equations.pack()

entry_A = []
entry_b = []

solve_button = None  # Tránh lỗi UnboundLocalError
result_text = None

def create_equation_entries():
    global solve_button
    global result_text

    for i in range(n):
        frame = tk.Frame(root)
        frame.pack()

        entry_A_row = []
        for j in range(n):
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            entry_A_row.append(entry)
        entry_A.append(entry_A_row)

        entry_b_i = tk.Entry(frame)
        entry_b_i.pack(side=tk.LEFT)
        entry_b.append(entry_b_i)

    solve_button = tk.Button(root, text="Giải", command=solve_button_click)
    solve_button.pack()

    result_text = tk.Label(root, text="")
    result_text.pack()

# Thiết lập sự kiện cho việc nhập giá trị n
def n_entry_callback(event):
    global n
    try:
        n = int(entry_n.get())
        create_equation_entries()
    except ValueError:
        pass

entry_n.bind("<Return>", n_entry_callback)

# Khởi chạy cửa sổ giao diện
root.mainloop()