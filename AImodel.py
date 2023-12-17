import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")
    
    elif(hour>=12 and hour<18):
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("Hello sir I am Alexa. How may I help you, sir?")

def TakeCommand():
    # It takes input from microphone as audio and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        # speak(query)
    except Exception as e:
        print("Said the command again...")
        return "None"
    
    return query


if __name__ == "__main__":
    speak("Please enter user password") 

    check = input().lower()
    if(check == "src"):
        WishMe()
        while True:
            query = input().lower()
            if "wikipedia" in query:
                speak("Searching in Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                print(results)
                speak(results)

            elif ("open youtube" in query) or ("open you tube" in query):
                speak("Opening You tube")
                wb.open("youtube.com")
            
            elif "open google" in query:
                speak("opening Google")
                wb.open("google.com")

            elif ("open stackoverflow" in query) or ("open stack overflow" in query):
                speak("Opening stack over flow")
                wb.open("stackoverflow.com")

            elif ("play music" in query):
                mus_dir = "D:\\Songs\\J"
                songs = os.listdir(mus_dir)
                r = random.randint(0,len(songs)-1)
                os.startfile(os.path.join(mus_dir, songs[r]))

            elif("time" in query):
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"Sir the time is{strTime}")
            
            elif("quit" in query):
                quit()

    else:
        speak("Sorry user password is wrong...")
        quit()