## Annotating interactive plot of EEG data (MNE) 
This script loads a recording file and any existing labels using MNE, plotting a 24-hour window of data from 2 selected channels to be annotated/labelled. The output of the script should be a .csv file of annotations (description, onset and duration) of swd events (manually annotated or automatically detected) and immature discharges (manually annotated).

## Instructions
Navigate to the parameters(.py) script and enter the recording file you want to annotated in the taini_data_path parameter
```
taini_data_path="C:/Users/niamh/OneDrive/Desktop/Analysis/Raw_data/SCN2A_EEG/SCN2A/weeks16_19/SCN2A_718/TAINI_1047_B_SCN2A_718_BL-2025_04_17-0000.dat"
```
