import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt 

x = librosa.load('audio/test.wav')[0]
magnitude = np.abs(librosa.stft(x))
log_spectrogram = librosa.amplitude_to_db(magnitude)

plt.figure(figsize=(10,4))
librosa.display.specshow(log_spectrogram)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar(format='%+2.0f dB')
plt.title("Spectrogram (dB)")
plt.xscale('linear')
plt.yscale('linear')
plt.show()