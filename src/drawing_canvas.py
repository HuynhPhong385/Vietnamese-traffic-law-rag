# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np

class DrawingCanvas:
    """
    Quản lý Tkinter Canvas, hình ảnh backend (PIL) và logic vẽ.
    """
    def __init__(self, master, width=280, height=280):
        self.canvas_width = width
        self.canvas_height = height
        self.drawing = False
        self.last_x, self.last_y = None, None
        
        # Khởi tạo hình ảnh PIL (Backend image)
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), 0) 
        self.draw = ImageDraw.Draw(self.image)
        
        # Tạo Tkinter Canvas
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, 
                                bg="black", cursor="crosshair", bd=0, 
                                highlightthickness=3, highlightbackground="#3b82f6")

        # Gán sự kiện chuột
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def start_draw(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw_line(self, event):
        if self.drawing:
            x, y = event.x, event.y
            
            # Vẽ trên Tkinter Canvas (để hiển thị)
            self.canvas.create_line(self.last_x, self.last_y, x, y, 
                                    fill="white", width=20, capstyle=tk.ROUND, smooth=tk.TRUE)
            
            # Vẽ trên Backend PIL Image (để xử lý)
            self.draw.line([self.last_x, self.last_y, x, y], 
                           fill="white", width=20, joint="round")
            
            self.last_x, self.last_y = x, y

    def stop_draw(self, event):
        self.drawing = False
        self.last_x, self.last_y = None, None

    def clear(self):
        """Xóa canvas Tkinter và hình ảnh backend"""
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), 0)
        self.draw = ImageDraw.Draw(self.image)

    def preprocess_image(self):
        """Chuẩn bị ảnh từ Canvas thành tensor (1, 28, 28, 1)"""
        # 1. Resize ảnh PIL sang 28x28
        img_resized = self.image.resize((28, 28), Image.Resampling.LANCZOS)
        
        # 2. Chuyển đổi sang mảng Numpy (0=đen, 255=trắng)
        img_array = np.array(img_resized, dtype=np.float32)
        
        # 3. Chuẩn hóa và định hình lại
        img_array /= 255.0
        processed_input = img_array.reshape(1, 28, 28, 1)
        
        return processed_input