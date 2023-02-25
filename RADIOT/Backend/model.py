import webbrowser
import os
import pyautogui as at
from datetime import datetime
import random
import pywhatkit
import sys 
from time import gmtime, strftime
from Backend.Speak import Speak
from Backend.Listen import listen
from Backend.Search import GoogleSearch
from Backend.AI_Model import Reply
from Backend.Open import app_open
from Backend.TaskExecution import TasksExecutor
# for i in range(0,8):                                              
#     print(voices[i])
# def chat(query):
 
#     try:
#         mname = 'facebook/blenderbot-400M-distill'
#         model = BlenderbotForConditionalGeneration.from_pretrained(mname)
#         tokenizer = BlenderbotTokenizer.from_pretrained(mname)
#     except:
#         print("No internet")
#         pass
#     inputs = tokenizer([query], return_tensors='pt')
#     reply_ids = model.generate(**inputs)
#     return tokenizer.batch_decode(reply_ids,skip_special_tokens=True)[0]



def playJarvis(voice): 
    reply = TasksExecutor(voice)
    # print(reply)
    if reply is not None:
           
            if 'closing' in reply:
                open.close()
            elif "youtube" in reply:
                reply=reply.replace("youtube", "")
                voice=voice.replace("on youtube", "")
                pywhatkit.playonyt(voice)
                reply= (f"playing {voice} on youtube")
            
            elif "pause" or "countinue" in voice:
                at.press("space")
            elif "fullscreen"  in voice:
                at.press("f")
            elif "mute" in voice:
                at.press("m")
            elif "forward" in voice:
                at.press("arrow right")
            elif "backward" in voice:
                at.press("arrow left")

            elif "opening" in reply:
                  app_open(voice)
            elif  'search' in reply:
                   
                   temp=GoogleSearch(voice, reply)
                   reply = temp
                #  pywhatkit.search(topic)
             
            if 'searching' in reply:
             
                   reply=reply.replace('search', "")
                   voice=voice.replace("tell me", " ")
                   temp=GoogleSearch(voice, reply)
                   Speak(f"{temp}")
    
                
            elif 'time' in reply:
                 strTime =datetime.now().strftime("%H:%M")    
                 #print(f"Sir, the time is {strTime}")
                 reply=reply.replace("time", "")
                 d = datetime.strptime(strTime, "%H:%M")
                 currentTime=d.strftime("%I:%M %p")

                 #print("sir time is "+ d.strftime("%I:%M %p"))
                 reply=f"sir the time is {currentTime}"
                
            elif "volume down" in voice:
                at.press('volumedown')
                at.press('volumedown')
                at.press('volumedown')
                at.press('volumedown')
                at.press('volumedown')
                
            elif "volume up" in voice:
                at.press('volumeup')
                at.press('volumeup')
                at.press('volumeup')
                at.press('volumeup')
                at.press('volumeup')
            elif "mute" in voice:
                at.press("volumemute")
            elif "minimize" in voice or 'minimise' in voice:
                        reply=('Minimizing Sir')
                        at.hotkey('win', 'down','down')
                        at.hotkey('win', 'down','down')

            elif "maximize" in voice or 'maximise' in voice:
                        reply='Maximizing Sir'
                        at.hotkey('win', 'up','up')
          
                       
            elif "screenshot" in voice:
                        reply=("Taking Screenshot sir...")
                        at.hotkey('win','prtsc')
       
            if "paste" in voice:
                        at.hotkey('ctrl','v')
                        reply=("Done Sir!")
            elif "saving" in reply:
                        at.hotkey('ctrl','s')
                        Speak("Sir, tell a name for this file")
                        Savingvoice=listen()
                        at.write(Savingvoice)
                        at.press('enter')
                        reply = "file saved sir."
            elif 'typing' in voice:
                        Speak("Please Tell me what should I Write...")
                        while True:
                            writeIn=listen()
                            if writeIn == 'exit':
                                Speak("Done Sir.")
                                break
                            else:
                                at.write(writeIn)
                 
         
            # return reply 
        
if __name__== "__main__":
    while True:
        query = input(" say :")
        # reply = TasksExecutor(query)
        playJarvis(query) 