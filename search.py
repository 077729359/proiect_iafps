def search_schedules(index, schedules, group=None, subject=None, teacher=None, week_type=None, days=None):
    results = []
    
    # daca avem zile de cautat
    if days:
        for day in days:
            if day in index:  # verificam rapid în hash table
                for schedule in index[day]:

                    # verificam restul conditiilor
                    if (group and schedule.grupa != group) or \
                       (subject and subject.lower() not in schedule.subject.lower()) or \
                       (teacher and teacher.lower() not in schedule.teacher.lower()) or \
                       (week_type and schedule.week_type != week_type):
                        continue
                    results.append(schedule)
    else:
        # cautam dupa linear search daca nu avem zile in campul de cautare
        
        for schedule in schedules:
            if (group and schedule.grupa != group) or \
               (subject and subject.lower() not in schedule.subject.lower()) or \
               (teacher and teacher.lower() not in schedule.teacher.lower()) or \
               (week_type and schedule.week_type != week_type):
                continue
            results.append(schedule)
    
    return results