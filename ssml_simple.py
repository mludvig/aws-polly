#!/usr/bin/env python3

# ssml_simple.py - Basic SSML-enhanced text output
# Author Michael Ludvig

# Import play_audio_stream() from audio_helper.py
from audio_helper import play_audio_stream

# Boto3 is the AWS SDK for Python
import boto3

# Initialise AWS Polly client
# AWS Credentials will be read from ~/.aws/credentials
polly = boto3.client('polly')


# SSML-enhanced text
ssml_text = '''
<speak>
Let me tell you a secret.
<break time="1s" />
<amazon:effect name="whispered">Amazon Alexa is my sister!</amazon:effect>
</speak>
'''
response = polly.synthesize_speech(OutputFormat='ogg_vorbis', VoiceId='Emma',
           TextType='ssml', Text=ssml_text)

# Play the returned audio stream - call the function from audio_helper.py
play_audio_stream(response['AudioStream'])
