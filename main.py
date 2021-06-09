import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
engine  =  pyttsx3.init()
voices =  engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
newVoiceRate = 230
engine.setProperty('rate', newVoiceRate)
#--------------------------------------------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#----------------------------------------------------------------
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(time)
#---------------------------------------------------------------
def date():
    year =  int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)

    speak("Today's date is ")
    speak (date)
    speak(month)
    speak (year)
#-----------------------------------------------------------------
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("Jarvis at your Service sir. How may I help you?")
#----------------------------------------------------------------
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio =  r.listen(source)

    try:
        print("Recognizing......")
        query =  r.recognize_google(audio, language='en-US')
        print(query)
    except Exception as e:
        print(e)
        speak("I did not hear you sir! Please Say that again. ")
        return "None"

    return query
#---------------------------------------------------------------
def sendemail(to, content):
    server = smtplib.SMTP('smtp.gemail.com',587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","Password")
    server.sendemail("text@gmail.com", to, content)
    server.close()

#----------------------------------------------------------------------------
def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\ss.png")
#-----------------------------------------------------------------------------
def cpu():
    usage =  str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery
    speak("battery is at ")
    speak(battery.percent)
#--------------------------------------------------------------------------------
if __name__ == "__main__" :
    wishme()
    
    while True:
        query = takecommand().lower()
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query =  query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences =  2)
            speak(result) 
        elif "send email" in query:
            try:
                speak("What should I send?")
                content = takecommand()
                to = "xyz@gmail.com"
                sendemail(to, content)
                speak("The mail was sent successfully.")
            except Exception as e:
                speak(e)
                speak("Unable to send email")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search =  takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif  "logout" in query :
            os.System("shutdown - 1")
        elif  "shutdown" in query :
            os.System("shutdown /s /t 1")
        elif "restart" in query:
            os.System("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir =  " "
            songs = os.listdir(songs_dir)
            os.startfile (os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("what should I remember?")
            data =  takecommand()
            speak("You said me to remember" + data)
            remember  =  open("data.txt, "w")
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember =  open("data.txt", "r")
            speak("You said me to remember that" + remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done!")
        elif "cpu" in query:
            cpu()
        elif  "goodbye jarvis" in query:
            quit()
            



