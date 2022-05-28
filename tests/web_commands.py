# Project-CortanaAI, Level 0, Step-3


# Web commands for CortanaAI

import pyttsx3
import speech_recognition as source1
import datetime
import os
from cortana_introduction import introduction
import webbrowser


# username
username = "Starboy"
ai_name = "Cortana"


# voice_engine
voice_engine = pyttsx3.init("sapi5")       # object creation, voice_engine
# voice_engine.say('Hello World')


# voice_engine_voice
voice_engine_voice = voice_engine.getProperty("voices")

# print(voice_engine_voice[1].id)
voice_engine.setProperty("voice", voice_engine_voice[2].id)

# voice_engine_rate
voice_engine_rate = voice_engine.getProperty("rate")

# print(voice_engine_rate)
voice_engine.setProperty("rate", 200)


def speak(audio):             # A speak function(), which takes audio as it's parameter
    voice_engine.say(audio)
    voice_engine.runAndWait()


# Greeting message
def greeting():
    datetime.datetime.now()

    # print(time1)
    time_in_hour = int(datetime.datetime.now().hour)

    # print(time_in_hour)
    if time_in_hour > 0 and time_in_hour < 12:
        print(f"Hello {username}, Good Morning :)\n")

    elif time_in_hour > 12 and time_in_hour < 16:
        print(f"Hello {username}, Good Afternoon :)\n")

    else:
        print(f"Hello {username}, Good Evening :)\n")

    # Ultimate statements
    print("I'm here... \n")
    speak("I'm here")


def process_command():
    """
    As the name says, It processes voice command from microphone & returns result of the command.

    """
    command = source1.Recognizer()

    with source1.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1.5
        audio = command.listen(source)

    # Executing Query
    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language="en-us")
        print(f"You said; {query}\n")

    except Exception:
        return "Something's not right, Please try again! \n"

    return query


