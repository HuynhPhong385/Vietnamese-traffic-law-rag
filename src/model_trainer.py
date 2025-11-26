# -*- coding: utf-8 -*-
import os 
try:
    import tensorflow as tf
    import numpy as np 
except ImportError:
    tf = None
    np = None 

# Đường dẫn để lưu file mô hình đã huấn luyện
MODEL_PATH = 'mnist_cnn_model.h5'

class ModelTrainer:
    """
    Quản lý việc định nghĩa, biên dịch và huấn luyện mô hình CNN cho MNIST.
    Sẽ tải mô hình nếu file đã tồn tại.
    """
    def __init__(self, confidence_label):
        self.model = None
        self.is_trained = False
        self.confidence_label = confidence_label # Tkinter Label để cập nhật trạng thái

        self.initialize_model()

    def initialize_model(self):
        """Định nghĩa kiến trúc mô hình CNN (chưa tải weights)"""
        if tf:
            print("Định nghĩa kiến trúc mô hình CNN...")
            # Mô hình CNN 2 lớp tích chập
            self.model = tf.keras.Sequential([
                tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
                tf.keras.layers.MaxPooling2D((2, 2)),
                tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
                tf.keras.layers.MaxPooling2D((2, 2)),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(10, activation='softmax')
            ])
            self.model.compile(optimizer='adam',
                               loss='categorical_crossentropy',
                               metrics=['accuracy'])
            print("Kiến trúc mô hình đã được biên dịch.")
            self.confidence_label.config(text="Kiến trúc mô hình đã sẵn sàng. Đang tải/huấn luyện...")
        else:
            self.confidence_label.config(text="Lỗi: Không tìm thấy TensorFlow.", fg="red")

    def train_model(self):
        """Tải mô hình đã lưu, hoặc nếu không có thì tải dữ liệu và huấn luyện"""
        if self.model is None or not tf:
            return

        # 1. Kiểm tra xem mô hình đã được lưu chưa
        if os.path.exists(MODEL_PATH):
            try:
                print(f"\nĐang tải mô hình đã huấn luyện từ: {MODEL_PATH}...")
                self.confidence_label.config(text="Đang tải mô hình đã huấn luyện...")
                # Tải toàn bộ mô hình (cấu trúc + weights)
                self.model = tf.keras.models.load_model(MODEL_PATH) 
                self.is_trained = True
                print("Tải mô hình hoàn tất.")
                self.confidence_label.config(text="Mô hình ĐÃ ĐƯỢC HUẤN LUYỆN (Tải từ file)!", fg="green")
                return
            except Exception as e:
                print(f"Lỗi khi tải mô hình từ file: {e}")
                print("Tiếp tục huấn luyện lại từ đầu...")

        # 2. Nếu chưa được lưu, tiến hành tải dữ liệu và huấn luyện
        try:
            print("\nĐang cố gắng tải dữ liệu MNIST và huấn luyện mô hình...")
            self.confidence_label.config(text="Đang tải dữ liệu MNIST (yêu cầu mạng)...")
            
            # Tải dữ liệu MNIST (sẽ thất bại nếu không có mạng)
            (x_train, y_train), (_, _) = tf.keras.datasets.mnist.load_data()

            # Tiền xử lý Dữ liệu
            x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32') / 255
            y_train = tf.keras.utils.to_categorical(y_train, 10)

            NUM_SAMPLES = 10000 
            print(f"Bắt đầu huấn luyện mô hình (sử dụng {NUM_SAMPLES} mẫu, 3 epochs)...")
            self.confidence_label.config(text=f"Đang huấn luyện mô hình ({NUM_SAMPLES} mẫu, 3 epochs)...")

            # Huấn luyện Mô hình
            self.model.fit(x_train[:NUM_SAMPLES], y_train[:NUM_SAMPLES], 
                           epochs=3, 
                           batch_size=32, 
                           verbose=1)

            self.is_trained = True
            print("Huấn luyện mô hình hoàn tất.")
            self.confidence_label.config(text="Mô hình ĐÃ ĐƯỢC HUẤN LUYỆN!", fg="green")

        # 3. Lưu mô hình sau khi huấn luyện thành công
            print(f"Đang lưu mô hình vào file: {MODEL_PATH}...")
            self.model.save(MODEL_PATH)
            print("Lưu mô hình hoàn tất.")
            
        except Exception as e:
            # Xử lý lỗi tải mạng/dữ liệu
            print(f"Lỗi khi tải dữ liệu hoặc huấn luyện mô hình: {e}")
            print("Ứng dụng sẽ tiếp tục với mô hình CHƯA được huấn luyện. Kết quả dự đoán sẽ là ngẫu nhiên.")
            self.is_trained = False
            self.confidence_label.config(text="Mô hình CHƯA được huấn luyện (Lỗi mạng). Dự đoán sẽ ngẫu nhiên.", fg="orange")
            
    def predict(self, processed_input):
        """Thực hiện dự đoán trên tensor đầu vào đã xử lý"""
        if self.model is None or np is None:
            return None, 0.0
            
        predictions = self.model.predict(processed_input, verbose=0)
        predicted_digit = np.argmax(predictions[0])
        confidence = predictions[0][predicted_digit] * 100
        return predicted_digit, confidence

    def get_status(self):
        return self.is_trained