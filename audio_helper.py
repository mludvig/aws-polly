#!/usr/bin/env python3

# audio_helper.py - simple PyGame audio player
# Author Michael Ludvig

import io
import pygame

# PyGame initialisation - upon module loading
pygame.init()
pygame.mixer.init()

# Convert boto3 audio stream to Bytes stream
# for compatibility with pygame
def play_audio_stream(audio_stream):
    audio = io.BytesIO(audio_stream.read())
    play_audio(audio)

# Here we play the audio stream
def play_audio(audio):
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
