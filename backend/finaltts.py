
from google.cloud import texttospeech


tts_client = texttospeech.TextToSpeechClient()

def generate_tts(text: str) -> bytes:
    """Generate TTS audio in MP3 format with fixed Hindi Male voice."""
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="hi-IN",
        name="hi-IN-Wavenet-B",   
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = tts_client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    return response.audio_content

