# 🎯 Color Detection and Object Tracking using OpenCV

This project performs real-time color detection and tracking from a **video file** using the **HSV color space** and **OpenCV**. It identifies objects of specific colors (like blue, yellow, or azure) and draws their paths across frames, creating a visual trail of their motion.

---

## 📸 Demo

https://github.com/yourusername/color-tracking/assets/demo.gif *(Add a screen recording or GIF here if possible)*

---

## 🧠 Features

- Detects and tracks colored objects in video (supports multiple colors)
- Uses HSV color thresholds for reliable detection
- Marks and traces object positions over time
- Adjustable HSV ranges for custom colors

---

## 🛠 Technologies Used

- Python 3.x
- OpenCV
- NumPy

---

## 🎨 HSV Color Ranges Used

| Color  | HSV Lower            | HSV Upper            |
|--------|----------------------|----------------------|
| Blue   | `[100, 150, 0]`      | `[140, 255, 255]`    |
| Yellow | `[22, 93, 0]`        | `[45, 255, 255]`     |
| Azure  | `[80, 100, 100]`     | `[100, 255, 255]`    |

You can tweak these in the `myColors` list.

---

## 🧪 How It Works

1. The video is read frame-by-frame.
2. Each frame is converted to HSV color space.
3. A mask is created for each color using its HSV range.
4. The largest contour of each mask is located.
5. A colored circle is drawn on the detected position.
6. The positions are stored and redrawn across frames to track movement.

---

## 📂 File Structure

