# models.py

class Schedule:
    def __init__(self, id, group, subject, teacher, start_time, end_time, week_type, building, day):
        self.id = id
        self.group = group
        self.subject = subject
        self.teacher = teacher
        self.start_time = start_time
        self.end_time = end_time
        self.week_type = week_type
        self.building = building
        self.day = day


