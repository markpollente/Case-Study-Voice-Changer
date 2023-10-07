from pydub import AudioSegment
import numpy as np

def pitchAndSpeed(sound, semitones, speed):
    samples = np.array(sound.get_array_of_samples())
    semitone_ratio = 2 ** (semitones / 12.0)
    pitch_shifted_samples = np.interp(np.arange(0, len(samples), semitone_ratio), np.arange(0, len(samples)), samples).astype(np.int16)
    sample_width = sound.sample_width
    channels = sound.channels
    new_length = int(len(pitch_shifted_samples) / (speed * semitone_ratio)) // (sample_width * channels) * (sample_width * channels)
    modified_samples = np.interp(np.linspace(0, len(pitch_shifted_samples) - 1, new_length), np.arange(0, len(pitch_shifted_samples)), pitch_shifted_samples).astype(np.int16)
    new_sound = AudioSegment(modified_samples.tobytes(), frame_rate=int(sound.frame_rate * speed), sample_width=sample_width, channels=channels)
    return new_sound

def main():
    original = "C:\\Users\\Mark\\OneDrive\\Documents\\DSP\\Corpuz.wav"
    sound = AudioSegment.from_file(original)

    semitonesAdjust = 2
    speedAdjust = 1 

    modifyVoice = pitchAndSpeed(sound, semitonesAdjust, speedAdjust)

    modified = "C:\\Users\\Mark\\OneDrive\\Documents\\DSP\\corpuzDubbed2.wav"  
    modifyVoice.export(modified, format="wav")

if __name__ == "__main__":
    main()
