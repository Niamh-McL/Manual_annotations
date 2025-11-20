#taini data and metadata
taini_data_path="C:\\Users\\niamh\\OneDrive\\Desktop\\Analysis\\Raw_data\\SCN2A_EEG\\SCN2A\\month_6\\SCN2A_669\\TAINI_1047_B_SCN2A_669_BL-2024_10_04-0000.dat"

animal_id = taini_data_path.split("_SCN2A_")[1].split("_")[0]

number_of_channels = 16
sample_rate = 250.4
sample_datatype = 'int16'
display_decimation = 1

#start and end sample for 24-hour quantification period
start_sample = 12214513
end_sample = 33849072

#eeg channels to label
eeg_1 = 3
eeg_2 = 16


#previously annotated? (True or False)
previously_annotated = True

#annotations/labels file
label_file_path = "C:\\Users\\niamh\\OneDrive\\Desktop\\Manual_annotations-master\\669_annotations.csv"
