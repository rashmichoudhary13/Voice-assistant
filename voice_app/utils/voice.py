import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser
import datetime
import requests
from bs4 import BeautifulSoup

running = False

def start_voice_assistant():
    global running
    running = True
    voice_assistant() 

#To stop the execution of this script
def stop_voice_assistant():
    global running
    running = False
    print("running 1: ", running)
    
def voice_assistant():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 170)

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
            return query.lower()
        except Exception as e:
            print("Say that again")
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
            web = "https://www.youtube.com/results?search_query=" + query
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

    while running:
        print("running 3: ", running)
        query = takeCommand()
        if "hello" in query:
            speak("Yes sir, How can I assist you?")
            while running:
                print("running 4: ", running)
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

                elif "temperature" in query:
                    search = "temperature in Mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in Mumbai "
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                else:
                    searchGoogle(query)
                    searchYoutube(query)
                    searchWikipedia(query)


if __name__ == "__main__":
    if running:
        voice_assistant()

