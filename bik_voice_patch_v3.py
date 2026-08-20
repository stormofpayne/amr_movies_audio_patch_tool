import os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askdirectory

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
TEMP_DIR = os.path.join(CURRENT_DIR, "temp")

ENGLISH_TRACK_ID = 5
TRACK_TO_REPLACE = [8, 14, 11, 17]  # French, German, Italian, Spanish

EXCLUDE_BIK_LIST = [
    "DEMO_Trailer.bik",
    "Intro_EA.bik",
    "Intro_Nvidia.bik",
    "Intro_SH.bik",
    "LoadingMovie.bik",
    "TechLogo_Short.bik",
]

rad_tool_path = ""
alice_movies_folder = ""

# Create temp folder if it doesn't exist
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# Folder Selection
while True:
    rad_video_tools = "C:/Program Files (x86)/RADVideo/radvideo64.exe"
    if os.path.exists(rad_video_tools):
        rad_tool_path = rad_video_tools
        break
    
    print("Please select RADVideo folder")
    Tk().withdraw()
    rad_video_tools = os.path.normpath(askdirectory(title="Select RADVideo folder"))

    if rad_video_tools == "":
        print("User has cancelled the selection. Exiting program.")
        exit()

    if os.path.exists(os.path.join(rad_video_tools, "radvideo64.exe")):
        rad_tool_path = os.path.normpath(os.path.join(rad_video_tools, "radvideo64.exe"))
        break
    else:
        print("Invalid RADVideo folder. Please try again.")

print("RADVideo Tool path:", rad_tool_path)

while True:
    print("Please select Alice MOVIES folder")
    Tk().withdraw()
    alice_movies_folder = os.path.normpath(askdirectory(title="Select Alice Movies folder"))

    if alice_movies_folder == "":
        print("User has cancelled the selection. Exiting program.")
        exit()

    if os.path.exists(alice_movies_folder):
        break
    else:
        print("Invalid Alice folder. Please try again.")

for filename in os.listdir(alice_movies_folder):
    if filename.endswith(".bik") and filename not in EXCLUDE_BIK_LIST:
        print(f"Converting {filename}")

        original_path = os.path.join(alice_movies_folder, filename)
        wav_output_path = os.path.join(CURRENT_DIR, "temp", f"{os.path.splitext(filename)[0]}__english.wav")

        # Extract audio from BIK to WAV
        binkconv_cmd = [
            f'"{rad_tool_path}"',
            "BinkConv",
            f'"{original_path}"',
            f'"{wav_output_path}"',
            "/o", # Overwrite
            "/v",
            f"/n{ENGLISH_TRACK_ID}",
            "/#", # don't wait for user interaction
        ]
        
        print(f"Extracting English audio: {' '.join(binkconv_cmd)}")
        try:
            subprocess.run(
                " ".join(binkconv_cmd),
                shell=True,
                check=False,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"Error extracting English audio: {e}")
            continue
        print(f"Extracting English audio completed")
        
        # Mix English audio to all language tracks
        for track in TRACK_TO_REPLACE:
            binkmix_cmd = [
                f'"{rad_tool_path}"',
                "BinkMix",
                f'"{original_path}"', # INPUT FILE
                f'"{wav_output_path}"', # ENGLISH AUDIO
                f'"{original_path}"', # OUTPUT FILE
                "/o", # Overwrite
                "/l0", # Sound Compression Level
                f"/t{track}", # Track ID
                "/#", # don't wait for user interaction
            ]
            print(f"Mixing track {track}: {' '.join(binkmix_cmd)}")
            try:
                subprocess.run(
                    " ".join(binkmix_cmd),
                    shell=True,
                    check=False,
                    capture_output=True,
                    text=True,
                )
            except subprocess.CalledProcessError as e:
                print(f"Error mixing track {track}: {e}")
                continue
            print(f"Mixing track {track} completed")
        
        print(f"Process completed for {filename}")
        
# Cleanup
print("Cleaning up temp folder")
for filename in os.listdir(TEMP_DIR):
    os.remove(os.path.join(TEMP_DIR, filename))
    
print("Process completed")