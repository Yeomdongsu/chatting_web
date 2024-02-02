from flask import request, send_file
from flask_restful import Resource
from google.cloud import texttospeech
from io import BytesIO

class TextToSpeechResource(Resource) :
    def post(self) :
        data = request.get_json()

        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=data["content"])

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code="ko-KR", name=data["type"]
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        audio_bytes = response.audio_content
    
        # # The response's audio_content is binary.
        # with open("output.mp3", "wb") as out:
        #     # Write the response to the output file.
        #     out.write(audio_content)
        #     print('성공')

        return send_file(BytesIO(audio_bytes), mimetype='audio/mpeg')