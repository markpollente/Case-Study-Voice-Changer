# Development Of An Audio Voice Modulator

## Requirements
- Python 3.x
- `pydub` library
- `numpy` library
- `.wav` file

## Usage

### 1. Installation
Install the required libraries using `pip`:
```python
pin install pydub
pip install numpy
```

### 2. Run the Script
1. Place the correct file path of the audio file in the `original` variable.
2. Choose the save file path of the modfied file in the `modified` variable and its file name at the end. Make sure it's a .wav file.
2. Open a terminal and change directory to the script's directory.
3. Run the script using the command:
```python
py voicechanger.py
```

### 3. Parameters
- `semitonesAdjust`: Adjust this value to change the pitch of the output audio. Positive values increase pitch, negative values decrease pitch.
- `speedAdjust`: Adjust this value to change the speed of the output audio. Values less than 1 slow down the audio, values greater than 1 speed up the audio.

### 4. Output
The modified audio is saved to the specified directory (`modified` variable) with the specified name.

### Note
- Make sure to adjust the semitonesAdjust and speedAdjust variables according to your preferred output voice before running the script.
- Ensure that the audio file exists and the file path is correctly specified.

### Credits
- zakee001 - used this user's script as the learning material and to achieve the desired results. I do not claim the script myself. 
- Mikayla13 - used this youtube user's video clip
