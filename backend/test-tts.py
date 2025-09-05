from google.cloud import texttospeech

def test_tts():
    # Initialize client
    client = texttospeech.TextToSpeechClient()

    # Set text input
    synthesis_input = texttospeech.SynthesisInput(text="Hello! Your Google Cloud Text to Speech is working.")

    # Choose voice
    voice = texttospeech.VoiceSelectionParams(
    language_code="hi-IN",
    name="hi-IN-Wavenet-B",   # <--- exact name you found
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

    # Select audio config
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Generate response
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # Save output to file
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print("✅ Audio content written to output.mp3")

if __name__ == "__main__":
    test_tts()
