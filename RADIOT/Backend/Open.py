import os
import pyautogui as at 
from time import sleep

def app_open(query):
    query=query.replace("open","")
    query=query.replace("launch","")
    reply=f"openning {query} sir"
    query = query[0:4]
    at.press('win')
    sleep(0.2)
    at.write(query)
    sleep(0.3)
    at.press("enter")
    return reply

def close():
    at.hotkey("ctrl","w")

if __name__ == "__main__":
    app_open("")