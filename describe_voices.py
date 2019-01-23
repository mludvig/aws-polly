#!/usr/bin/env python3

# describe_voices.py - describe and play all AWS Polly voices
# Author Michael Ludvig

import boto3
from audio_helper import play_audio_stream

polly = boto3.client('polly')

response = polly.describe_voices()  # Optional param: LanguageCode='en-US'
voices = response['Voices']
print("AWS Polly currently supports {} voices".format(len(voices)))

for voice in voices:
    text = "Hi, my name is {Name} and I speak {LanguageName}".format(**voice)
    print(text)

    ssml_text = '''<speak>
        Hi, my name is
        <lang xml:lang="{LanguageCode}">{Name}</lang>
        and I speak {LanguageName}.
    </speak>'''.format(**voice)
    response = polly.synthesize_speech(OutputFormat='ogg_vorbis',
        LanguageCode='en-GB', VoiceId=voice['Id'],
        TextType='ssml', Text=ssml_text)
    play_audio_stream(response['AudioStream'])
