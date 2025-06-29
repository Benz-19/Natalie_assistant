from app.core.speech_to_text import listen, convert_to_text
from app.core.text_to_speech import speak
from app.services.openai_service import get_ai_response

if __name__ == "__main__":
    while True:
        print("Listening for your command...")
        audio_data = listen()
        command = convert_to_text(audio_data)

        if command is None:
            speak("Sorry, I didn’t catch that.")
            continue

        print(f"You said: {command}")
        response = get_ai_response(command)
        print(f"Natalie: {response}")
        speak(response)
