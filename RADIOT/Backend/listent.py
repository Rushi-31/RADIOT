import speech_recognition as sr
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Speak now...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='en-in')
            print(f"You said: {text}")
            return text.lower()
        except:
           return None

while True:
    listen()