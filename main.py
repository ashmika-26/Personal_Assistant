import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import pywhatkit
import randfacts
import pyjokes
import requests
import ss
#from Riddles.riddle import riddle

print("INITIALISING V.A.M.A ...." )

master = "Ash"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!" + master)
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!" +master)
    else:
        speak("Good evening!" +master)
    speak("My name is Vaaama ,How may I help you?")

def giveCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source)

    try :
        print("Recognising...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please")
        query = None
    return query

def news():

    api_address = "https://newsapi.org/v2/top-headlines?language=en&apiKey="+ss.key
    res = requests.get(api_address).json()
    arr = []
    for i in range(5):
        arr.append("Number "+str(i+1)+" "+res["articles"][i]["title"]+".")
    return arr

wish()

def run_vama():
    query = giveCommand()

    if query is None:
        speak("I didn't catch that")

    elif "wikipedia" in query.lower():
        try:
            speak("Searching wikipedia...")
            query = query.lower().replace("wikipedia","")
            results = wikipedia.summary(query,sentences= 2)
            print(results)
            speak(results)
        except Exception as e:
            speak("I'm sorry, I did not find anything about this")

    elif "how are you" in query.lower():
        speak("I'm having a good day,thanks for asking.")


    elif "news" in query.lower():
        arr = news()
        for y in range(len(arr)):
            print(arr[y])
            speak(arr[y])

    elif "open youtube" in query.lower() or "youtube" in query.lower():
        speak("Ok, opening youtube")
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "youtube.com"
        webbrowser.get(chrome_path).open(url)
        exit(-1)

    elif "fact" in query.lower() or "something new" in query.lower():
        x = randfacts.get_fact()
        print(x)
        speak("Did you know"+x)

    elif "play" in query.lower():
        query = query.lower().replace("play","")
        speak("Playing "+query)
        pywhatkit.playonyt(query)
        exit(-1)

    elif "who is" in query.lower():
        try:
            query = query.lower().replace("who is","")
            speak("I found the following information about"+query)
            result = wikipedia.summary(query,sentences=2)
            speak(result)

        except Exception as e:
            print(e)
            speak("I'm sorry, I did not find anything about this")

    elif "what is" in query.lower():
        query = query.lower().replace("what is","")
        speak("I found the following information about"+query)
        try:
            result = wikipedia.summary(query,sentences=2)
            speak(result)
        except Exception as e:
            speak("I'm unable to help you at this moment")

    elif "joke" in query.lower() or "jokes" in query.lower():
        x = pyjokes.get_joke()
        speak(x)
        print(x)
        
    elif "time" in query.lower():
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak("currently its "+time)

    elif "stop" in query.lower() or "shut up" in query.lower() or "bye" in query.lower():
        speak("Ok")
        exit(-1)

    elif query is None:
        speak("I didn't catch that")
    else:
        speak("sorry I'm having trouble understanding clearly. Can you repeat that")
        giveCommand()


while True:
    run_vama()
    time.sleep(2)
    