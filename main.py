import numpy as np
import matplotlib.pyplot as plt
import mne

from mne.viz import set_browser_backend
from processes import load_dat, load_labels
from parameters import taini_data_path, label_file_path, sample_rate, start_sample, end_sample

#create MNE raw object for interactive plotting
custom_raw = load_dat(taini_data_path)

#Load in existing labels
annotations = load_labels(label_file_path)

#Create interactive plot of 24-hour window
set_browser_backend('qt')
annot_custom_raw = custom_raw.set_annotations(annotations)

tmin = start_sample/sample_rate
tmax = end_sample/sample_rate
annot_custom_raw.crop(tmin, tmax).plot(scalings = "auto", order=[0,1,2,3,4,6,7,8,9,10,11,12,13,14, 15], show_options = "true", block=True)