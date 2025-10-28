# ps-chords
psChords project - turn your Dualshock controller into a synth

This is the start of a project. The idea is to build a program that uses controller input to play music chords. Inspired by the HiChord synth.
The project is being developed for a Dualshock 4, but i plan to support other controllers.

### Development plan

Logic:
- Read the controller input with ```inputs```;
- Use ```mingus```, a music theory library to translate the inputs into chord notes;
- Send the notes as MIDI messages to a virtual MIDI port using ```mido```.

For the TUI, ```rich```;

For the virtual MIDI port:  
on Windows, ```loopMIDI```;  
on Linux, ```snd-virmidi```;  

A separate synth program will read the port and make the sounds. Options for the synth: 
VCV Rack (modular, a bit complex);.
Vital (wavetable).
Helm (simpler, but powerful).
Surge XT (great features).

**main.py** - Main loop (reads controller, updates TUI)

**controller.py** - class/functions for inputs

**music_engine.py** - class to hold state (key, octave, mod) and use mingus

**midi_handler.py** - class for the mido port and send note_on/note_off

**tui.py** - class for the rich.live display

### Inputs
Imagine the ps4 controller:

<img width="600" alt="ps4 controller representation" src="/controllerDrawing.png">


Now assign the degrees of a scale to the buttons:
```
X 1  do  
C 2  re  (m)
S 3  mi  (m)
T 4  fa
d 5  sol
l 6  la  (m)
r 7  si  (dim)
```

Move the Left Analog LA to get a modification:
```
LAu   maj/min
LAd   sus4
LAr   maj/min7
LAl   dim
LAru  7
LArd  maj/min9
LAlu  aug
LAld  sus2/maj6
```

Move the Right Analog RA to modify the scale:
```
RAu    up one octave
RAd    down one octave
u+RAl  change key by -1
u+RAr  change key by +1
```

Use L1 and R1 to cycle through styles;
