import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyaudio

#initialize speech recognition and text_to_speech engines
recogniser = sr.Recognizer()
engine = pyttsx3.init()

#function for text speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function to recognize speech
def listen():
    #make use of microphone as the audio source
    with sr.Microphone() as source: #make use of built in microphone
        print("Currently listening")
        #implement audio adjustment before listening
        recogniser.adjust_for_ambient_noise(source)
        #listen for audio 
        audio = recogniser.listen(source)

        try:
            print("recognizing...")
            #recognise speech using google speech recognition
            query = recogniser.recognize_google(audio)
            print("User: ", query)
            return query.lower()
        except sr.UnknownValueError:
            #handle unknown or unrecognised speech
            speak("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            #handle network issues (request error)
            speak("Sorry, I couldn't process your request at the moment.")
            return ""
        
#implement function to greet user
def greet():
    #acquire current datetime
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
#Main function for the functionality of the voice recognition
def main():
    #greet user!
    greet()
    speak("How can i assist you?")
    
    #continuous loop to listen for commands
    while True:
        voice_query = listen()
        #process user commands
        if "hello" in voice_query:
            speak("Hello! How can i help you?")
        elif "what is the time" in voice_query:
            #get current time
            current_time = datetime.datetime.now().strftime("%I-%M-%p")
            speak(f"The current time is {current_time}.")
        elif "what is the date of today" in voice_query:
            #get current date
            current_date = datetime.datetime.now().strftime("%A, %B, %d, %Y")
            speak(f"The current date is {current_date}.")
        elif "search" in voice_query:
            speak("What would you like me to search for?")
            search_query = listen()
            #listen to the user search command
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                speak(f"Here are the search results for {search_query}.")
        #get user input to exit the program
        elif "exit" in voice_query or "quit" in voice_query:
            speak("Goodbye!")
            break

    

if __name__ == "__main__":
    main()
