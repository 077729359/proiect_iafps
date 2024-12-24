from csv_loader import load_schedule_from_csv
from search import search_schedules

schedules, index = load_schedule_from_csv('schedule.csv')

group = None
subject = None
teacher = None
week_type = None
days = ["Joi"]

results = search_schedules(index, schedules, group=group, subject=subject, teacher=teacher, week_type=week_type, days=days)

for a in results:
    print(a)

    