# Handwritten Digit Recognition

A complete desktop application for recognizing handwritten digits using **Python**, **Tkinter GUI**, and a **Convolutional Neural Network (CNN) trained on the MNIST dataset**.

This project includes:
- A GUI application for prediction  
- A fully trainable deep learning model  
- Preprocessing utilities  
- Dataset training scripts  
- Editable assets for UI  

---

## 📌 Table of Contents
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Model Training](#-model-training)
- [Technologies Used](#-technologies-used)
- [Screenshots](#-screenshots)
- [License](#-license)
- [Contributing](#-contributing)

---

##  Features
-  **Draw digits directly on the canvas**  
-  **Instant prediction** using a trained CNN model  
-  **Image preprocessing** that converts canvas drawings into MNIST-like format  
-  Buttons: **Predict**, **Clear**, **Exit**  
-  Lightweight, does not require GPU to run  
-  Includes full training source code  

---

## 🖼 Demo
> *(Bạn thêm ảnh vào thư mục `assets/` và đổi đường dẫn dưới đây)*  

![demo](assets/demo.png)

---

## 📦 Installation

### 1️⃣ Clone this repository

git clone https://github.com/<your-username>/handwritten-recognition.git
cd handwritten-recognition

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ (Optional) Install TensorFlow CPU/GPU manually

TensorFlow CPU:
pip install tensorflow

TensorFlow GPU:
pip install tensorflow-gpu

### ▶️ Usage

Run the desktop application:
python main.py
Use the canvas to draw a digit (0–9), then click Predict.

---

# Project Structure

handwriting-recognition/
│
├── assets/                     # Images used for UI, demo, or documentation
│   ├── demo.png
│   ├── logo.png
│   └── result.png
│
├── models/
│   └── mnist_cnn_model.h5      # Pretrained MNIST model for prediction
│
├── src/
│   ├── __init__.py
│   ├── main.py                 # Main entry point – runs the app or server
│   │
│   ├── digit_app.py            # Flask backend / API for digit recognition
│   ├── drawing_canvas.py       # Canvas logic (HTML/JS or Python module)
│   └── model_trainer.py        # Script for training the MNIST CNN model
│
├── .gitignore
├── requirements.txt            # TensorFlow, Flask, NumPy, etc.
└── README.md                   # Instructions for running the project

Each folder has a clear purpose:

1. assets/
Contains images for UI, demo, debugging, or documentation.

2. models/
Stores trained model files (.h5).
→ Keeping them separate makes the codebase cleaner and avoids large files being mixed into source code.

3. src/
Main application code:

main.py:	Application entry point (Flask server or GUI launcher).
digit_app.py:	Backend API: receives images, loads model, predicts digit.
drawing_canvas.py:	Canvas logic for drawing digits (frontend or Python).
model_trainer.py:	Trains the MNIST CNN and saves the model.

---

# How It Works

---

# Model Training

## You can retrain the CNN model using MNIST: python src/model_trainer.py

What the model includes:

Convolutional layers
MaxPooling
Dropout
Dense output layer (10 classes)
Accuracy typically > 98%

## Output:

The trained model is saved as: model/digit_model.h5

---

# Technologies Used

Python 3.x
Tkinter (GUI)
TensorFlow / Keras (Deep Learning)
NumPy
Pillow (PIL) for image processing

---

# Screenshots

---

# License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute.
