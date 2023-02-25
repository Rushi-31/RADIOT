import pyttsx3

language = 'en'

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 150)

engine.setProperty('volume', 1)


voices = engine.getProperty('voices')


engine.setProperty('voice', voices[3].id)
# for i in range(0,7):
#     print(voices[i])

def Speak(text):
    
    engine.say(text)
    engine.runAndWait()
    return text

if __name__ =="__main__":
    Speak("I am radiot")