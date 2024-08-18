# AttendanceTracker-with-Face-Recognition
# Face Recognition Attendance Tracker

This project is an automated attendance tracking system that uses face recognition technology. It captures video from a webcam, detects faces, matches them against a known dataset, and records attendance in a CSV file.

## Features

- Real-time face detection and recognition
- Attendance logging with timestamp and date
- Visual feedback with bounding boxes and names displayed on video feed
- CSV-based attendance record keeping

## Output:
![WhatsApp Image 2024-08-19 at 00 12 58_180e1e6f](https://github.com/user-attachments/assets/00cafd38-2da7-4141-8870-e7912d6513ac)

## Requirements

- Python 3.12
- OpenCV (cv2)
- NumPy
- face_recognition
- A webcam

## Installation

1. Clone this repository:
```git clone https://github.com/yourusername/face-recognition-attendance.git```
2. Install the required packages:
```pip install opencv-python numpy face_recognition```

## Usage

1. Add images of known individuals to the `images` folder. Name each image file with the person's name (e.g., "John_Doe.jpg").

2. Run the script:
```python attendance_tracker.py```
3. The system will start capturing video from your webcam. Known faces will be recognized, highlighted with a green box, and their names will be displayed.

4. Attendance will be automatically logged in `attendance.csv` with the name, time, and date.

5. Press 'q' to quit the application.

## How it works

1. The script loads known face images from the `images` folder.
2. It encodes the facial features of known individuals.
3. The webcam feed is processed in real-time to detect faces.
4. Detected faces are compared against the known face encodings.
5. If a match is found, the person's name is displayed on the video feed and logged in the attendance file.

## Customization

- Adjust the `path` variable to change the location of known face images.
- Modify the `markAttendance` function to change the format of the attendance log.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

