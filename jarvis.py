#recognizer.adjust_for_ambient_noise(source) => to reduce background noise
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk
import subprocess

#Initialize recognizer and text-to-speech engine
listening = sr.Recognizer()
engine = pt.init()

#Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Hear function to capture voice command
def hear():
    try:
        with sr.Microphone() as mic:
            print('Listening.....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'jarvis' in cmd:
                cmd = cmd.replace('karishma', '').strip()
                print(cmd)
                return cmd
    except:
        return ""
    return ""
 
#Function to open system applications
def open_app(app_name):
    if('notepad') in app_name:
        speak('Opening Notepad')
        subprocess.run('notepad')
        
    elif 'calculator' in app_name:
        speak('Opening Calculator')
        subprocess.run('calc')
        
    elif 'chrome' in app_name:
        speak('Opening Google Chrome')
        subprocess.run('start chrome', shell=True)
        
    elif 'command prompt' in app_name or 'cmd' in app_name:
        speak('Opening Command Prompt')
        subprocess.run('cmd', shell=True)
        
    elif 'explorer' in app_name:
        speak('Opening File Explorer')
        subprocess.run('explorer')
        
    elif 'task manager' in app_name:
        speak('Opening Task Manager')
        subprocess.run('taskmgr')
        
    else: 
        speak(f"Sorry, I can't open {app_name} at the moment")
        
        
#Run function to exceute commands
def run():
    cmd = hear()
    print(cmd)
    
    #Play Youtube video
    if 'play' in cmd:
        song = cmd.replace('play', '').strip()
        speak(f'Playing {song} on YouTube')
        pk.playonyt(song)
        
    #Open system applications
    elif 'open' in cmd:
       app_name = cmd.replace('open', '').strip()
       open_app(app_name)
       
    else:
         speak("I didn't understand that. Please try again.")
      
#Main function call
run()
        
        
    