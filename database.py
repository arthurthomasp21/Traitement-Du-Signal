"""
Create a database containing the hashcodes of the songs stored 
in the specified folder (.wav files only). 
The database is saved as a pickle file as a list of dictionaries.
Each dictionary has two keys 'song' and 'hashcodes', corresponding 
to the name of the song and to the hashcodes used as signature for 
the matching algorithm.
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.io.wavfile import read
from algorithm import *


# ----------------------------------------------
# Run the script
# ----------------------------------------------
if __name__ == '__main__':

    folder = 'C:\\Users\\arthu\\Desktop\\Cours\\Info\\Traitement-Du-Signal\\samples'

    # 1: Load the audio files
    import os
    audiofiles = os.listdir(folder)
    audiofiles = [item for item in audiofiles if item[-4:] =='.wav']

    # 2: Set the parameters of the encoder
    wsize = 128
    ovsize = 32

    # 3: Construct the database
    database = []
    for audiofile in audiofiles :
        encoder = Encoding(wsize, ovsize)
        fs, s = read(audiofile)
        encoder.process(fs, s)
        encoder.display_spectrogram(display_anchors=True)
        database.append(encoder)


    # 4: Save the database
    with open('songs.pickle', 'wb') as handle:
        pickle.dump(database, handle, protocol=pickle.HIGHEST_PROTOCOL)



