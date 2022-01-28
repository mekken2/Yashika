import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak('I am Yashika(developed by Priyanshu). How may I help you?')

#Takes Microphone input from User and Enters String value
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP(smtp.gmail.com, 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_EMAIL_ID@gmail.com', 'YOUR_PASSWORD')
    server.sendmail('YOUR_EMAIL_ID@gmail.com',to,content)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube for master Prince")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google for master Prince")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow for master Prince")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("Playing music for master Prince")
            music_dir = "YOUR_MUSIC_DIRECTORY"
            songs = os.listdir(music_dir)
            print(songs)
            num = int(random.randint(0,380))
            os.startfile(os.path.join(music_dir, songs[num]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is " + strTime)

        elif 'editor' in query:
            speak("Opening Sublime Text")
            path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(path)

        elif 'email to Prince' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "emailtosend@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send Email at the moment")

