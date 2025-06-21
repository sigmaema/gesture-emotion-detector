# Emotion & Gesture Controlled Assistant

This project is a camera-based assistant that reacts to your facial emotions and hand gestures in real time. Designed and tested on macOS.

## Features

- **Real-time emotion recognition** using `DeepFace`
- **Hand gesture detection** powered by `MediaPipe`
- Automatic response to:
  - Emotions (e.g. open music/video links or quit apps)
  - Gestures (e.g. simulate keyboard shortcuts, launch apps or kill programs)
- **Cooldown handling** to avoid action spamming
- Modular action system (easy to customize)

## 🛠️ Tech Stack

| Area         | Library/Tool        |
|--------------|---------------------|
| Emotion AI   | `deepface`          |
| Camera input | `opencv-python`     |
| Gestures     | `mediapipe`         |
| Automation   | `webbrowser`, `os`, `pyautogui`, `pynput`, `subprocess`
| Platform     | macOS (Apple Silicon tested)


