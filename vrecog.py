import speech_recognition as sr
import requests, json
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from gtts import gTTS
import os
from playsound import playsound
from datetime import datetime
import pyjokes
def bolna(s):
    language='en'
    myobj = gTTS(text=s,lang=language,slow=False)
    myobj.save("temp.mp3")
    playsound('temp.mp3')
    os.remove("temp.mp3")
def speaking():
    while(1):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Give me a Command!")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            sp=r.recognize_google(audio)
            break
        except sr.UnknownValueError:
            print("Gideon could not understand audio, Please speak again")
            continue
        except sr.RequestError as e:
            print("Gideon error; {0}".format(e))
            continue
    return sp
def weather():
    str1="which city?"
    bolna(str1)
    city=speaking()
    url='https://www.google.com/search?q=weather+'+str(city)+''
    op=webdriver.ChromeOptions();
    op.add_argument('headless');
    driver=webdriver.Chrome(options=op)
    driver.get(url)
    w=driver.find_element_by_xpath('//*[@id="wob_tm"]').text
    w+="°C"
    f="weather in "+str(city)+" is "+str(w)
    bolna(f)
def telltime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bolna(current_time)
def joke():
    My_joke = pyjokes.get_joke(language="en", category="neutral")
    bolna(My_joke)
while(1):
    a=""
    a=speaking()
    if("weather" in a):
        weather()
        break
    if("time" in a):
        telltime()
    if("joke" in a):
        joke()

