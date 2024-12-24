import csv
from schedule import Schedule
from collections import defaultdict


def load_schedule_from_csv(filename: str):
    schedules = []
    index = defaultdict(list)  

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            schedule = Schedule(
                grupa=row[0],
                subject=row[1],
                teacher=row[2],
                start_time=row[3],
                end_time=row[4],
                week_type=row[5],
                building=row[6],
                day=row[7]
            )
            schedules.append(schedule)
            index[schedule.day].append(schedule)  

    return schedules, index  