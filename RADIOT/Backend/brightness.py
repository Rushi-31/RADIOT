import screen_brightness_control as sbc



# Adjust the screen brightness based on recognized speech
def adjust_brightness(text):
        # print("Say 'set brightness to <value>' or 'increase/decrease brightness by <value>' to adjust screen brightness...")
       
            words = text.split()
            if  words[0] == "set" and words[1] == "brightness" and words[2] == "to":
                brightness = int(words[3])
                sbc.set_brightness(brightness)
                print("Brightness set to", brightness)
            elif len(words) ==4 and (words[0] == "increase" or words[0] == "decrease") and words[1] == "brightness" and words[2] == "by":
                value = int(words[3])
                if words[0] == "increase":
                    sbc.increase_brightness(value)
                else:
                    sbc.decrease_brightness(value)
                print("Brightness adjusted by", value)
            else:
                print("Sorry, I didn't understand that.")
    
adjust_brightness("set brightness to 80")

