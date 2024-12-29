class Schedule:
    def __init__(self, group: str, subject: str, teacher: str, start_time: str, end_time: str, week_type: str, building: str, day: str):
        self.group = group
        self.subject = subject
        self.teacher = teacher
        self.start_time = start_time
        self.end_time = end_time
        self.week_type = week_type
        self.building = building
        self.day = day

    def __str__(self):
        return f"{self.group}; {self.subject}; {self.teacher}; {self.start_time}; {self.end_time}; {self.week_type}; {self.building}; {self.day}"