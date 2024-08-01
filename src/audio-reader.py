import pywt
import scipy.io.wavfile


wavefile = 'path to the wavefile'
# read the wavefile
sampling_frequency, signal = scipy.io.wavfile.read(wavefile)
#
scales = (1, len(signal))
coefficient, frequency = pywt.cwt(signal, scales, 'wavelet_type')

