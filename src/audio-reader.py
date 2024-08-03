import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load the audio file
file_path = 'audio/test.wav'  # Path to your audio file
x, sr = librosa.load(file_path, sr=44100)  # Load with a sampling rate of 44100 Hz

# Truncate the audio to the first 10 seconds
duration = 10  # Duration in seconds
num_samples = sr * duration
x = x[:num_samples]
    
# Define STFT parameters
n_fft = 2048
hop_length = 512

# Perform STFT on the first 10 seconds
stft_result = librosa.stft(x, n_fft=n_fft, hop_length=hop_length)

# Calculate the magnitude spectrogram
magnitude = np.abs(stft_result)

# Get the frequencies corresponding to each FFT bin
frequencies = librosa.fft_frequencies(sr=sr, n_fft=n_fft)

# Define the piano frequency range
min_freq = 27.5  # A0
max_freq = 4186.0  # C8

# Find the index range for the desired frequency range
freq_idx = np.where((frequencies >= min_freq) & (frequencies <= max_freq))[0]

# Filter the spectrogram to only include the piano range
filtered_magnitude = magnitude[freq_idx, :]

# Calculate the time for each frame
times = librosa.frames_to_time(np.arange(filtered_magnitude.shape[1]), sr=sr, hop_length=hop_length)


mag = filtered_magnitude * 100 / frequencies[freq_idx, np.newaxis]

# Plot the filtered spectrogram in linear scale
plt.figure(figsize=(14, 5))
librosa.display.specshow(
    mag,
    sr=sr,
    hop_length=hop_length,
    x_axis='time',
    y_axis='linear',
    fmin=min_freq,
    fmax=max_freq
)
plt.colorbar(label='Calibrated Amplitude')
plt.title('Calibrated Piano Frequency Range Spectrogram (First 10 Seconds) - Linear Scale')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency (Hz)')
plt.show()
