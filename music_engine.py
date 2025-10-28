# music_engine.py
# ps_chords project

# v0.1: music engine core

from mingus.core import scales as scales
from mingus.core import chords as chords

def getChord(key,degree,scale):
    match scale:
        case 0:
            # major

            scale = scales.Major(key).ascending()
            note = scale[degree - 1] 
            return chords.triad(note,key)
        case _:
            return "Invalid Scale!"
        # TODO: Natural Minor scale


while True: 
    print("Type q to quit")
    key = input("Key: ") 
    if key == 'q' : break
    degree = input("Degree: ")
    if degree == 'q' : break
    scale = input(f"Choose a scale: \n0 = Major\n > ")
    if scale == 'q' : break
    # todo: modifiers
    
    notes = getChord(key,int(degree),int(scale))
    print(notes)

