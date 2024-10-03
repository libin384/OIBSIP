import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import speech_recognition as sr
import time
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Silvi")
    speak("I am your Assistant")
    speak(assname)




def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=10)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

def username():
    speak("What should i call you sir")
    username = takeCommand()
    speak("Welcome Mister")
    speak(username)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", username.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")






def set_reminder(reminder, duration_minutes):
    """Set a reminder after a specific duration in minutes."""
    reminder_time = datetime.now() + datetime.timedelta(minutes=duration_minutes)
    speak(f"Reminder set for {reminder} in {duration_minutes} minutes.")
    print(f"Reminder set for {reminder_time.strftime('%H:%M:%S')}")

    # Wait for the reminder time
    while datetime.now() < reminder_time:
        time.sleep(1)

    # Alert the user
    speak(f"Reminder: {reminder}")

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command


        if 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("www.stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open opera' in query:
            codePath = r"C:\\Users\\LIBIN\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath)

        elif 'reminder' in query:
            speak("What would you like to set a reminder for?")
            reminder = takeCommand()

            if reminder:
                speak("In how many minutes?")
                time_input = takeCommand()

                try:
                    duration_minutes = int(time_input)
                    set_reminder(reminder, duration_minutes)
                except ValueError:
                    speak("Sorry, I couldn't understand the time duration.")
            else:
                speak("I didn't get the reminder task.")


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Libin")

        elif 'joke' in query:
            speak(pyjokes.get_joke())



        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Libin. further It's a secret")

        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\Users\TECHWORLD\Downloads\pp1 (1).pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Libin")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Libin ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
            speak("Background changed successfully")


        elif 'news' in query:

            try:
                jsonObj = urlopen(
                    '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Silvi from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Silvi Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("Silvi.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "Silvi" in query:

            wishMe()
            speak("Silvi 1 point o in your service Mister")
            speak(assname)


        elif "weather" in query:

            api_key = "a611d1d1ffafdd662242db723143ef81"

            base_url = "http://api.openweathermap.org/data/2.5/weather?q="

            speak("Please tell me the city name.")

            print("City name: ")

            city_name = takeCommand()  # Assumes takeCommand() is a function to get user input

            complete_url = base_url + city_name + "&appid=" + api_key

            try:

                # Request weather data from the API

                response = requests.get(complete_url)

                x = response.json()

                # Safely checking if 'cod' key exists and its value is not "404" (correct key for the response code is "cod")

                if x.get("cod") != "404":

                    # Access nested data safely

                    y = x.get("main", {})

                    current_temperature = y.get("temp", "N/A")

                    current_pressure = y.get("pressure", "N/A")

                    current_humidity = y.get("humidity", "N/A")

                    # Access weather description

                    z = x.get("weather", [{}])

                    weather_description = z[0].get("description", "No description available")

                    # Display weather information

                    print(

                        f"Temperature (in kelvin unit) = {current_temperature}\n"


                        f"Atmospheric pressure (in hPa unit) = {current_pressure}\n"


                        f"Humidity (in percentage) = {current_humidity}\n"


                        f"Description = {weather_description}"

                    )

                    # Optional: Speak out the weather details if your system supports it

                    speak(f"The current temperature is {current_temperature} kelvin, "

                          f"atmospheric pressure is {current_pressure} hPa, "

                          f"humidity is {current_humidity} percent, "

                          f"and the weather is described as {weather_description}.")

                else:

                    # City not found error handling

                    speak("City not found. Please check the city name and try again.")

            except requests.exceptions.RequestException as e:

                # Handle exceptions related to network or request issues

                print(f"Error fetching data: {e}")

                speak("There was an error fetching the weather data. Please try again later.")


        elif "send message " in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )

            print(message.sid)


        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")


    # elif "" in query:
    # Command go here
    # For adding more commands

