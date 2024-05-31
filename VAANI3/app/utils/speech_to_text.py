import speech_recognition as sr

def speech_to_text():
    """
    Transcribes speech from audio to text using Google Speech Recognition.

    Returns:
        str: The transcribed text from the audio.
    """
    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print('Speak now...')
        audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return 'Sorry, I could not understand your speech.'
    except sr.RequestError as e:
        return f'Speech Recognition Error: {e}'