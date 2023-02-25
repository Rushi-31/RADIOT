import wikipedia
import pyautogui as at
from functools import cache
import pywhatkit
import requests
from bs4 import BeautifulSoup
import sys
def GoogleSearch(voice,reply):
                # try:
                    
                    
                #     voice = voice.replace("wikipedia", "")
                #     results = wikipedia.summary(voice, sentences=1)
                #     return results

                # except:
                    search =  voice
                    # search= topic.replace('google', '')
                    
                    url =f"https://www.google.com/search?q={search}"
                    r  = requests.get(url) 
                    data= BeautifulSoup(r.text, "html.parser")
                    results = data.find("div", class_ = "BNeawe").text
                    return results
