# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, PhotoImage
import numpy as np
import threading
# Import các module đã refactor
try:
    from src.model_trainer import ModelTrainer
    from src.drawing_canvas import DrawingCanvas
except ImportError:
    # Xử lý nếu các file không được đặt trong cùng thư mục
    print("Lỗi Import: Đảm bảo 'model_trainer.py' và 'drawing_canvas.py' nằm trong cùng thư mục.")
    ModelTrainer = None
    DrawingCanvas = None

class DigitRecognizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Ứng Dụng Nhận Diện Số Viết Tay")
        logo = PhotoImage(file="Logo_Handwritten.png")
        master.iconphoto(False, logo)
        master.configure(bg="#f0f0f0") 
        master.resizable(False, False)

        # --- Tạo hiệu ứng Card UI (Khung trắng nổi) ---
        main_card = tk.Frame(master, bg="white", padx=40, pady=25, bd=1, relief="flat", highlightbackground="#cccccc", highlightthickness=1)
        
        # Sử dụng pack để căn giữa Card
        main_card.pack(padx=30, pady=30, fill=tk.BOTH, expand=True)

        # Tiêu đề
        tk.Label(main_card, text="Nhận Diện Số Viết Tay", font=("Inter", 18, "bold"), fg="#000000", bg="white").pack(pady=(0, 5))
        
        # Trạng thái mô hình / Lỗi (Vị trí 1)
        self.confidence_label = tk.Label(main_card, text="Đang khởi tạo mô hình...", font=("Inter", 10), fg="red", bg="white")
        self.confidence_label.pack(pady=(5, 10))

        # Nhãn hướng dẫn
        tk.Label(main_card, text="Vẽ số vào đây (280x280)", font=("Inter", 12, "bold"), fg="#555555", bg="white").pack(pady=(10, 5))

        # --- Khung chứa Canvas và Dự đoán (Sử dụng Grid) ---
        content_frame = tk.Frame(main_card, bg="white")
        content_frame.pack(pady=10)

        # Khởi tạo Canvas (vị trí grid 0, 0)
        self.draw_manager = DrawingCanvas(content_frame)
        self.draw_manager.canvas.grid(row=0, column=0, padx=(0, 20))

        # Khung chứa Kết quả Dự đoán (vị trí grid 0, 1)
        prediction_frame = tk.Frame(content_frame, bg="white")
        prediction_frame.grid(row=0, column=1)

        tk.Label(prediction_frame, text="Dự đoán:", font=("Inter", 14), fg="#333333", bg="white").pack()

        # Label hiển thị kết quả (Dấu ?)
        self.result_label = tk.Label(prediction_frame, text="?", font=("Inter", 60, "bold"), fg="#3b82f6", bg="white")
        self.result_label.pack(pady=(0, 20))
        
        # --- Nút hành động ---
        button_frame = tk.Frame(main_card, bg="white")
        button_frame.pack(pady=20)
        
        # Nút Xóa (Màu Đỏ)
        tk.Button(button_frame, text="Xóa", command=self.clear_canvas, 
                  font=("Inter", 12, "bold"), bg="#ef4444", fg="white", 
                  activebackground="#dc2626", activeforeground="white", 
                  relief="raised", bd=2, padx=20, pady=10).pack(side=tk.LEFT, padx=10)

        # Nút Nhận diện (Màu Xanh lá)
        tk.Button(button_frame, text="Nhận diện", command=self.predict_digit, 
                  font=("Inter", 12, "bold"), bg="#10b981", fg="white", 
                  activebackground="#059669", activeforeground="white", 
                  relief="raised", bd=2, padx=20, pady=10).pack(side=tk.LEFT, padx=10)
        
        # Thông báo hướng dẫn ở cuối
        tk.Label(main_card, text="Hãy vẽ một chữ số (từ 0-9) bằng nét đậm và rõ ràng.", font=("Inter", 10), fg="gray", bg="white").pack(pady=(10, 0))

        # --- Khởi tạo và Bắt đầu Huấn luyện Mô hình ---
        self.trainer = ModelTrainer(self.confidence_label)
        
        # Chạy huấn luyện ở luồng (thread) nền để không làm treo giao diện
        threading.Thread(target=self.trainer.train_model, daemon=True).start()
    def clear_canvas(self):
        """Xóa canvas và cập nhật trạng thái dự đoán."""
        self.draw_manager.clear()
        self.result_label.config(text="?")
        
        # Cập nhật thông báo trạng thái mô hình (từ ModelTrainer)
        if self.trainer.get_status():
            self.confidence_label.config(text="Mô hình ĐÃ ĐƯỢC HUẤN LUYỆN!", fg="green")
        else:
            self.confidence_label.config(text="Lỗi khi tải mô hình. Vui lòng kiểm tra kết nối mạng.", fg="red")

    def predict_digit(self):
        """Thực hiện dự đoán và cập nhật giao diện."""
        if not self.trainer or self.trainer.model is None:
            messagebox.showerror("Lỗi", "Hệ thống học máy chưa sẵn sàng.")
            return

        processed_input = self.draw_manager.preprocess_image()

        # Kiểm tra nét vẽ
        if np.sum(processed_input) < 1.0: 
            messagebox.showwarning("Cảnh báo", "Vui lòng vẽ một chữ số rõ ràng trước khi nhận diện.")
            return

        # Thực hiện dự đoán
        predicted_digit, confidence = self.trainer.predict(processed_input)
            
        # Cập nhật giao diện
        self.result_label.config(text=str(predicted_digit))
        
        # Cập nhật độ tin cậy bên dưới trạng thái mô hình
        if self.trainer.get_status():
             self.confidence_label.config(text=f"Độ tin cậy: {confidence:.2f}%", fg="#10b981")
        else:
             self.confidence_label.config(text=f"Độ tin cậy: {confidence:.2f}% (Mô hình chưa được huấn luyện)", fg="orange")
            