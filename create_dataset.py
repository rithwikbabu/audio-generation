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
dataset_x = []
for i in range(0,newlen,5000):
  dataset_x.append(rounded_array[i:i+10001])

# Split dataset into values and predicted values
dataset = []
for val in dataset_x:
  dataset.append([val[:10000], val[10000:]])
