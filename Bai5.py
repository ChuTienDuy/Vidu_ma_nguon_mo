import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFormLayout

class StudentPerformanceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Performance Prediction")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.form_layout = QFormLayout()

        self.label_exam_score = QLabel("Điểm thi cuối kỳ:")
        self.line_edit_exam_score = QLineEdit()

        self.label_study_hours = QLabel("Số giờ học:")
        self.line_edit_study_hours = QLineEdit()

        self.predict_button = QPushButton("Dự đoán Hiệu quả học tập")
        self.predict_button.clicked.connect(self.predict_performance)

        self.result_label = QLabel("Kết quả dự đoán: ")

        self.form_layout.addRow(self.label_exam_score, self.line_edit_exam_score)
        self.form_layout.addRow(self.label_study_hours, self.line_edit_study_hours)
        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.predict_button)
        self.layout.addWidget(self.result_label)

    def predict_performance(self):
        try:
            # Đọc dữ liệu từ file CSV
            df = pd.read_csv('du_lieu.csv')

            # Xác định biến độc lập (điểm thi cuối kỳ và số giờ học)
            exam_score = float(self.line_edit_exam_score.text())
            study_hours = float(self.line_edit_study_hours.text())

            # Khởi tạo mô hình hồi quy tuyến tính
            model = LinearRegression()

            # Huấn luyện mô hình trên toàn bộ dữ liệu
            X = df[['Điểm thi cuối kỳ', 'Số giờ học']]
            y = df['Hiệu quả học tập']
            model.fit(X, y)

            # Dự đoán hiệu quả học tập cho dữ liệu nhập vào
            predicted_performance = model.predict([[exam_score, study_hours]])

            # Hiển thị kết quả dự đoán
            self.result_label.setText(f"Kết quả dự đoán: {predicted_performance[0]:.2f}")
        except ValueError:
            self.result_label.setText("Vui lòng nhập số hợp lệ cho Điểm thi cuối kỳ và Số giờ học.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_app = StudentPerformanceApp()
    main_app.show()
    sys.exit(app.exec_())