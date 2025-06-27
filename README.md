# 🎯 Color Detection and Object Tracking using OpenCV

This project performs real-time color detection and tracking from a **video file** using the **HSV color space** and **OpenCV**. It identifies objects of specific colors (like blue, yellow, or azure) and draws their positions across frames, creating a visual trail of their motion.

---

## 📸 Demo

*(Insert GIF or screenshot here showing the tracking working on a video)*

---

## 🧠 Features

- Detects and tracks colored objects in a video
- Uses HSV color filtering for accurate detection
- Tracks multiple colors (you can customize them)
- Draws the path of the object over time

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- NumPy

---

## 🎨 Color Ranges in HSV

| Color  | HSV Lower            | HSV Upper            |
|--------|----------------------|----------------------|
| Blue   | `[100, 150, 0]`      | `[140, 255, 255]`    |
| Yellow | `[22, 93, 0]`        | `[45, 255, 255]`     |
| Azure  | `[80, 100, 100]`     | `[100, 255, 255]`    |

You can change these colors from the `myColors` list inside the code.

---

## ▶️ Run the Project

1. افتح المجلد اللي فيه المشروع.
2. افتح التيرمنال (أو Anaconda Prompt) واكتب:

```bash
pip install opencv-python numpy
