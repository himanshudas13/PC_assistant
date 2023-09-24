import speech_recognition as sr
import win32com.client
import webbrowser as web

def say(text2):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text2)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio, language="en-in")
        print(f"User: {user_input}")
        return user_input
    except Exception as e:
        print("Sorry ! COULDN'T PROCESS WHAT YOU SAID")
        sorry_text = "Sorry ! COULDN'T PROCESS WHAT YOU SAID"
        say(sorry_text)
        return "none"

def checkcommand(command):

    links = [["google", "www.google.com"], ["youtube", "www.youtube.com"], ["github", "github.com"]]
    if "open" in command.lower():
     for x in links:
        if f"open {x[0]}" in command.lower():
         say(f"loading {x[0]}")
         web.open(f"{x[1]}")
    elif (f"search" in command.lower()) or (f"what is" in command.lower()):
     command=command.replace("search"," ")
     say("this might be of some help")
     web.open(command)
    elif(f"play" in command.lower()):
      say(f"playing ")





say("Hello Himanshu")
case = 1
while case:
  print("Listening..")
  uinput = take_command()
  if "bye siri" in uinput.lower():
      case=0
      break
  elif uinput=="none" :
      case = 0
      break
  checkcommand(uinput)

