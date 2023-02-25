# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# chrome_options.headless = True
# PathofDriver = "Driver\\chromedriver.exe"
# chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic":1})
# chrome_options.add_argument("--mute-audio")
# driver = webdriver.Chrome(PathofDriver,options=chrome_options)
# driver.maximize_window()
# driver.get('https://www.google.com/')

# def SpeechRecognition():
#     try:
#        sleep(1)
#        print(" Listening........ ")
#        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[2]').click()
#        sleep(5)
#        voice = driver.title
#        query = str(voice).replace(" - Google Search","")
#        query = str(query).replace("Google","")
#        sleep(1)
#        driver.get('https://www.google.com/')
#        print(f" You Said : {query}.")
#        return query
#     except:
#         print("")
# if __name__== "__main__":

#     while True:
#         print(SpeechRecognition())
# import speech_recognition as sr
# from googletrans import Translator

# def listen():
#         r = sr.Recognizer()
       
#         with sr.Microphone() as source:
#             r.pause_threshold=1.5
#             audio = r.listen(source)
#             r.adjust_for_ambient_noise(source, duration=0.1)
#             try:
               
                
#                 audiosaid = r.recognize_google(audio,language="en")
                
#             except:
#                 return None
#         return audiosaid

# from googletrans import Translator

# def mar_to_english(text):
#     translator = Translator()
#     result = translator.translate(text, dest='en', src='mr')
#     return result.text


# def Listen():
#     audio = Listen()
#     word = mar_to_english(audio)
#     return word.lower()

# import concurrent.futures

import speech_recognition as sr

# def listen():

#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening....")
#         r.pause_threshold = 0.5
#         audio = r.listen(source,0,2)

#     try:
#         print("Recognizing....")
#         query = r.recognize_google(audio,language="en-in")
#         # print(f" You : {query}")

#     except:
#         return None

#     query = str(query)
#     return query.lower()

import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)  # automatically adjust the microphone sensitivity to the ambient noise level
        audio = r.listen(source, phrase_time_limit=None)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand you.")

    return None

   


if __name__=="__main__":
    while True:
        print(listen())
