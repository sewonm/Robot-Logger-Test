# Robot Logger: Webcam + IMU Data Sync

This project captures synchronized real-world multimodal data using a webcam and a phone's built-in IMU (Inertial Measurement Unit).

### 🎯 What It Does
- Records timestamped images using your laptop webcam
- Logs accelerometer + gyroscope data from your smartphone (via SensorLog or Phyphox)
- Syncs the data using timestamps and displays each image with its corresponding motion data

### 🛠 How to Use

#### 1. Set up virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install opencv-python pandas matplotlib pillow