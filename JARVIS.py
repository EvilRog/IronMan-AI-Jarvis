from platform import python_branch
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import pywhatkit as kit
from requests import get
import webbrowser
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1,phrase_time_limit=5) 

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        speak("Say that again please:....")
        return "none"
    return query
    

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if(hour>0 and hour<=12):
        speak("Good morning")
    elif(hour>12 and hour<18):
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis sir. Please tell me how may i help you:")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()
    


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if "open pycharm" in query:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
            os.startfile(npath)
            
        elif "open command prompt" in query:
            os.system("start cmd")
        
        
        elif "play music" in query:
            music_dir = "C:\\Users\\EVIL ROG\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your ip address is {ip}")
            
        elif "wikipedia" in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            
        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
            
        elif "open google" in query:
            speak("Sir, what should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")    
            
        elif "send message" in query:
            kit.sendwhatmsg("+91XXXXXXXXXX", "this is message testing protcol",22,28)
            
        elif "song on youtube" in query:
            kit.playonyt("never satisfied")
        
        elif "email to unknown" in query:
            try:
                speak("what should i say?")
                content = takeCommand().lower()
                to = "unknown@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to unknown")
                
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this email to unknown")
                
        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day")
            sys.exit()
                
        
        speak("Sir do have any other work.?")
                      