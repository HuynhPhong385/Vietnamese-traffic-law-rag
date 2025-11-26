import tkinter as tk
from src.digit_app import DigitRecognizerApp 

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    
    try:
        app = DigitRecognizerApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Lỗi ứng dụng không mong muốn: {e}")