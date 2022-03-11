from datetime import datetime
from py_compile import main
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
# print(voices[0].id)
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    """"""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """"""
    hour=int(datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am zira mam. Please tell me how may I help you")

def takecommand():
    """it iakes microphone input from the user and returns string output"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold=4000
        audio=r.listen(source)
    try:
        print("Recognizing......")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishme()
    while True:
       query=takecommand().lower()
    #logic for executing the task based on query
       if 'wikipedia' in query:
           speak('searching wikipedia.....')
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")

       elif 'play music' in query:
           music_dir = 'F:\\Music\\Prem-Ratan-Dhan-Payo-2015'
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
       elif 'the time' in query:
           strTime=datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(f"Mam,the time is {strTime}")
        
       elif 'open code' in query:
           codepath="C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)

       elif 'email to sabiha' in query:
           try:
               speak("What should I say")
               content=takecommand()
               to="sabihayourEmail@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent")
           except Exception as e:
               print(e)
               speak("Sorry my friend sabiha I am not able to send this email")

       elif 'play video song' in query:
           video_dir='F:\\Videoz'
           videos=os.listdir(video_dir)
           print(videos)
           os.startfile(os.path.join(video_dir,videos[1]))
       
       elif 'how are you' in query:
           speak("I am fine how are you mam")
       
       elif 'i am fine' in query:
           speak("okay nice")

       elif 'who are you' in query:
           speak("I am bad girl")

       elif 'quit' in query:
           exit()

