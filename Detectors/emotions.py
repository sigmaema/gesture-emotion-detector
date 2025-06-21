from deepface import DeepFace
import cv2
import time
import webbrowser
import os
import signal
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kameru se nepodařilo otevřít.")
    exit()

last_emotion = None
last_emotion_time = 0
COOLDOWN_SECONDS = 2 

while True:
    ret, frame = cap.read()
    if not ret:
        break

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
                    webbrowser.open("https://open.spotify.com/playlist/5ucUMpNF7h9IshksCSvtqu?si=6a5e00caef534bbb")
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
