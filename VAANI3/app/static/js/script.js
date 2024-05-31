const startRecordingButton = document.getElementById('start-recording');
const stopRecordingButton = document.getElementById('stop-recording');
const recognizedTextArea = document.getElementById('recognized-text');

let recognition;

function startRecording() {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onresult = function(event) {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
            transcript += event.results[i][0].transcript;
        }
        recognizedTextArea.value = transcript;
    };

    recognition.start();

    startRecordingButton.disabled = true;
    stopRecordingButton.disabled = false;
}

function stopRecording() {
    recognition.stop();
    startRecordingButton.disabled = false;
    stopRecordingButton.disabled = true;
}

startRecordingButton.addEventListener('click', startRecording);
stopRecordingButton.addEventListener('click', stopRecording);

// Image Preview
const imageForm = document.getElementById('image-form');
const imagePreview = document.getElementById('image-preview');

imageForm.addEventListener('change', function(event) {
    const imageFile = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function() {
        const img = document.createElement('img');
        img.src = reader.result;
        img.classList.add('img-fluid');
        imagePreview.innerHTML = '';
        imagePreview.appendChild(img);
    };

    if (imageFile) {
        reader.readAsDataURL(imageFile);
    }
});

// Chat Functionality
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

function addMessageToChat(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = message;
    chatMessages.appendChild(messageDiv);
}

sendButton.addEventListener('click', function() {
    const userMessage = userInput.value.trim();
    if (userMessage) {
        addMessageToChat(userMessage, 'user');

        fetch('/smart_assistant', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'query=' + encodeURIComponent(userMessage)
        })
        .then(response => response.text())
        .then(data => {
            addMessageToChat(data, 'assistant');
        })
        .catch(error => {
            console.error('Error:', error);
        });

        userInput.value = '';
        }
        });