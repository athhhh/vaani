import os
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from app import app
from app.utils.text_to_speech import text_to_speech
from app.utils.speech_to_text import speech_to_text
from app.utils.image_recognizer import image_recognition
from app.utils.smart_assistant import smart_assistant

@app.route('/')
def index():
    """
    Renders the index.html template for the home page.
    """
    return render_template('index.html')

@app.route('/text_to_speech', methods=['GET', 'POST'])
def text_to_speech_route():
    """
    Handles the text-to-speech functionality.
    """
    if request.method == 'POST':
        text = request.form['text']
        language = request.form['language']
        audio_file = text_to_speech(text, language)
        return redirect(url_for('text_to_speech_route', audio_file=audio_file))
    return render_template('text_to_speech.html')

@app.route('/speech_to_text', methods=['GET', 'POST'])
def speech_to_text_route():
    """
    Handles the speech-to-text functionality.
    """
    if request.method == 'POST':
        text = speech_to_text()
        return text
    return render_template('speech_to_text.html')

@app.route('/image_recognition', methods=['GET', 'POST'])
def image_recognition_route():
    """
    Handles the image recognition functionality.
    """
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No image file uploaded.')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No image file selected.')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            description = image_recognition(file_path)
            return render_template('image_recognition.html', description=description)
    return render_template('image_recognition.html')

@app.route('/smart_assistant', methods=['GET', 'POST'])
def smart_assistant_route():
    """
    Handles the smart assistant functionality.
    """
    if request.method == 'POST':
        query = request.form['query']
        response = smart_assistant(query)
        return response
    return render_template('smart_assistant.html')

@app.route('/about')
def about():
    """
    Renders the about.html template for the About page.
    """
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Handles the contact form submission.
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You can implement email sending or save to a database here
        flash('Thank you for your message!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')