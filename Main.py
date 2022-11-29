import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyfiglet
from selenium import webdriver

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    en_voice_id = "english-us"
    id_voice_id = "indonesian"
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 129)
    for voice in voices:
        voices = engine.setProperty('voice', en_voice_id)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M")
    print(Time)
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = datetime.datetime.now()
    day = datetime.datetime.now()
    speak("the current date is")
    speak(day.strftime("%A"))
    speak(month.strftime("%B"))
    speak(year)
    print(year, month.strftime("%B"), day.strftime("%A"))

def searchGoogle(link):
    driver = webdriver.Firefox()
    speak("open the Firefox")
    driver.get("https://www.google.com/")
    searchInput = driver.find_element("class name", "gLFyf")
    searchInput.send_keys(link)
    searchInput.submit()
    speak("This is what i found")

def wishme():
    ascii_banner = pyfiglet.figlet_format("JARVIS Assistent")
    print(ascii_banner)
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!")
        print("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good afternoon. Sir")
        print("Good Afternoon")
    elif hour >= 18 and hour<24:
        speak("Good Evening Sir!")
        print("Good Evening")
    else:
        speak("Good Night Sir!")
        print("Good Night")
    speak("Welcome back")
    speak("can i help you sir?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Can you say that again please?")

        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'are you jarvis' in query:
            speak("yes sir, i am here for you")
        elif 'who are you' in query:
            speak("i am a jarvis sir!")
        elif 'who am i' in query:
            speak("You Are Iyad Rozan")

        elif 'search in google' in query:
            speak("What should i search?")
            link = takeCommand().lower()
            print(link)
            searchGoogle(link)

        elif 'search on wikipedia' in query:
            speak("Searching...")
            query = query.replace("search on wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'offline' in query:
            quit()