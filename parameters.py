#taini data and metadata
taini_data_path="C:/Users/niamh/OneDrive/Desktop/Analysis/Raw_data/SCN2A_EEG/SCN2A\weeks16_19/SCN2A_718/TAINI_1047_B_SCN2A_718_BL-2025_04_17-0000.dat"

animal_id = taini_data_path.split("_SCN2A_")[1].split("_")[0]

number_of_channels = 16
sample_rate = 250.4
sample_datatype = 'int16'
display_decimation = 1

#start and end sample for 24-hour quantification period
start_sample = 14678449
end_sample = 36313008

#eeg channels to label
eeg_1 = 3
eeg_2 = 16


#previously annotated (manual or automatic)? (True or False)
previously_annotated = True

#first time loading automatically detected annotation? (True or False)
first_from_automatically_detected = False

#annotations/swd_labels file
label_file_path = "C:/Users/niamh/OneDrive/Desktop/Manual_annotations-master/718_annotations.csv"
