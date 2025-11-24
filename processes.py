import os
import numpy as np
import pandas as pd
import glob
import mne

from parameters import number_of_channels, sample_rate, sample_datatype, display_decimation


def load_dat(filename):
    '''Load a .dat file by interpreting it as int16 and then de-interlacing the 16 channels'''

    print("Loading_" + filename)

    # Load the raw (1-D) data
    dat_raw = np.fromfile(filename, dtype=sample_datatype)

    # Reshape the (2-D) per channel data
    step = number_of_channels * display_decimation
    dat_chans = [dat_raw[c::step] for c in range(number_of_channels)]

    # Build the time array
    t = np.arange(len(dat_chans[0]), dtype=float) / display_decimation

    # Build the data array
    data = np.array(dat_chans)

    # Build info for MNE raw object
    n_channels = 16

    channel_names = ['1', '2', '3', '4', '5',
                     '6', '7', '8', '9', '10',
                     '11', '12', '13', '14', '15', '16']
    channel_types = ['emg', 'misc', 'eeg', 'misc', 'misc', 'misc', 'emg', 'misc', 'misc', 'misc', 'misc', 'misc',
                     'misc', 'misc', 'misc', 'eeg']

    info = mne.create_info(channel_names, sample_rate, channel_types)

    # Build MNE raw object
    custom_raw = mne.io.RawArray(data, info)

    return custom_raw


def load_labels(filename):
    print("Loading_" + filename)

    read_labels = pd.read_table(
        filename,
        delimiter=',',
        skiprows=1,
        header=None)

    annotations = mne.Annotations(
        onset=read_labels.iloc[:, 1],
        duration=read_labels.iloc[:, 2],
        description=read_labels.iloc[:, 0],
        orig_time=None)

    print("Annotations loaded.")
    return annotations


def load_detected_swds_labels(filename, tmin):
    print("Creating labels from automatically detected events.")

    read_swd_events = pd.read_table(
        filename,
        delimiter=",",
        skiprows=1,
        header=None)

    annotations = mne.Annotations(
        onset=read_swd_events.iloc[:, 0] + tmin,
        duration=read_swd_events.iloc[:, 2],
        description="swd",
        orig_time=None)

    print("Annotations loaded.")
    return annotations


def save_manual_annotation_on_close(raw, tmin, save_path):
    label_df = raw.annotations.to_data_frame(time_format=None)
    label_df = label_df[['description', 'onset', 'duration']]
    label_df.to_csv(save_path, sep=",", index=False)
    print("Annotations saved.")