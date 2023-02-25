print(">> Loading R. A. D. I. O. T. ")
print(">>please wait for few seconds")
from Backend import Speak as s
from Backend import model as m
from Backend import Listen as l
from Backend import Open
from Backend import AI_Model as ai
from Backend.Search import GoogleSearch

import sys

def run_assistant():
        # s.Speak("At your service sir.")
       
            # try:
                        # # time = GoogleSearch("current time", "time")
                        # weather = GoogleSearch("weather in pune is good or not", "weather")
                        # temperature = GoogleSearch("temprature in pune", "temprature")

                        # s.Speak(f"welcome back sir. it's {time} .  {weather}")
                        while True:
                            cmd = l.listen()
                            if cmd is not None:
                                reply = ai.Reply(cmd)
                                m.playJarvis(cmd)
                                # querry=m.playJarvis(voice=cmd, reply=reply)
                                s.Speak(reply)
                                # 

            # except:

                       # continue
run_assistant()

