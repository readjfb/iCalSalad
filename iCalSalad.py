#!/usr/bin/env python3.6
from ics import Calendar, Event
from datetime import datetime
import pytz

def get_time(date, time):
    # Date is in the format MM-DD-YYYY
    # Time is in the form "HH:MM"
    form = "%m-%d-%Y %H:%M"
    local_tmz = pytz.timezone("US/Central")

    naive = datetime.strptime(date + " " + time, form)
    local_dt = local_tmz.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt.strftime("%Y-%m-%d %H:%M:%S")

def convert(csv_file="nu_schedule.csv", ics_flle="nu_classes.ics"):
    cal = Calendar()

    with open(csv_file) as file:
        next(file)
        for line in file:
            data = line.strip().split(",")
            data = [x[1:-1] for x in data]
            
            e = Event()
            e.name = data[0]

            e.begin     = get_time(data[1], data[2])
            e.end       = get_time(data[3], data[4])
            e.location  = data[5]
            
            cal.events.add(e)

    with open(ics_flle, "w") as file:
        file.writelines(cal)

def main():
    convert()


if __name__ == "__main__":
    main()