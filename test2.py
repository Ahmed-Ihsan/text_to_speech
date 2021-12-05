
# Importing required modules
import os
import pyttsx3
import speech_recognition as sr
from datetime import datetime

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

        elif  'good' in choice:
            print("yes ,Thank u sir")
            self.Speak("yes ,Thank u sir")

        elif  'hi' in choice:
            print("hi sir")
            self.Speak("hi sir")
        
        elif  'audio' in choice:
            self.Speak("open audio")
            os.system("welcome.mp3")
      
if __name__ == '__main__':
    Maam = Gfg()
    while 1:
     Maam.quitSelf()