# iCalSalad
Converts [salad.nu](https://www.salad.nu) CSV files into importable iCal files

Uses the ics library to convert CSVs into iCal files, and displays the process with a handy GUI. The User selects the file with a tKinter dialog box, and the iCal file is created in the directory where the csv is located.

## Setup
1. Download the repository first. 
2. Install dependencies by running `pip install -r requirements.txt` 
3. Run [iCalSalad_gui.py](iCalSalad_gui.py) in the Python interpreter of your choice
4. Select the CSV to be transformed, and press convert. iCal file will be created in the same file as the CSV.

## Timezone info
All times listed on salad.nu are in CST, so the iCalSalad converts times to UTC, as iCal natively uses the UTC standard. It should then import painlessly into the Calendar application, and display the correct time regardless of the user's local timezone.