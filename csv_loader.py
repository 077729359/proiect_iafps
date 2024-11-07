import csv
from models import Schedule

def load_schedule_from_csv(filename: str):
    schedules = []
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
    return schedules