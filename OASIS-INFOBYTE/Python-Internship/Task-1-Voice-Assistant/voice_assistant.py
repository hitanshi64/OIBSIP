import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# Initialize text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Convert text into speech."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen to user's voice command."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

            print("Recognizing...")
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand you. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Sorry, the speech recognition service is unavailable.")
            return ""


def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")


def tell_date():
    """Tell the current date."""
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {current_date}.")


def search_web(command):
    """Search the web for the user's topic."""
    topic = command.replace("search", "", 1).strip()

    if topic:
        speak(f"Searching for {topic}")
        webbrowser.open(
            "https://www.google.com/search?q=" + topic.replace(" ", "+")
        )
    else:
        speak("Please tell me what you want to search for.")


def process_command(command):
    """Process the user's voice command."""

    if not command:
        return True

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif command.startswith("search"):
        search_web(command)

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak(
            "Sorry, I do not understand that command. "
            "You can say hello, ask for the time or date, "
            "or say search followed by a topic."
        )

    return True


# Main program
speak("Voice assistant started. How can I help you?")

running = True

while running:
    command = listen()
    running = process_command(command)
    