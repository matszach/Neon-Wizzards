import pygame

# mixer channels init
pygame.mixer.init()
pygame.mixer.set_num_channels(10)


# ================ MUSIC ================

# plays sound effect
def play_music(sound):
    pygame.mixer.Channel(0).play(sound)


# ================ SOUNDS ================

# next sound channel
curr_channel = [1]


# cycle through designated sound mixer channels (1-9)
def get_next_sound_channel():
    curr_channel[0] += 1
    if curr_channel[0] > 9:
        curr_channel[0] = 1
    return pygame.mixer.Channel(curr_channel[0])


# plays sound effect
def play_sound(sound):
    get_next_sound_channel().play(sound)



