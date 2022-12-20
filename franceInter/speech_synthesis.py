import azure.cognitiveservices.speech as speechsdk
from translator_app import traduction

def speech(message):
    speech_config = speechsdk.SpeechConfig(subscription="55c6c6f626e04eb7b032dcb725b1cab1", region="westeurope")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    textEn = traduction(message)

    en =  speech_synthesizer.speak_text_async(textEn).get()
    stream = speechsdk.AudioDataStream(en)
    stream.save_to_wav_file("audioEn.wav")

    textFr = message

    fr =  speech_synthesizer.speak_text_async(textFr).get()
    stream = speechsdk.AudioDataStream(fr)
    stream.save_to_wav_file("audioFr.wav")
