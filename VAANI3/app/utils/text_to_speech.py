import os
from gtts import gTTS

def text_to_speech(text, language):
    """
    Converts text to speech and saves the audio file.

    Args:
        text (str): The text to be converted to speech.
        language (str): The language code for the speech (e.g., 'en', 'fr', 'es').

    Returns:
        str: The path to the generated audio file.
    """
    # Create a temporary file to save the audio
    audio_file = os.path.join('app/static/audio', 'output.mp3')

    # Convert text to speech
    tts = gTTS(text=text, lang=language)
    tts.save(audio_file)

    return audio_file