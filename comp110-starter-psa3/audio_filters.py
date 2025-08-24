"""
Module: audio_filters

Authors:
1) Cavin Nguyen - cavinnguyen@sandiego.edu
2) Jessica Cervantes - jessicacervantes@sandiego.edu
"""

import sound

def remove_vocals(original_sound):
    """
    Creates a new sound object that is the same as the given sound, but with
    the vocals having been removed.

    Parameters:
    original_sound (type: Sound) - The original Sound object

    Returns:
    Sound object - Same sound as the original, but with vocals removed
    """
    # for sample_number in range(len(copy_sound)):
    #     sample = copy_sound[sample_number]

    #     # change the left channel
    #     new_sound_val = sample * int(multiplier)
    #     sample = new_sound_val

    new_sound = sound.copy(original_sound)
    for i in range(len(new_sound)):
        s = new_sound[i]
        new_value = (s.left - s.right) // 2
        s.left = new_value
        s.right = new_value
        
    return new_sound


def fade_in(original_sound, fade_length):
    """
    Creates a new sound object that is the same as the given sound, but with
    the sound fading in.

    Parameters:
    original_sound (type: Sound) - The original Sound object, fade_length (type: int) - The length of the sample that will be faded in.
    Returns:
    Sound object - Same sound as the original, but with the sound fading in to a certain length.
    """
    new_sound = sound.copy(original_sound)
    for i in range(fade_length):
        s = new_sound[i]
        new_value_left = s.left/fade_length * i 
        new_value_right = s.right/fade_length * i
        s.left = int(new_value_left)
        s.right = int(new_value_right)
        
    return new_sound


def fade_out(original_sound, fade_length):
    """
    Creates a new sound object that is the same as the given sound, but with the sound fading out.

    Parameters:
    original_sound (type: Sound) - The original Sound object, fade_length (type: int) - The length of the sample that will be faded out.
    Returns:
    Sound object - Same sound as the original, but with the sound fading out to a certain length.
    """

    new_sound = sound.copy(original_sound)
    
    for i in range(fade_length):
        s = new_sound[-i]
        if i == 0:
            new_value_left = s.left
            new_value_right = s.right
        else:
            new_value_left = s.left/fade_length * (i) 
            new_value_right = s.right/fade_length * (i)
        s.left = int(new_value_left)
        s.right = int(new_value_right)
        
    return new_sound

def fade(original_sound, fade_length):
    """
    Calls two functions, fade_in() and fade_out() and callss the two new sound object that is the same as the given sound, but with the sound fading in and out.

    Parameters:
    original_sound (type: Sound) - The original Sound object, fade_length (type: int) - The length of the sample that will be faded out.
    Returns:
    Sound object - Same sound as the original, but with the sound fading in and out to a certain length.
    """
    #new_sound = sound.copy(original_sound)

    return fade_out(fade_in(original_sound, fade_length), fade_length)

def left_to_right(original_sound, pan_length):
    """
    Pans the audio from with the sound fading in and out, and the channels treated as reciprocals for their multipliers.
    The left channel starts at max volume and begins to fade out, while the right channel fades in so that there is a panning effect.

    Parameters:
    original_sound (type: Sound) - The original Sound object
    Returns:
    Sound object - Same sound as the original, but with the sound fading from left to right in and out to a certain length.
    """
    new_sound = sound.copy(original_sound)
    for i in range(pan_length):
        s = new_sound[i]
        new_value_left = s.left * (1 - 1/pan_length * i)
        new_value_right = s.right/pan_length * i
        s.left = int(new_value_left)
        s.right = int(new_value_right)

    return new_sound


# Your final submission should NOT contain any global code.
# In other words, all your code should be contained in the functions defined
# above.



# WARNING: DO NOT MODIFY ANYTHING BELOW THIS LINE!!!

def main():
    '''
    The main function allows for selections to be made to test the sound functions.
    '''
    import os.path

    options = {
                1: ("remove_vocals", None),
                2: ("fade_in", "fade_length"),
                3: ("fade_out", "fade_length"),
                4: ("fade", "fade_length"),
                5: ("left_to_right", "pan_length")
            }

    print("The following functions are available.\n")
    print("(1) remove_vocals")
    print("(2) fade_in")
    print("(3) fade_out")
    print("(4) fade")
    print("(5) left_to_right")

    selection = int(input("\nEnter the number of the function to test: "))

    if selection not in range(1, 6):
        print("Invalid selection. Please run the tester again.")
        return

    wav_file = input("Enter the name of the wav file to test with: ")

    # Make sure the file exists so we don't get an error trying to open a
    # file that isn't there.
    if not os.path.isfile(wav_file):
        print("\nTest Failed: The file you typed does not exist. Try again.")
        return

    # create a sound object then call the selected function
    original_sound = sound.load_sound(wav_file)
    test_function_name = options[selection][0]
    test_function = globals()[test_function_name]

    # Have user enter value for the parameter if one exists
    has_parameter = options[selection][1] is not None

    while has_parameter:
        param_name = options[selection][1]
        param_value = int(input("Enter a value for %s: " % param_name))

        # TODO: check that it is not greater than sound's length?
        if param_value < 1:
            print("Invalid selection.", param_name, "must be a positive integer.")
        else:
            break
    

    # TODO: run this in a try-catch 
    if has_parameter:
        filtered_sound = test_function(original_sound, param_value)
    else:
        filtered_sound = test_function(original_sound)

    # Check that the function gave back a sound
    if filtered_sound is None:
        print("\nTest Failed:", test_function_name, "does not return a sound. Did you forget the return statement?")
        return

    # Allow the user to play or display the original or filtered sounds
    while True:
        print("\nThe following options are available:\n")
        print("(1) Play original sound.")
        print("(2) Play filtered sound.")
        print("(3) Display original sound waveforms.")
        print("(4) Display filtered sound waveforms.")
        print("(5) Exit this program.")

        selection = int(input("\nEnter your selection: "))
        if selection not in range(1, 6):
            print("Invalid selection. Enter a number between 1 and 5.")
        elif selection == 1:
            original_sound.play()
            sound.wait_until_played()
        elif selection == 2:
            filtered_sound.play()
            sound.wait_until_played()
        elif selection == 3:
            original_sound.display()
        elif selection == 4:
            filtered_sound.display()
        elif selection == 5:
            break

if __name__ == "__main__":
    main()
