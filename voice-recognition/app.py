import speech_recognition as sr
from langdetect import detect_langs
from googletrans import Translator

def detect_language(audio_text):
    try:
        lang_list = detect_langs(audio_text)
        detected_language = lang_list[0].lang
        return detected_language
    except:
        return "unknown"

print("\t\t\t\t*\tWELCOME TO LANGUAGE TRANSLATOR\t*\nPlease select your choice\n")
x = int(input("1.\tSpeech to text conversion\n2.\tText to speech conversion\n"))

if x == 1:
    print("selected 1\n")
    # Initialize the recognizers
    recognizer = sr.Recognizer()
    
    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Recording...")
        audio = recognizer.listen(source)
        print("Recording finished.")
    
    try:
        recognized_text = recognizer.recognize_google(audio)
        print("Recognized Text: ", recognized_text)
        
        # Detect the language of the recognized text
        detected_language = detect_language(recognized_text)
        print("Detected language: {}".format(detected_language))
        
        # Ask user for the desired language
        desired_language = input("Enter the desired language (e.g., English, Urdu, Hindi, Pashto): ")
        
        # Translate the text to the desired language
        translator = Translator()
        translated_text = translator.translate(recognized_text, dest=desired_language).text
        print("Translated text: ", translated_text)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

elif x == 2:
    print("selected 2\n")
else:
    print("wrong input\n")