import numpy as np
import matplotlib.pyplot as plt
import mne
from mne.viz import set_browser_backend
from processes import load_dat, load_labels, load_detected_swds_labels, save_manual_annotation_on_close
from parameters import taini_data_path, animal_id, label_file_path, sample_rate, start_sample, end_sample, eeg_1, eeg_2, \
    previously_annotated, first_from_automatically_detected

# create MNE raw object for interactive plotting
print("Animal: SCN2A_" + animal_id)

custom_raw = load_dat(taini_data_path)

# define time period to quantify over
tmin = start_sample / sample_rate
tmax = end_sample / sample_rate

# Create interactive plot of 24-hour window
set_browser_backend('matplotlib')
# set_browser_backend('qt')

if previously_annotated == True:
    if first_from_automatically_detected == True:
        
        # Load in existing automatic labels
        annotations = load_detected_swds_labels(label_file_path, tmin)
    else:
        
        # Load in existing manual labels
        annotations = load_labels(label_file_path)

    # created annotated raw object
    annot_custom_raw = custom_raw.set_annotations(annotations)

    # plot annotated raw object
    labels = annot_custom_raw.crop(tmin, tmax).plot(None, 60, 0, 2, scalings="auto", order=[eeg_1 - 1, eeg_2 - 1],
                                                    show_options="true", block=True)
    save_manual_annotation_on_close(annot_custom_raw, tmin, animal_id + "_annotations.csv")


else:

    # plot un-annotated object
    labels = custom_raw.crop(tmin, tmax).plot(None, 60, 0, 2, scalings="auto", order=[eeg_1 - 1, eeg_2 - 1],
                                              show_options="true", block=True)
    save_manual_annotation_on_close(custom_raw, tmin, animal_id + "_annotations.csv")

