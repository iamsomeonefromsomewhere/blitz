import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import random
import pywhatkit
import requests

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("someone at your service sir, please tell me how may I help you.")
    print("someone at your service sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("./ss/ss.png")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()
        
        elif 'hello' in query:
            speak("good morning")
        
        elif "blitz" in query:
            speak("blitz")

        elif "who are you" in query:
            speak("I'm someone a desktop voice assistant.")
            print("I'm someone a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "tell me about" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("tell me about","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
        
        elif "alarm" in query:
            speak("enter the time")
            time = input("Enter the time:")
            speak(f"alarm set for {time}")
            while True:
                time_now=datetime.datetime.now()
                now = time_now.strftime("%H:%M:%S")
                if now == time:
                    speak("Time to wake up sir")
                    break
        elif "weather" in query:
            api_key = "a489106d98db3ccfac1ab48dbd82f83b"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = "Pokhara"
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            y = x["main"]
            z = x["wind"]
            temperature = round((y["temp"] - 273.15), 2)
            wind_speed = z["speed"]
            speak("Temperature in " + city_name + " is " + str(temperature) + "°C.")
            speak("Wind speed in " + city_name + " is " + str(wind_speed) + "meter per second")

        elif "offline" in query:
            speak("bye bye")
            quit()