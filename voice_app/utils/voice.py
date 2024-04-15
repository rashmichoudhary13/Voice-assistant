import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser
import datetime
import requests
import wolframalpha
import pyautogui
import os

from bs4 import BeautifulSoup
from plyer import notification
from pygame import mixer

running = False

def start_voice_assistant():
    global running
    running = True
    voice_assistant()

#To stop the execution of this script
def stop_voice_assistant():
    global running
    running = False
    # print("running 1: ", running)
    
def voice_assistant():
    global pyautogui  
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 160)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source, 0, 4)
        try:
            print("Understanding..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")
            query_low = query.lower()
            return query_low
        except Exception as e:
            print("Say that again")
            speak("Sorry, Can you say that again.")
            return "None"
        

    def searchGoogle(query):
        if "google" in query:
            query = query.replace("google", "")
            speak("This is what I found on Google")
            try:
                pywhatkit.search(query)
            except:
                speak("No speakable output available")

    def searchYoutube(query):
        if "youtube" in query:
            speak("This is what I found for your search!")
            query = query.replace("youtube", "")
            web = "https://www.youtube.com/" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done, Sir")

    def searchWikipedia(query):
        if "wikipedia" in query:
            speak("Searching from Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)

    def greetMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            # print("Print 1")
            speak("Good Morning, sir")
        elif hour > 12 and hour <= 18:
            # print("Print 2")
            speak("Good Afternoon, sir")
        else:
            # print("Print 3")
            speak("Good Evening, sir")
            
        # print("Print 4")
        speak("Please tell me, How can I help you ?")

    def WolfRamAlpha(query):
        apikey = "VQRRYV-WJ8UL76UQL"  # Replace "YOUR_API_KEY_HERE" with your actual API key
        requester = wolframalpha.Client(apikey)
        requested = requester.query(query)

        try:
            answer = next(requested.results).text
            return answer
        except StopIteration:
            return "Sorry, I couldn't find the answer."

    def Calc(query):
        Term = str(query)
        Term = Term.lower()  # Convert the query to lowercase for case insensitivity
        Term = Term.replace("jarvis", "")
        Term = Term.replace("multiply", "*")
        Term = Term.replace("plus", "+")
        Term = Term.replace("minus", "-")
        Term = Term.replace("divide", "/")

        try:
            result = WolfRamAlpha(Term)
            print(result)
            speak(result)
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I encountered an error while processing your request.")

   
    while running:
        # print("running 3: ", running)
        speak("Hi I am Serena your Voice Assistant")
        greetMe()
        while running:
                # print("running 4: ", running)
                query = takeCommand()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("That's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("You are welcome, sir")
                elif "what can you do" in query:
                    speak("I can do most of the things Such as, I can open apps, can do arithmetic operation, can search anything for you on google and youtube. I can also control volume.")
                elif "that's all" in query:
                    speak("I can also schedule your important meetings and all and can also click your photo.")
                elif "who made you" in query:
                    speak("I was created by Rashmi, Aryan and Pranjal.")
                elif "what modules do you use" in query:
                    speak("Modules that I use are pyttsx3, speech_recognition, pywhatkit, wikipedia, webbrowser, datetime, requests, wolframalpha, bs4 (BeautifulSoup), os, pyautogui, plyer, pygame")
                            
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from .keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from .keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                
                elif "open" in query:
                    from .Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from .Dictapp import closeappweb
                    closeappweb(query)

                
                elif "remember that " in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = rememberMessage.replace("jarvis", "")  # Corrected this line
                    speak("You told me to " + rememberMessage)  # Added space after 'to'
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage + "\n")  # Added a newline after each message
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to " + remember.read())  # Added space after 'to'
                    remember.close()

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                     speak("Screenshot taken")

                elif "click my photo" in query or "take a picture" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(5)
                        speak("SMILE")
                        pyautogui.press("enter")

                elif 'type' in query:
                    query = query.replace("type","")
                    pyautogui.typewrite(f"{query}",0.1)

                elif "temperature" in query or "weather" in query:
                    query = query.replace("temperature","")
                    query = query.replace("weather","")
                    api_key = '4d8f68f3a047a69766809f45bf6cebba'
                    url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric"
                    weather_data = requests.get(url)
                    
                    if weather_data.json()['cod'] == '404':
                        speak("No City Found")
                    else:
                        weather = weather_data.json()['weather'][0]['main']
                        temp = round(weather_data.json()['main']['temp'])

                        speak(f"The weather in {query} is: {weather}")
                        speak(f"The temperature in {query} is: {temp}ºF")
                        
                elif "what's the time now" in query or "tell me the time" in query :
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                    
                elif "calculate" in query:
                    
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    elif shutdown == "no":
                        break

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                        speak("opening your schedule")
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("static/notification.mp3.wav")
                        mixer.music.play()
                        notification.notify(
                            title = "My schedule :-",
                            message = content,
                            timeout = 15
                            )
                elif "sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                    

                else:
                    searchGoogle(query)
                    searchYoutube(query)
                    searchWikipedia(query)


if __name__ == "__main__":
    if running:
        voice_assistant()

 