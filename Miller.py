import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takecommandvoice():
    # it takes microphone input form the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')

    except Exception as e:
        print (e)
 
        print("Trying to recognise again....")
        return "None"
    return query  


# if ('Hey Miller' in query):
#      speak('Miller activated')

# elif speak(" Not recognising")


# print(query)
# if 'hey miller' in query:
#             speak ('Miller activated')
#             # query=query.replace("wikipedia","")
#             # results = wikipedia.summary(query, sentences=2)
#             # speak("According to wikipedia")
# else:
#         speak("Not recognising")







    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    
    speak("This is miller 2.0,your personal assistant.how may i assist you sir?")

def takeCommand():
    # it takes microphone input form the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print (e)

        print("Say that again please....")
        return "None"
    return query     
         
if __name__ == "__main__":
    
    query=takecommandvoice().lower()
    print(query)
    
    if 'google' not in query:
        speak ('Not Recognising')
        print("STATUS: Not Recognising")
    else:
        speak("Miller Activated")
        print("STATUS: Miller Activated")
        wishMe()
        takecommandvoice()
        
        while True:
            print("INFO: while loop begin")
            query = takeCommand().lower()
            
            
            # Logic for executing  tasks based on  query
            
            if 'wikipedia' in query:
                speak ('Searching Wikipedia....')
                query=query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
                
            elif 'open youtube' in query:
                speak('opening you tube')
                webbrowser.open("youtube.com")
                
            elif 'open google' in query:
                speak('opening google ')
                webbrowser.open("google.com")
            
            elif 'open instagram' in query:
                webbrowser.open("instagram.com")
                
            elif 'open linkedin' in query:
                webbrowser.open("linkedin.com")
                
            elif 'open geeks for geeks ' in query:
                webbrowser.open("geeksforgeeks.org")
                
            elif 'open git hub ' in query:
                webbrowser.open("https://github.com/")
            
            elif 'open stackoverflow ' in query:
                webbrowser.open("https://stackoverflow.com/")
            
            elif 'open hackerrank ' in query:
                webbrowser.open("https://www.hackerrank.com/")
            elif 'open codechef ' in query:
                webbrowser.open("https://www.codechef.com/login")  
                
            elif 'open google classroom ' in query:
                
                webbrowser.open("https://classroom.google.com/u/1/h") 
            
            elif 'open gmail  ' in query:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")  
            
            elif 'play song' in query:
                speak('playing song')
                webbrowser.open("https://www.youtube.com/watch?v=umscM6qNWFk")
          
          
            # elif 'play music' in query:
            #     music_dir = 
            
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir,the time is{strTime}")
                # print('{strTime}')
            # elif 'my favourite person?' in query:
            #     speak('tarun bhaiya')

            # elif 'open code ' in query:
            #     speak('opening visual studio code')
            #     codePath = "C:\\Users\\aayus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            #     os.startfile(codePath) 
            elif 'how are you?' in query:
                speak('i am good sir...what about you')
