# search.py

from models import Schedule

def search_schedules(schedules, group=None, subject=None, teacher=None):
    results = []
    for schedule in schedules:
        if (
            (group is None or schedule.group == group) and
            (subject is None or schedule.subject == subject) and
            (teacher is None or schedule.teacher == teacher)
        ):
            results.append(schedule)
    return results


