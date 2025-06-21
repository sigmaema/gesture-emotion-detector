import cv2
from Detectors.hands import detect_gesture
from Actions.gesture_actions import handle_gesture
import time
from deepface import DeepFace
import webbrowser

CAMERA_INDEX = 0
cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("Kameru se nepodařilo otevřít.")
    exit()

last_gesture = None
last_gesture_time = 0
last_emotion = None
last_emotion_time = 0
COOLDOWN_SECONDS = 1

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gesture = detect_gesture(frame, draw=True)
    current_time = time.time()

    if gesture and gesture != last_gesture:
        if current_time - last_gesture_time > COOLDOWN_SECONDS:
            handle_gesture(gesture)
            last_gesture = gesture
            last_gesture_time = current_time
    elif not gesture:
        last_gesture = None
    
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        current_emotion = result[0]['dominant_emotion']
        current_time = time.time()

        if current_emotion != last_emotion and (current_time - last_emotion_time) > COOLDOWN_SECONDS:
            print(f"Emoce: {last_emotion} → {current_emotion}")
            last_emotion = current_emotion
            last_emotion_time = current_time
            match current_emotion:
                case "happy":
                    webbrowser.open("https://youtube.com/playlist?list=PLCHyxBVZeL3Or-VsbHsH7Md8Kz96FKinS&si=XUgokmvWZSCLRgns")
                case "angry":
                    exit()
                case "neutral":
                    continue
                case "sad":
                    continue
                case _:
                    print("Nepodařilo se rozpoznat emoci")
                    continue

    except Exception as e:
        print("Nepodařilo se analyzovat:", e)

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
