def search_schedules(schedules, group=None, subject=None, teacher=None, week_type=None, days=None):
    results = []
    for schedule in schedules:
        if (group and schedule.grupa not in group) or \
           (subject and schedule.subject != subject) or \
           (teacher and schedule.teacher != teacher) or \
           (week_type and schedule.week_type not in week_type) or \
           (days and schedule.day not in days):
            continue
        results.append(schedule)
    return results
