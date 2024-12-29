def search_schedules(schedules, index, group=None, subject=None, teacher=None, week_type=None, building=None, day=None):
    results = schedules  

    if group:
       
        results = [schedule for schedule in results if schedule.group in group]
    
    if subject:

        results = [schedule for schedule in results if any(s for s in subject if s.lower() in schedule.subject.lower())]
    
    if teacher:
        
        results = [schedule for schedule in results if any(t for t in teacher if t.lower() in schedule.teacher.lower())]
    
    if week_type:
        
        results = [schedule for schedule in results if schedule.week_type in week_type]
    
    if building:
        
        results = [schedule for schedule in results if schedule.building in building]
    
    if day:
       
        results = [schedule for schedule in results if any(d for d in day if d.lower() in schedule.day.lower())]
    
    return results
