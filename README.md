# ps-chords
psChords project - turn your Dualshock controller into a synth

This is the start of a project. The idea is to build a program that uses controller input to play music chords. Inspired by the HiChord synth.
The project is being developed for a Dualshock 4, but i plan to support other controllers; using the https://github.com/JibbSmart/JoyShockLibrary

Imagine the ps4 controller:

<img width="600" alt="ps4 controller representation" src="/controllerDrawing.png">


Now assign the notes of a scale to the buttons:
<code>
X 1  do  
C 2  re  (m)
S 3  mi  (m)
T 4  fa
d 5  sol
l 6  la  (m)
r 7  si  (dim)
</code>

Move the Left Analog LA to get a modification:
<code>
LAu   maj/min
LAd   sus4
LAr   maj/min7
LAl   dim
LAru  7
LArd  maj/min9
LAlu  aug
LAld  sus2/maj6
</code>

Move the Right Analog RA to modify the scale:
<code>
RAu    up one octave
RAd    down one octave
u+RAl  change key by -1
u+RAr  change key by +1
</code>

Use L1 and R1 to cycle through styles;
