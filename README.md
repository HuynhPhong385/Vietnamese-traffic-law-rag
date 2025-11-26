Ứng Dụng Nhận Dạng Số Viết Tay (Tkinter & TensorFlow)

Đây là một ứng dụng desktop đơn giản được xây dựng bằng Python (Tkinter) cho phép người dùng vẽ một chữ số (0-9) và sử dụng mô hình Mạng Tích Chập (CNN) được huấn luyện trên tập dữ liệu MNIST (TensorFlow/Keras) để dự đoán chữ số đó.

Tính năng

Giao diện đồ họa đơn giản, trực quan.

Canvas cho phép người dùng vẽ bằng chuột.

Tự động tải và huấn luyện mô hình CNN khi khởi động ứng dụng (với 3 epochs đơn giản).

Hiển thị kết quả dự đoán và độ tin cậy.

Cài đặt (Installation)

Để chạy ứng dụng này, bạn cần cài đặt Python (phiên bản 3.x) và các thư viện cần thiết.

Clone repository (Nếu bạn đang sử dụng Git):

git clone <URL_DỰ_ÁN_CỦA_BẠN>
cd <TÊN_THƯ_MỤC>


Cài đặt các dependencies (Sử dụng requirements.txt):

pip install -r requirements.txt


Sử dụng

Chạy file chính của ứng dụng:

python digit_recognizer.py


Lưu ý

Ứng dụng yêu cầu một môi trường đồ họa đầy đủ (như Windows, macOS, hoặc Linux có X Server) để hiển thị giao diện Tkinter. Nó sẽ không hoạt động trên các môi trường chỉ có console (ví dụ: SSH không có X-forwarding).

Quá trình huấn luyện mô hình sẽ tự động chạy khi khởi động và có thể mất vài phút tùy thuộc vào hiệu suất CPU/GPU của bạn.