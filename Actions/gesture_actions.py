import pyautogui
import os
import subprocess
import signal
import webbrowser

def send_key(key):
    script = f'tell application "System Events" to key code {fkey_to_code(key)}'
    print(f"Key pressed {key}")
    subprocess.run(["osascript", "-e", script])
    print(f"Success")


def open_app(app_name):
    subprocess.Popen(["open", "-a", app_name])

def fkey_to_code(fkey):
    mapping = {
        "f1": 122, "f2": 120, "f3": 99, "f4": 118, "f5": 96,
        "f6": 97, "f7": 98, "f8": 100, "f9": 101, "f10": 109,
        "f11": 103, "f12": 111
    }
    return mapping.get(fkey.lower(), 100)

def stop_program():
    print("Ukončuji program...")
    os.kill(os.getpid(), signal.SIGTERM)

def handle_gesture(gesture):
    print(f"Gesto rozpoznáno: {gesture}")

    match gesture:
        case "1_fingers":
            webbrowser.open("https://youtube.com")
        case "2_fingers":
            webbrowser.open("https://github.com")
        case "3_fingers":
            open_app("Spotify")
        case "4_fingers":
            open_app("Microsoft OneNote")
        case "5_fingers":
            stop_program()
        case "thumb_down":
            webbrowser.open("https://chatgpt.com")
        case _:
            print("Gesto nerozpoznáno nebo nepodporováno.")
