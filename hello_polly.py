#!/usr/bin/env python3

# hello_polly.py - Simple AWS Polly demo
# Author Michael Ludvig

# Import play_audio_stream() from audio_helper.py
from audio_helper import play_audio_stream

# Boto3 is the AWS SDK for Python
import boto3

# Initialise AWS Polly client
# AWS Credentials will be read from ~/.aws/credentials
polly = boto3.client('polly')

# Synthesise Text to OGG Vorbis audio
response = polly.synthesize_speech(OutputFormat='ogg_vorbis', VoiceId='Brian',
             Text='Hello, I am Polly! Even though I sound like Brian.')

# Play the returned audio stream - call the function from audio_helper.py
play_audio_stream(response['AudioStream'])
