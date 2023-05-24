import cv2
import time
import os

output_directory = r"E:\Projects\face_recognizer\training\Preetha"
duration = 5  # Duration in seconds

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

video = cv2.VideoCapture(0)  # Use index 0 for the default webcam

start_time = time.time()
end_time = start_time + duration

success = True
count = 1

while success and time.time() < end_time:
    success, frame = video.read()
    name = os.path.join(output_directory, f"frame_{count}.jpg")

    if success:
        cv2.imwrite(name, frame)
        print(f"Frame {count} Extracted Successfully")
        count += 1
    else:
        break

video.release()
