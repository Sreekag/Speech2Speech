import base64
import streamlit as st
import pyttsx3
import speech_recognition as sr
import os

def speech_to_text(audio_file_path):
    # Initialize recognizer
    r = sr.Recognizer()

    # Load the audio file
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio = r.record(source)  # Record the audio file

        # Recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return 
        except sr.RequestError as e:
            return 

    except FileNotFoundError:
        return f"Audio file not found at {audio_file_path}"


def text_to_speech(text, file_name='output.mp3'):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.say(text)
    # Save the speech to an audio file
    engine.save_to_file(text, file_name)
    engine.runAndWait()



