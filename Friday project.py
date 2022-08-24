import pyttsx3                                                     #pip install pyttsx3   lib
import datetime                                                    #import date time lib
import speech_recognition as sr                                    #pip install speechrecognition
import wikipedia                                                   #pip install wikipedia
import smtplib                                                     #pip install smtp to send emails using gmail
import webbrowser as wb                                            #pip install wb to take browsing commands
import psutil                                                      #lib used to access system details and process utilities
import pyjokes                                                     #python library that is used to create one-line jokes
import os
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha                                                #pip instal wolframalpha
import time






engine = pyttsx3.init()                                            #to load the necessary driver
wolframalpha_app_id ='9PP9RQ-X3P5YTYW4G' 



def speak(audio):
        engine.say(audio)                                           # to Speak particular task
        engine.runAndWait()

def time_():
        Time= datetime.datetime.now().strftime("%H:%M:%S")         #for 24 hour clock       #%I: for 12 hour clock
        speak("The current time is: ")
        speak(Time)
        print(Time)

        

def date_():
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        date = datetime.datetime.now().day
        speak("The current date is: ")
        speak(date)
        print(date)
        speak(month)
        print(month)                                                 #sequence wise date - month - year
        speak(year)
        print(year)
        

        
         
                                                                    #call function just like print  
                                                                    #FUNCTION COMPLETED TILL YET (speak,time,date


def wishme_():
    
    
             #GREETINGS

        hour= datetime.datetime.now().hour                              #so that it can store the value of hour

        if hour>=6 and hour<=12:
         speak("GOOD MORNING SIR!")
        elif hour>=12 and hour<=18:
         speak("GOOD AFTERNOON SIR!")    
        elif hour>=18 and hour<=24:
         speak("GOOD EVENING SIR!")
        else:
         speak("GOOD NIGHT SIR!")

        speak("Hi, I'm FRIDAY 2.0 at your service. Speed 1 terahertz, memory 1 zigabyte. Please tell me how can i help you? , I can do variety of stuff!")
    
      


def TakeCommand():

    r=sr.Recognizer()                                     #it is prebuild function in python and it helps us in recognizing voice commands   
    with sr.Microphone() as source:
         print("Listening.......")
         r.pause_threshold = 1                               #it is prebuild function of recognizer means how long will it wait for its user to take command
         audio = r.listen(source)                            #whatever it listens it will be stored in this variable called audio

    try: 
         print("Recognizing.......")                          
         query = r.recognize_google(audio,language='en-US')                 #command will stored here after recognized by google
         print(query)


    except Exception as e:
         print(e)
         print("Say that again please......")
         return "None"
    return query                                              #pip install pipwin & pipwin install pyaudio




def sendEmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)                  #587 is a code for GMAIL
        server.ehlo()                                              #ehlo will help in identifying ourselve to an ESMTP server
        server.starttls()                                          #help us putting connection to the SMTP server into the TLS mode

                                                                  #However, for this function , you must enable low security in your gmail which you are going to use as sender
        server.login('tarun007.b@gmail.com','Shv1975#')
        server.sendmail('tarun007.b@gmail.com',to,content)
        server.close()

def screenshot():
        img = pyautogui.screenshot()                                      
        img.save('C:/Users/tarun/Desktop/screenshot.png')         #pyautogui provides the ability to simulate mouse cursor moves and clicks as well as keyboard button presses.



def cpu():
        usage = str(psutil.cpu_percent())
        speak('cpu is at'+usage)

        battery = psutil.sensors_battery()            #psutil is used to tell Usage of resources like CPU, memory, disks, network, sensors can be monitored
        speak('battery is at')
        speak(battery.percent)

def joke():
        speak(pyjokes.get_joke())                     #pyjokes is pre built lib used to tell jokes
        print(joke)



