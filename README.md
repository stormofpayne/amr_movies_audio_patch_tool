# Movies Patch Tools for Alice: Madness Returns

## About This Mod
The complete mod can be found on **[Nexus Mods](https://www.nexusmods.com/alicemadnessreturns/mods/55)**.

---

## Dependencies

1. **Install Python:**
   Run the following command in CMD:
   ```cmd
   winget install Python.Python.3.12
   ```

2. **Install RADVideo Tools:**
   - Download RADVideo tools from [this page](https://www.radgametools.com/bnkdown.htm).
   - *Note: The file will have a password that is located on the download page.*
   - Extract the file -> Enter the password -> Open the `.EXE` -> Click Next -> Install.

## Important Locations

- **RADVideo Tools (Typically):** `C:\Program Files (x86)\RADVideo\radvideo64.exe`
- **Movies Folder:** `<path-of-game>/AliceGame/Movies`

## How to Run

Run the patches by executing this command in CMD:
```cmd
python voice_patch_v3.py
```

## Track IDs

| Bink ID | Language |
| :--- | :--- |
| 5 | English |
| 8 | French |
| 14 | German |
| 11 | Italian |
| 17 | EU Spanish |

## Mod Compatibility: AMR Upscaled Cutscenes

If you want to use this tool with the mod **"AMR Upscaled Cutscenes"**, you must change the following lines in `bik_voice_patch_v3.py`.

**From:**
```python
ENGLISH_TRACK_ID = 5
TRACK_TO_REPLACE = [8, 14, 11, 17]  # French, German, Italian, Spanish
```

**To:**
```python
ENGLISH_TRACK_ID = 0
TRACK_TO_REPLACE = [5, 8, 14, 11, 17]  # English, French, German, Italian, Spanish
```

*Note: This will also fix the English track ID.*
