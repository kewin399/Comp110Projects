"""
Module: song_generator

Module with functions for PSA #4 of COMP 110 (Fall 2019).

Authors:
1) Jessica Cervantes - jessicacervantes@sandiego.edu
2) Cavin Nguyen - cavinnguyen@sandiego.edu
"""

import sound

# Do NOT modify the scale_volume function
def scale_volume(original_sound, factor):
    """
    Decreases the volume of a sound object by a specified factor.

    Paramters:
    original_sound (type; Sound): The sound object whose volume is to be decreased.
    factor (type: float): The factor by which the volume is to be decreased.

    Returns:
    (type: Sound) A new sound object that is a copy of original_sound, but with volumes
    scaled by factor.
    """

    scaled_sound = sound.copy(original_sound)

    for smpl in scaled_sound:
        # Scale left channel of smpl
        current_left = smpl.left
        scaled_left = round(current_left * factor)
        smpl.left = scaled_left

        # Scale right channel of smpl
        current_right = smpl.right
        scaled_right = round(current_right * factor)
        smpl.right = scaled_right

    return scaled_sound


def mix_sounds(snd1, snd2):
    """
    Mixes together two sounds (snd1 and snd2) into a single sound.
    If the sounds are of different length, the mixed sound will be the length
    of the longer sound.

    This returns a new sound: it does not modify either of the original
    sounds.

    Parameters:
    snd1 (type: Sound) - The first sound to mix
    snd2 (type: Sound) - The second sound to mix

    Returns:
    (type: Sound) A Sound object that combines the two parameter sounds into a
    single, overlapping sound.
    """


    snd1copy = sound.copy(snd1)
    snd2copy = sound.copy(snd2)

    print(snd1)
    print(snd2)
    print(snd1copy)
    print(snd2copy)

    if len(snd1copy) > len(snd2copy):
        longer_sound = snd1copy
        shorter_sound = snd2copy
    
    else:
        longer_sound = snd2copy
        shorter_sound = snd1copy

    for i in range(len(shorter_sound)):
        longer_s = longer_sound[i]
        shorter_s = shorter_sound[i]
        longer_s.left = longer_s.left + shorter_s.left
        longer_s.right = longer_s.right + shorter_s.right

    return longer_sound


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
    sounds_2nd = sound.create_silent_sound(1)
    note_list = ['C','D','E','F','G','A','B']
    level = 0
    level_2nd  = 0
    found_int = False
    found_vert = False
    vol_one = 1.0
    vol_two = 1.0
    for i in range(len(notestring)):
        if notestring[i] == "|":
            found_vert = True
        if found_vert == False and notestring[i] == ">":
            level += 1
        elif found_vert == False and notestring[i] == "<":
            level += -1
        elif found_vert == True and notestring[i] == ">":
            level_2nd += 1
        elif found_vert == True and notestring[i] == "<":
            level_2nd -= 1
        
        if found_vert == False and notestring[i] == "+":
            vol_one += .2
        elif found_vert == False and notestring[i] == "-":
            vol_one -= .2
        elif found_vert == True and notestring[i] == "+":
            level_2nd += .2
        elif found_vert == True and notestring[i] == "-":
            level_2nd -= .2
        
        if found_vert == False and (found_int == False) and (notestring[i] in note_list):
            new_note = sound.Note(notestring[i], 14700, octave=level)
            new_note = scale_volume(new_note, vol_one)
            found_int = False
            sounds = sounds + new_note
        elif found_vert == False and found_int == False and notestring[i] == "P":
            new_note = sound.create_silent_sound(14700)
            found_int = False           
            sounds = sounds + new_note
        elif found_vert == False and notestring[i].isdigit():
            found_int = True
            if notestring[i+1] == "P":
                new_note = sound.create_silent_sound(14700)
            else:
                new_note = sound.Note(notestring[i+1], 14700*(int(notestring[i])), octave=level)
            new_note = scale_volume(new_note, vol_one)
            sounds = sounds + new_note
        elif found_vert == True and (found_int == False) and (notestring[i] in note_list):
            new_note = sound.Note(notestring[i], 14700, octave=level_2nd)
            found_int = False
            new_note = scale_volume(new_note, vol_two)
            sounds_2nd = sounds_2nd + new_note
        elif found_vert == True and found_int == False and notestring[i] == "P":
            new_note = sound.create_silent_sound(14700)
            found_int = False           
            sounds_2nd = sounds_2nd + new_note
        elif found_vert == True and notestring[i].isdigit():
            found_int = True
            if notestring[i+1] == "P":
                new_note = sound.create_silent_sound(14700)
            else:
                new_note = sound.Note(notestring[i+1], 14700*(int(notestring[i])), octave=level_2nd)
            new_note = scale_volume(new_note, vol_two)
            sounds_2nd = sounds_2nd + new_note
        else:
            found_int = False
    
    if found_vert == True:
        return mix_sounds(sounds, sounds_2nd)
    else:
        return sounds


"""
Don't modify anything below this point.
"""

def main():
    """
    Asks the user for a notestring, generates the song from that
    notestring, then plays the resulting song.
    """
    import sounddevice
    print("Enter a notestring (without quotes):")
    ns = input()
    song = song_generator(ns)
    song.play()
    sounddevice.wait()

if __name__ == "__main__":
    main()