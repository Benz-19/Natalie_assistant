from app.core.speech_to_text import listen, convert_to_text
from app.core.text_to_speech import speak

def process_command(text):
    if text is None:
        speak("Sorry, I couldn't understand that.")
        return

    if "hello" in text:
        response = "Hi, I’m Natalie, your assistant."
    elif "how are you" in text:
        response = "I'm functioning properly. How can I assist you today?"
    elif "what is your name" in text:
        response = "My name is Natalie."
    else:
        response = "I'm not sure how to respond to that yet."

    print(f"Natalie: {response}")
    speak(response)

if __name__ == "__main__":
    while True:
        audio_data = listen()
        command = convert_to_text(audio_data)
        process_command(command)
