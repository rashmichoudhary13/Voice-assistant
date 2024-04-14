import wolframalpha
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

# Sample usage
if __name__ == "__main__":
    query = input("Enter your query: ")
    Calc(query)
