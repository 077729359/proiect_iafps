import csv
from models import Schedule

def load_schedule_from_csv(filename: str):
    schedules = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Setăm delimitatorul la ';'
        for row in reader:
            schedule = Schedule(
                grupa=row[0],         # Grupa
                subject=row[1],      # Materie
                teacher=row[2],      # Profesor
                start_time=row[3],   # Ora începere
                end_time=row[4],     # Ora sfârșit
                week_type=row[5],    # Tip săptămână
                building=row[6],     # Clădire
                day=row[7]           # Zi
            )
            schedules.append(schedule)
    return schedules