if __name__ == "__main__":

    wishme_()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:                         #tell us time when asked
            time_()

        elif 'date' in query:                       #tell us date when asked
            date_()

    

        elif 'wikipedia' in query:                                         #tell us wikipedia info when asked
            speak("searching......")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('according to wikipedia')
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content=TakeCommand()
                                                                             #provide reciever's address
                speak("who is the reciever?")
                reciever=input("enter reciever's email address :")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('email has been sent.')
                print('email has been sent.')

            except Exception as e: 
                print(e)  
                speak("unable to send email.")   

        elif 'search in chrome' in query:
            speak('what should i search?')
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
                                                                     #chromepath is location of chrome exe file on computer
                                                                    
            search=TakeCommand().lower()                             #for easy recognition
            wb.get(chromepath).open_new_tab(search+'.com')           #only open websites with .com at the end.


        elif 'search in youtube' in query:
            speak('what should i search, sir?')
            search_Term = TakeCommand().lower()
            speak("here, we go to youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)         #here wb is webbrowser and search_query is for search

        elif 'search in google' in query:
            speak('what should i search, sir?')
            search_Term = TakeCommand().lower()
            speak('searching......')
            wb.open('https://www.google.com/search?q='+search_Term)    


        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()
            
            

        elif 'i love you' in query:
            speak('Aww, So sweet of you, I love you too, as a machine!')
            print('Aww, So sweet of you, I love you too, as a machine!')               #These are the commands from users stored in query, where query is a variable!
            

        elif 'how are you' in query:
            speak('I am fine, thanks for asking sir!')
            print('I am fine, thanks for asking sir!')
            speak("how are you sir?")
        elif 'fine' in query or 'good' in query:
            speak("it's good to know that you are fine")    
            

        elif 'check my system' in query:
            speak('CHECKING....... , your HP laptop is running at normal and it is up to date sir!')
            print("Friday: Your HP laptop is running at normal and it is up to date sir!") 
               

        elif 'who created you' in query or 'who is your boss' in query:
            speak('Tarun created me, He is studying Btech in computer science and engineering as a project for his college')
            print('Tarun created me, He is studying Btech in computer science and engineering as a project for his college')

        elif 'who are your friends' in query:
            speak('i have many friends like Jarvis, cortana, alexa , siri!')
            print('i have many friends like Jarvis, cortana, alexa , siri!')

        elif 'what is love' and 'tell me about love' in query:
            speak("it is 7th sense that destroy all other senses ,"
                   "And i think it is just a mere illusion ,"
                   "it is waste of time")        
            

        elif 'who are you' in query or 'tell me about yourself' in query:
            speak("Hi, I'm FRIDAY 2.0 your artificial intelligence virtual assistant at your service. Speed 1 terahertz, memory 1 zigabyte. I can perform variety of tasks for you at your command")       
            print("Hi, I'm FRIDAY 2.0 your artificial intelligence virtual assistant at your service. Speed 1 terahertz, memory 1 zigabyte. I can perform variety of tasks for you at your command")

        elif 'shutdown' in query:
            speak('Signing off!')
            print('Signing off!')
            quit()                                             #quit function is used to quit the code after executing it.



        elif 'open word' in query:
            speak('opening ms word!')
            ms_word = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'             #location of ms word in computer
            os.startfile(ms_word)                                                            #os.startfile  allows us to start/run a file with its associated program.


        elif 'write a note' in query:
            speak('what should is write, sir?')
            notes=TakeCommand()
            file= open('notes.txt','w')
            speak("sir should i include date and time?")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H: %M: %S")
                file.write(strTime)       
                file.write(':-')
                file.write(notes)
                speak('done taking notes, sir!')
            else: 
                file.write(notes)

        elif 'show notes' in query:
                speak('showing notes')
                file = open('notes.txt','r')
                print(file.read())
                speak(file.read())       

        elif 'take screenshot' in query:
                speak('taking screenshot..')
                print('taking screenshot..')
                speak('screenshot taken!')
                print('screenshot taken!')
                screenshot()
         
    

        elif 'play music' in query:
            songs_dir = 'D:\songs'
            music = os.listdir(songs_dir)                               #os means operating system
            speak('what should i play?')
            speak('select a number....')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random' and ans != 'you choose'):
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1,100)     

            os.startfile(os.path.join(songs_dir,music[no]))
  


        elif 'remember that' in query:
             speak("what should i remember?")
             memory = TakeCommand()
             speak('you asked me to remember that'+memory)
             remember = open('memory.txt','w')
             remember.write(memory)
             remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('you asked me to remember that'+remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=fe87a6fefefa44138f56fcd4e59de066")
                data = json.load(jsonObj)
                i = 1

                speak('Here are some top headlines from business industry')
                print('=============TOP HEADLINES============'+'\n')
                for item in data['articles']: 
                    print (str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print (str(e))   

        elif 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
            
        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print('The answer is : '+answer)
            speak('The answer is '+answer) 

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")    

        elif 'stop listening' in query:
            speak('For how many seconds you want me to stop listening to your commands?')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans) 


        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")                              



        
                      









                
