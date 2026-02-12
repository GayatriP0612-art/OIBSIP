import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit  # For YouTube/play commands (optional)

engine = pyttsx3.init()
# Optional: Customize voice (female/male, rate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index for different voice
engine.setProperty('rate', 170)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300  # Adjust if needed: lower for quiet voices (e.g., 200), higher for noise (e.g., 500)
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Increased duration for better noise calibration
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)  # Increased timeouts to prevent early cutoffs
            query = r.recognize_google(audio, language='en-IN')  # Good for Indian English
            print(f"You said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            speak("Listening timed out. Please speak sooner or check your microphone.")
            return ""  # Retry on next loop
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return ""
        except sr.RequestError:
            speak("Network issue. Please check your connection.")
            return ""
        except Exception as e:  # Catch other audio errors
            speak(f"An error occurred: {str(e)}")
            return ""

speak("Hello! I'm your voice assistant. How can I help?")

while True:
    query = listen()
    if not query:
        continue

    if "hello" in query or "hi" in query:
        speak("Hello! Great to hear from you.")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {current_date}")
    elif "wikipedia" in query or "who is" in query or "what is" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "").replace("who is", "").replace("what is", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        except:
            speak("Sorry, I couldn't find that on Wikipedia.")
    elif "search" in query or "google" in query:
        query = query.replace("search", "").replace("google", "")
        speak(f"Searching the web for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "youtube" in query:
        query = query.replace("play", "").replace("youtube", "")
        speak(f"Playing {query} on YouTube")
        pywhatkit.playonyt(query)
    elif "exit" in query or "stop" in query or "bye" in query:
        speak("Goodbye! Have a great day.")
        break
    else:
        speak("I'm not sure how to help with that yet. Try asking for time, date, or a search.")