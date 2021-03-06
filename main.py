from scipy.io import wavfile
import numpy as np
import pygame
import os
import sys

key_sounds = {}

def register_sound(key, sound):
    key_sounds[key] = sound

def register_sounds():
    register_sound(pygame.K_a, pygame.mixer.Sound("A4.wav"))
    register_sound(pygame.K_s, pygame.mixer.Sound("B4.wav"))
    register_sound(pygame.K_d, pygame.mixer.Sound("C5.wav"))
    register_sound(pygame.K_f, pygame.mixer.Sound("D5.wav"))
    register_sound(pygame.K_g, pygame.mixer.Sound("E5.wav"))
    register_sound(pygame.K_h, pygame.mixer.Sound("F5.wav"))
    register_sound(pygame.K_j, pygame.mixer.Sound("G5.wav"))
    register_sound(pygame.K_k, pygame.mixer.Sound("A5.wav"))

def init():
        rate, sound = wavfile.read('A4.wav')
        pygame.mixer.init(rate, -16, 1, 2048)
        register_sounds()
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.display.set_caption('Keyboard')
        screen = pygame.display.set_mode((800, 600))



def playSound(key_obj):
    pygame.mixer.Sound.play(key_sounds[key_obj])
    pygame.mixer.music.stop()


def startPiano():
    init()
    shouldQuit = False
    while not shouldQuit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key in key_sounds:
                    playSound(event.key)
                if event.key == pygame.K_q:
                    shouldQuit = True
            elif event.type == pygame.KEYUP:
                pass
            if event.type == pygame.QUIT:
                shouldQuit = True



if __name__ == "__main__":
    startPiano()