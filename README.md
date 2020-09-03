# iCalSalad
Converts salad.nu CSV files into importable iCal files

Uses the ics library to convert csvs into iCal files, and displays the process with a handy GUI. The User selects the file with a tKinter dialog box, and the iCal file is created in the directory where the csv is located.

I think that salad.nu is on CST, so the program converts the time to UTC, as iCal natively uses the UTC standard. It should then import painlessly into the Calendar application.