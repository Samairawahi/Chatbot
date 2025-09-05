from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()


voices = client.list_voices().voices


for voice in voices:
    if "hi-IN" in voice.language_codes:
        print("Name:", voice.name)
        print("Language Codes:", voice.language_codes)
        print("Gender:", texttospeech.SsmlVoiceGender(voice.ssml_gender).name)
        print("Natural Sample Rate Hertz:", voice.natural_sample_rate_hertz)
        print("-" * 40)

