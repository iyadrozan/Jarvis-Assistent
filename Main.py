import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    en_voice_id = "english-us"
    id_voice_id = "indonesian"
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 126)
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

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!")
        print("Morning")
    elif hour >=12 and hour<18:
        speak("Good afternoon. Sir")
        print("Afternoon")
    elif hour >= 18 and hour<24:
        speak("Good Evening Sir!")
        print("Evening")
    else:
        speak("Good Night Sir!")
        print("Night")
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
        elif 'who am i' in query:
            speak("Iyad Rozan My BOSS")
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'offline' in query:
            quit()