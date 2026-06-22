# Finger Counter

A Python webcam application that detects one hand and displays the number of raised fingers in real time.

It uses OpenCV for camera/video display and MediaPipe for hand landmark detection.

## Requirements

- Python 3.10 or newer
- A working webcam

## Setup

From the project folder, create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Run the app

```powershell
python main.py
```

The camera window shows the detected hand landmarks and the current finger count. Press `Esc` to close the application.

## Project files

- `main.py` — opens the webcam and counts raised fingers.
- `hand_detector.py` — detects the hand and extracts landmark positions.
- `requirements.txt` — project dependencies.
- `test.py` — small MediaPipe import test.

## Notes

The current app tracks one hand. For the clearest results, keep the hand visible to the camera with reasonable lighting.