# Ultimate-Function
attempt = 0
if __name__ == "__main__":
    introduction()
    greeting()

    # logic
    try:
        while True:
            query = process_command().lower()
            attempt = attempt + 1

            # base-commands;
            if attempt >= 5:
                print("Looking forward to helping out... \n")
                speak("Looking forward to helping out...")
                break

            # define yourself
            elif "who are you" in query:
                print(
                    f"Hello, I'm {ai_name} & I'm here to help you... \n")
                speak(f"Hello, I'm {ai_name}, and I'm here to help you")
                continue

            # feedback | work required!
            elif "you need to improve" in query:
                print("Sorry for the inconvenience :( \n")
                speak("Sure")
                break

            # date | work required!
            elif "the date" in query:
                current_date = str(os.system("date"))
                print(f"The current date is; {current_date} \n")
                speak(f"The current date is, {current_date}")
                continue

            # time
            elif "the time" in query:
                current_time = datetime.datetime.now().strftime(" %H:%M:%S ")
                print(f"The time is; {current_time} \n")
                speak(f"The time is; {current_time}")
                continue

            # wishing
            elif "good morning" in query:
                print(f"Good morning {username}, have a nice day :) \n")
                speak(f"Good morning {username}, have a nice day")
                continue

            elif "good afternoon" in query:
                print(f"Good afternoon {username}, hope you doing good :) \n")
                speak(f"Good afternoon {username}, hope you doing good")
                continue

            elif "good evening" in query:
                print(
                    f"Good evening {username}, It's time to get refreshed :) \n")
                speak(
                    f"Good evening {username}, It's time to get refreshed")
                continue

            elif "good night" in query:
                print(f"Good Night {username}, Have a nice dream :) \n")
                speak(f"Good Night {username}, Have a nice dream")
                continue

            # Web Commands

            # google.com
            elif 'open google.com' in query:
                webbrowser.open('https://www.google.com/')
                print('Opening Google.com...')
                speak('Opening Google.com...')
                exit()

            # duckduckgo.com
            elif "open duckduckgo" in query:
                webbrowser.open("https://duckduckgo.com/")
                print("Opening DuckDuckGo.com...")
                speak("Opening DuckDuckGo.com...")
                exit()

            # wikipedia.org
            elif "open wikipedia" in query:
                webbrowser.open("https://www.wikipedia.org/")
                print("Opening Wikipedia.org...")
                speak("Opening Wikipedia...")
                exit()

            # gmail.com
            elif "open gmail" in query:
                webbrowser.open("https://www.gmail.com/")
                print("Opening Google Mail...")
                speak("Opening Google Mail...")
                exit()

            # protonmail.com
            elif "open protonmail" in query:
                webbrowser.open("https://protonmail.com/")
                print("Opening ProtonMail.com...")
                speak("Opening ProtonMail.com...")
                exit()

            # blogger.com
            elif "open blogger.com" in query:
                webbrowser.open("https://www.blogger.com/")
                print("Opening Blogger.com...")
                speak("Opening Blogger.com...")
                exit()

            # youtube.com
            elif 'open youtube' in query:
                webbrowser.open('https://www.youtube.com/')
                print('Opening Youtube...')
                speak('Opening Youtube...')
                exit()

            # google drive
            elif "open google drive" in query:
                webbrowser.open("https://drive.google.com/")
                print("Opening Google Drive...")
                speak("Opening Google Drive...")
                exit()

            # google cloud shell
            elif "open cloud terminal" in query:
                webbrowser.open("https://cloud.google.com/shell/")
                print("Opening Google Cloud Shell...")
                speak("Opening Google Cloud Shell...")
                exit()

            # khanacademy.org
            elif "open khan academy" in query:
                webbrowser.open("https://www.khanacademy.org/")
                print("Opening KhanAcademy.org...")
                speak("Opening KhanAcademy.org...")
                exit()

            # udemy.com
            elif 'open udemy' in query:
                webbrowser.open('https://www.udemy.com/')
                print('Opening Udemy.com...')
                speak('Opening Udemy...')
                exit()

            # replit.com
            elif "open code browser" in query:
                webbrowser.open("https://replit.com/")
                print("Opening Replit.com...")
                speak("Opening Replit.com...")
                exit()

            # stackoverflow
            elif "open stack overflow" in query:
                webbrowser.open("https://stackoverflow.com/")
                print("Opening StackOverFlow.com...")
                speak("Opening StackOverFlow...")
                exit()

            # stackoverflow.com
            elif "open stackoverflow" in query:
                webbrowser.open("https://stackoverflow.com/")
                print("Opening StackOverFlow.com...")
                speak("Opening StackOverFlow.com...")
                exit()

            # github.com
            elif 'open github' in query:
                webbrowser.open('https://github.com/')
                print('Opening Github.com...')
                speak('Opening Github...')
                exit()

            # gitlab.com
            elif "open git lab" in query:
                webbrowser.open("https://gitlab.com/")
                print("Opening GitLab.com...")
                speak("Opening GitLab...")
                exit()

            # hackthebox.eu
            elif "open hack the box" in query:
                webbrowser.open("https://www.hackthebox.eu/")
                print("Opening HackTheBox.eu...")
                speak("Opening HackTheBox...")
                exit()

            # hackerone.com
            elif "open hacker 1" in query:
                webbrowser.open("https://www.hackerone.com/")
                print("Opening HackerOne.com...")
                speak("Opening HackerOne.com...")
                exit()

            # docker hub
            elif "open docker hub" in query:
                webbrowser.open("https://hub.docker.com/")
                print("Opening Docker Hub...")
                speak("Opening Docker Hub...")
                exit()

            # apple.com
            elif "open apple.com" in query:
                webbrowser.open("https://www.apple.com/")
                print("Opening Apple.com...")
                speak("Opening Apple.com...")
                exit()

            # amazon.in
            elif 'open amazon.in' in query:
                webbrowser.open('https://www.amazon.in/')
                print('Opening Amazon.in...')
                speak('Opening Amazon.in...')
                exit()

            # amazon.com
            elif 'open amazon.com' in query:
                webbrowser.open('https://www.amazon.com/')
                print('Opening Amazon.com...')
                speak('Opening Amazon.com...')
                exit()

            # flipkart.com
            elif "open flipkart" in query:
                webbrowser.open("https://www.flipkart.com/")
                print("Opening Flipkart.com...")
                speak("Opening Flipkart.com...")
                exit()

            # twitter.com
            elif "open twitter" in query:
                webbrowser.open("https://twitter.com/")
                print("Opening Twitter.com...")
                speak("Opening Twitter.com...")
                exit()

            # discord.com
            elif "open discord" in query:
                webbrowser.open("https://discord.com/")
                print("Opening Discord.com...")
                speak("Opening Discord.com...")
                exit()

            # reddit.com
            elif "open reddit" in query:
                webbrowser.open("https://www.reddit.com/")
                print("Opening Reddit.com")
                speak("Opening Reddit.com")
                exit()

            # spacex.com
            elif "open space x.com" in query:
                webbrowser.open("https://www.spacex.com/")
                print("Opening SpaceX.com...")
                speak("Opening SpaceX.com...")
                exit()

            # unrealengine.com
            elif "open unreal engine dotkom" in query:
                webbrowser.open("https://www.unrealengine.com/")
                print("Opening Unreal Engine.com...")
                speak("Opening Unreal Engine.com...")
                exit()

            elif "open unreal engine dotcom" in query:
                webbrowser.open("https://www.unrealengine.com/")
                print("Opening Unreal Engine.com...")
                speak("Opening Unreal Engine.com...")
                exit()

            # learn.unrealengine.com
            elif "open unreal engine learning" in query:
                webbrowser.open("https://learn.unrealengine.com/")
                print("Opening Learn.UnrealEngine.com...")
                speak("Opening Learn.UnrealEngine.com...")
                exit()

            # dev.epicgames.com
            elif "open epic developer community" in query:
                webbrowser.open("https://dev.epicgames.com/community/")
                print("Opening Dev.EpicGames.com/community...")
                speak("Opening Dev.EpicGames.com/community...")
                exit()

            # open.spotify.com
            elif "open spotify on web" in query:
                webbrowser.open("https://open.spotify.com/")
                print("Opening Spotify on Web, Enjoy listening...")
                speak("Opening Spotify on Web, Enjoy listening...")
                exit()

            # open.spotify.com
            elif "open spotify on the web" in query:
                webbrowser.open("https://open.spotify.com/")
                print("Opening Spotify on Web, Enjoy listening...")
                speak("Opening Spotify on Web, Enjoy listening...")
                exit()

            # exit
            elif "quit" in query:
                print("Okay :) \n")
                speak("Okay")
                break

            elif "exit" in query:
                print("Okay :) \n")
                speak("Okay")
                break

            # ok
            elif "ok" in query:
                print("Alright ;) \n")
                speak("Alright")
                break

            # error-message
            else:
                print("Please Try Again! \n")
                speak("Say again")
                continue

    except KeyboardInterrupt:
        print("\n Operation cancelled by the user :( \n")