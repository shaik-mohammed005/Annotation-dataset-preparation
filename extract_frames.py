import cv2
import os

video_path = "video.mp4"

output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % 10 == 0:
        frame_name = os.path.join(output_folder, f"frame_{saved_count}.jpg")
        cv2.imwrite(frame_name, frame)
        saved_count += 1

    frame_count += 1

cap.release()

print(f"Done Extracted {saved_count} frames")
