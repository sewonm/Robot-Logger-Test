import cv2
import time
import os 

os.makedirs("images", exist_ok = True)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    timestamp = time.time()
    filename = f"images/frame_{timestamp:.3f}.jpg"
    cv2.imwrite(filename, frame)

    print(f"Saved {filename}")
    time.sleep(0.5)

cap.release()