from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
PathofDriver = "Driver\\chromedriver.exe"
driver = webdriver.Chrome(PathofDriver, options=chrome_options)
driver.maximize_window()

Website = f'https://ttsmp3.com/text-to-speech/British%20English/'

driver.get(Website)
ButtonSelection = Select(driver.find_element(
    by=By.XPATH, value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Emma')


def Speak(Text):
    lengthoftext = len(str(Text))
    if lengthoftext == 0:
        pass
    else:
        # print("")
        # print(f" AI : {Text}")
        # print("")
        Data = str(Text)
        xpathtec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(by=By.XPATH, value=xpathtec).send_keys(Data)
        # driver.find_element(by=By.XPATH, value=xpathtec).send_keys(f'<prosody rate="fast"> {Data} </prosody>')
        driver.find_element(
            by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
        driver.find_element(
            by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
        if lengthoftext >= 30:
            sleep(4)
        elif lengthoftext >= 40:
            sleep(6)
        elif lengthoftext >= 55:
            sleep(8)
        elif lengthoftext >= 70:
            sleep(10)
        elif lengthoftext >= 100:
            sleep(13)
        elif lengthoftext >= 120:
            sleep(14)
        else:
            sleep(2)


if __name__ == "__main__":
    Speak('welcome back sir.')
