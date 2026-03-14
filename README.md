# Sign Language Recognition System

**Author:** Abhinav Shrivastav  
**Tech Stack:** Python | OpenCV | MediaPipe | PyDuino  
**Accuracy:** ~95% gesture recognition

---

## 🎯 Project Overview

A real-time sign language recognition system that detects hand gestures using a webcam and maps them to letters/words using computer vision. Built using OpenCV for video capture and MediaPipe for 21-point hand landmark detection.

---

## 🚀 Features

- Real-time hand detection and tracking
- 15+ gesture/sign recognition
- Gesture stabilization using history smoothing
- Live finger state display (Thumb, Index, Middle, Ring, Pinky)
- Color-coded bounding box (green = known, orange = unknown)
- Clean UI overlay with gesture name display

---

## 🛠️ Tech Stack

| Technology | Purpose                                        |
| ---------- | ---------------------------------------------- |
| Python 3.x | Core language                                  |
| OpenCV     | Webcam capture, frame processing, UI rendering |
| MediaPipe  | 21-point hand landmark detection               |
| PyDuino    | Hardware integration (robotic control)         |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/abhinavshrivastavgit/sign-language-recognition

# Install dependencies
pip install opencv-python mediapipe

# Run the project
python main.py
```

---

## 🖥️ How It Works

```
Webcam Feed
    ↓
OpenCV captures frame
    ↓
MediaPipe detects 21 hand landmarks
    ↓
gestures.py analyzes finger states
    ↓
Gesture matched to sign/letter
    ↓
Result displayed on screen
```

---

## 🤌 Supported Gestures

| Gesture       | Recognition |
| ------------- | ----------- |
| Pointing (D)  | ✅          |
| Peace / V     | ✅          |
| Open Hand (5) | ✅          |
| Fist (A/S)    | ✅          |
| Thumb Up      | ✅          |
| Pinky (I)     | ✅          |
| ILY Sign      | ✅          |
| Rock On       | ✅          |
| L Shape / Gun | ✅          |
| + 6 more      | ✅          |

---

## 📊 Performance

- Gesture accuracy: **~95%** on supported signs
- Frame processing: Real-time (30fps+)
- Stability: 10-frame history smoothing for consistent output

---

## 🔮 Future Improvements

- Add full ASL alphabet (A-Z)
- Word formation from consecutive gestures
- PyDuino hardware integration for robotic arm control
- Dataset training with custom ML model

---

## 👤 Author

**Abhinav Shrivastav**  
B.Tech CSE (AI & ML) | Haldia Institute of Technology  
GitHub: github.com/abhinavshrivastavgit  
LinkedIn: linkedin.com/in/abhinavshrivastav-no1
