import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    try:
        print("No error")
        engine.say(audio)
        engine.runAndWait()
       
    except Exception as e:
        print("An error occurred during speech synthesis:", e)

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        print("Print 1")
        speak("Good Morning, sir")
    elif hour > 12 and hour <= 18:
        print("Print 2")
        speak("Good Afternoon, sir")
    else:
        print("Print 3")
        speak("Good Evening, sir")
        
    print("Print 4")
    speak("Please tell me, How can I help you ?")