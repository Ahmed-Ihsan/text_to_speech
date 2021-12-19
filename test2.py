
# Importing required modules
import os
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from threading import Thread
import webbrowser
import alsaaudio

class Gfg:
    def takeCommands(self):
          
          r = sr.Recognizer()
          with sr.Microphone() as source:
              print('Listening')
 
              r.pause_threshold = 1
              r.energy_threshold = 4000
              audio = r.listen(source)
            
              try:
 
                  print("Recognizing")
                  Query = r.recognize_google(audio, language='en-in')
 
                  print("the query is printed='", Query, "'")
 
              except Exception as e:
 
                  print(e) 
                  print("Say that again sir")
                  return "None"
          return Query
 
    def Speak(self, audio):
   
          engine = pyttsx3.init('sapi5')
          voices = engine.getProperty('voices')
          engine.setProperty('voice', voices[1].id)
          engine.say(audio)
          engine.runAndWait()
 
     
    def quitSelf(self):
        self.Speak("")
 
        take = self.takeCommands()
        choice = take
        if 'time' in choice or "oclock" in choice:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            self.Speak("time is")
            self.Speak(current_time)
        
        elif choice == 'open folder':
            os.system("start.")
            self.Speak("open folder")

        elif 'open' in choice and 'word' :
            os.system("start.")
            self.Speak("open folder")

        elif  'good' in choice:
            print("yes ,Thank u sir")
            self.Speak("yes ,Thank u sir")

        elif  'hi' in choice:
            print("hi sir")
            self.Speak("hi sir")
        
        elif  'audio' in choice:
            self.Speak("open audio")
            os.system("welcome.mp3")

        elif 'open' in choice and 'browser' in choice :
            self.Speak("open browser")
            webbrowser.open("https://google.com")
    
        elif  'close browser' in choice:
            self.Speak("close browser")
            os.system("taskkill /im chrome.exe")
            
        elif  'open paint' in choice:
            self.Speak("open paint")
            os.system("start mspaint")
        
        elif  'exit paint' in choice:
            self.Speak("close paint")
            os.system("taskkill /im mspaint.exe")

        elif 'open' in choice and 'YouTube' in choice :
            self.Speak("open YouTube")
            webbrowser.open("https://youtube.com")

        elif 'when' in choice and 'birthday':
            self.Speak("you are birthday in 1990/12/13")

        elif 'open text file'  in choice:
            os.system("start notepad")
            self.Speak("start notepad")
        
        elif 'who'  in choice and "Dr Ali" in choice :
            os.system("start notepad")
            self.Speak("start notepad")

        


if __name__ == '__main__':
    Maam = Gfg()
    while 1:
     Maam.quitSelf()