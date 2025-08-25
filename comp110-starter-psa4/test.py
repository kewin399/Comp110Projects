import sound

# def song_generator(notestring):
#     """
#     Generates a sound object containing a song specified by the notestring.

#     Parameter:
#     notestring (type: string) - A string of musical notes and characters to
#     change the volume and/or octave of the song.

#     Returns:
#     (type: Sound) A song generated from the notestring given as a paramter.
#     """
#     sounds = sound.create_silent_sound(1)
#     note_list = ['C','D','E','F','G','A','B']
#     for n in notestring:
#         if n in note_list:
#             new_note = sound.Note(n, 14700)
#         elif n == "P":
#             new_note = sound.create_silent_sound(14700)
#         sounds = sounds + new_note
#     sound.play(sounds)

#     return sounds

def song_generator(notestring):
    """
    Generates a sound object containing a song specified by the notestring.

    Parameter:
    notestring (type: string) - A string of musical notes and characters to
    change the volume and/or octave of the song.

    Returns:
    (type: Sound) A song generated from the notestring given as a paramter.
    """
    sounds = sound.create_silent_sound(1)
    note_list = ['C','D','E','F','G','A','B']
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    found_an_int = False
    for i in range(len(notestring)):
        if (notestring[i]) in note_list:
            new_note = sound.Note((notestring[i]), 14700)
        elif notestring[i] == "P":
            new_note = sound.create_silent_sound(14700)
        elif type(int(notestring[i])) == type(1):
            new_note = sound.Note(notestring[i+1], 14700)
            print("Yay")
        sounds = sounds + new_note
      

    return sounds

# num = 13
# if type(num) == type(1):
#     print("Yay")
print(song_generator("2A4BEEE"))
