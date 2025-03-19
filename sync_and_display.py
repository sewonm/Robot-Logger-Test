import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
from PIL import Image

# === 1. Load Accelerometer and Gyroscope CSVs ===
accel_df = pd.read_csv("Accelerometer.csv")
gyro_df = pd.read_csv("Gyroscope.csv")

# Keep only necessary columns and rename for clarity
accel_df = accel_df.rename(columns={
    "timestamp": "time",
    accel_df.columns[1]: "accel_x",
    accel_df.columns[2]: "accel_y",
    accel_df.columns[3]: "accel_z"
})

gyro_df = gyro_df.rename(columns={
    "timestamp": "time",
    gyro_df.columns[1]: "gyro_x",
    gyro_df.columns[2]: "gyro_y",
    gyro_df.columns[3]: "gyro_z"
})

# === 2. Merge IMU data by timestamp ===
imu_df = pd.merge_asof(
    accel_df.sort_values("time"),
    gyro_df.sort_values("time"),
    on="time",
    direction="nearest"
)

# === 3. Load image files and extract timestamps ===
image_files = sorted(glob.glob("images/frame_*.jpg"))
image_timestamps = [float(f.split("_")[-1][:-4]) for f in image_files]  # remove '.jpg'
# Get min and max IMU times
imu_start = imu_df['time'].min()
imu_end = imu_df['time'].max()

# Filter only images that fall within IMU time range
filtered_images = []
filtered_timestamps = []

for img_path, img_time in zip(filtered_images, filtered_timestamps):
    if imu_start <= t <= imu_end:
        filtered_images.append(f)
        filtered_timestamps.append(t)

print(f"Using {len(filtered_images)} images within IMU range.")

# === 4. For each image, find closest IMU reading and display both ===
for img_path, img_time in zip(image_files, image_timestamps):
    # Find closest row in IMU
    closest_row = imu_df.iloc[(imu_df['time'] - img_time).abs().argsort()[:1]]
    print(f"Image time: {img_time}, Closest IMU time: {closest_row['time'].values[0]}")

    # Load image
    img = Image.open(img_path)

    # Plot
    plt.figure(figsize=(6, 4))
    plt.imshow(img)
    plt.axis('off')

    # Print IMU data
    row = closest_row.iloc[0]
    imu_text = f"""
    accel: ({row['accel_x']:.2f}, {row['accel_y']:.2f}, {row['accel_z']:.2f})
    gyro:  ({row['gyro_x']:.2f}, {row['gyro_y']:.2f}, {row['gyro_z']:.2f})
    """
    plt.title(f"{os.path.basename(img_path)}\n{imu_text}")
    plt.tight_layout()
    plt.show()