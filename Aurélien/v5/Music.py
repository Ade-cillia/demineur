'''
mixer.init()
mixer.music.load("music1.wav")
mixer.music.set_volume(0.05)
mixer.music.play(-1)

def music():                        #Selectionne une musique aléatoirement dans notre liste
    global music
    global music_jouer
    music_jouer = None
    music= ["music_noragami.ogg"]
    music_suivant = choice(music)
    while music_suivant == music_jouer:
        music_suivant = choice(music)
    music_jouer = music_suivant
    mixer.music.load(music_suivant)
    mixer.music.set_volume(0.05)
    mixer.music.play()

'''
#music()