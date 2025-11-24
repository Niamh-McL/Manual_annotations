## Annotating interactive plot of EEG data (MNE) 
This script loads a recording file and any existing labels using MNE, plotting a 24-hour window of data from 2 selected channels to be annotated/labelled. The output of the script should be a .csv file of annotations (description, onset and duration) of swd events (manually annotated or automatically detected) and immature discharges (manually annotated).

## Instructions
Navigate to the parameters(.py) script and enter the recording file you want to annotated in the taini_data_path parameter.
```
taini_data_path="C:/Users/niamh/OneDrive/Desktop/Analysis/Raw_data/SCN2A_EEG/SCN2A/weeks16_19/SCN2A_718/TAINI_1047_B_SCN2A_718_BL-2025_04_17-0000.dat"
```
Edit the start and end sample to adjust the 24-hour window for labelling (find values in SCN2A meta-data file).
```
start_sample = 14678449
end_sample = 36313008
```
Enter the EEG channels you want to plot in eeg_channels parameter.
```
eeg_1 = 3
eeg_2 = 16
```
Adjust boolean (True or False) variables.
```
previously_annotated = False
first_from_automatically_detected = True
```
If the recording file has been previously annotated/labelled then edit the label_file_path to import these existing labels.
```
label_file_path = "C:/Users/niamh/OneDrive/Desktop/Manual_annotations-master/718_annotations.csv"
```
