import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    return query


if __name__ == '__main__':
    speak("Verona assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'are you' in query:
            speak("I am a Virtual Assistance")
        elif 'where are you from' in query:
            speak("I am from vijayapura KA-28")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
         elif 'play' in query:
            speak("Playing song on YouTube")
            query = query.replace("play", '').strip()
            if 'from' in query:
                song = query.split('from')[0].strip()
                movie = query.split('from')[1].strip()
                pywhatkit.playonyt(f"{song} song from {movie}")
                speak(f"Playing {song} from {movie}")
            else:
                pywhatkit.playonyt(query)
                speak(f"Playing {query}")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play' in query:
            speak("playing song on youtube")
            query = query.replace("play", '')
            song = query
            movie = ''
            for word in song.split():
                if word == 'from':
                    movie = ''.join(song.split()[song.split().index(word)+1:])
                    song = ''.join(song.split()[:song.split().index(word)])
            break
            pywhatkit.playonyt(song + " song from " + movie)
            speak("Playing " + song + " from " + movie)
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'leep' in query:
            exit(0)
        elif 'box office sultan of kannada industry' in query:
            speak("The box office Sultan of Kannada industry is Darshan Thougudeep.Also known as DBoss")
        elif 'google search' in query:
            speak("What would you like to search on Google?")
            search_query = take_command().lower()
            parameter = {
                "q": search_query,
                "location": "Austin,Texas",
                "api_key": os.getenv("API_KEY")
            }
            search = GoogleSearch(parameter)
            result = search.get_dict()
            if "error" in result:
                speak("Oops, error: " + result["error"])
            else:
                speak("Here are the search results:")
                for organic_result in result["organic_results"]:
                    speak(organic_result["title"] + " - " + organic_result["link"])
        else:
            speak("I didn't understand. Can you please repeat?")