import os
import pygame

# ===== music tracks =====

# LOG
print(f'Log: Music tracks loaded successfully.')

# ===== sound effects =====
SOUND_RES_PATH = f'resources{os.sep}sounds{os.sep}sound_effects{os.sep}'

TEST_SOUND = pygame.mixer.Sound(f'{SOUND_RES_PATH}test_sound_1.wav')
# "pre-loading" the sound seems to produce a beeping noise with the sound ?
# worked correctly when the Sound object was created on sound load

# LOG
print(f'Log: Sound effects loaded successfully.')


