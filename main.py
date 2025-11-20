import numpy as np
import matplotlib.pyplot as plt
import mne
from mne.viz import set_browser_backend
from processes import load_dat, load_labels, save_manual_annotation_on_close
from parameters import taini_data_path, animal_id, label_file_path, sample_rate, start_sample, end_sample, eeg_1, eeg_2, \
    previously_annotated

# create MNE raw object for interactive plotting
print("Animal: SCN2A_" + animal_id)

custom_raw = load_dat(taini_data_path)

# Create interactive plot of 24-hour window
set_browser_backend('matplotlib')
# set_browser_backend('qt')

if previously_annotated == True:

    # Load in existing labels
    annotations = load_labels(label_file_path)
    print(annotations)

    # created annotated raw object
    annot_custom_raw = custom_raw.set_annotations(annotations)

    # plot annotated raw object
    tmin = start_sample / sample_rate
    tmax = end_sample / sample_rate
    labels = annot_custom_raw.crop(tmin, tmax).plot(None, 60, 0, 2, scalings="auto", order=[eeg_1 - 1, eeg_2 - 1],
                                                    show_options="true", block=True)
    save_manual_annotation_on_close(annot_custom_raw, tmin, animal_id + "_annotations.csv")

else:

    # plot un-annotated object
    tmin = start_sample / sample_rate
    tmax = end_sample / sample_rate
    labels = custom_raw.crop(tmin, tmax).plot(None, 60, 0, 2, scalings="auto", order=[eeg_1 - 1, eeg_2 - 1],
                                              show_options="true", block=True)
    save_manual_annotation_on_close(custom_raw, tmin, animal_id + "_annotations.csv")


