# File Path
file_path = "audio.wav"

# Imports
import soundfile as sf

# Load File
x, fs = sf.read(file_path)

# Round Array
n = len(x)
newlen = round(n/10000)*10000
rounded_array = x[:newlen]

# Make Dataset with Sliding Window
dataset = []
for i in range(0,newlen,5000):
  dataset.append(rounded_array[i:i+100000])
