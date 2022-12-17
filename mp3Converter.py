import os
from scipy.io.wavfile import read

os.system("ffmpeg -i magicInTheAir.mp3.mp3 -vn -acodec pcm_s16le -ac 1 -ar 44100 -f wav foo.wav")