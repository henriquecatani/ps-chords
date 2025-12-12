from mingus.core import scales as scales
from mingus.core import chords as chord

# teste.py 
# for testing the program logic

# 1 - scale selection - note, type - returns scale list
# 2 - chord selection - degree - index of the scale list
# 3 - chord calc - if degree 2, 3, 6 = minor triad, 7 = dim, else major - returns triad list

def scaleSelect(note, typeScale):
    # expandable for more types
    match typeScale:
        case "major":
            return scales.Major(note).ascending()
        case "natural minor":
            return scales.NaturalMinor(note).ascending()

def getChord(degree,scale):
    selectedChord = scale[degree - 1]
    if degree in [2,3,6]:
        return chord.major_triad(selectedChord)
    elif degree == 7:
        return chord.diminished_triad(selectedChord)
    else:
        return chord.major_triad(selectedChord)
    
noteScale = input("Which note would you like to select the scale? ")
typeScale = input("Type which scale you want: \nmajor\nnatural minor\n> ")
selectedScale = scaleSelect(noteScale, typeScale)
print("Selected Scale: ", noteScale, typeScale, selectedScale)
degreeScale = int(input("What degree would you want to play? "))
selectedChord = getChord(degreeScale, selectedScale)
print(selectedChord)