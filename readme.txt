-------MOVIES PATCH TOOLS FOR ALICE: MADNESS RETURNS-----
-----------------CREATED BY STORMOFPAYNE-----------------

=====================================================================================

DEPENDENCIES:

Install Python using this command in CMD:
winget install Python.Python.3.12

Download RADVideo tools in this page:
https://www.radgametools.com/bnkdown.htm
(THE FILE WILL HAVE A PASSWORD THAT'S IN THAT SAME PAGE)
Extract it -> Put the password -> Open .EXE -> Next -> Install.

======================================================================================

LOCATION OF RADVIDEOTOOLS (TYPICALLY): C:\Program Files (x86)\RADVideo\radvideo64.exe
LOCATION OF MOVIES: <path-of-game>/AliceGame/Movies

======================================================================================

RUN PATCHES BY EXECUTING THIS IN CMD:
python voice_patch.py

======================================================================================

TRACK IDS

BINK ID | LANGUAGE
    5   | ENGLISH
    8   | FRENCH
    14  | GERMAN
    11  | ITALIAN
    17  | EU. SPANISH

======================================================================================

IF YOU WANT TO USE THIS TOOL WITH THE MOD "AMR Upscaled Cutscenes" YOU HAVE TO CHANGE 
THESE LINES ON "voice_patch.py":

ENGLISH_TRACK_ID = 5
TRACK_TO_REPLACE = [8, 14, 11, 17]  # French, German, Italian, Spanish

TO

ENGLISH_TRACK_ID = 0
TRACK_TO_REPLACE = [5, 8, 14, 11, 17]  # English, French, German, Italian, Spanish

THIS WILL ALSO FIX THE ENGLISH TRACK ID.