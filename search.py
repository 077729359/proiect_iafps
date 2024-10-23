from models import Schedule

def search_schedules(schedules, group=None, subject=None, teacher=None, week_type=None, days=None):
    results = []
    
    for schedule in schedules:
        
        if group and schedule.group not in group:
            continue
            
        
        if subject and subject.lower() not in schedule.subject.lower():
            continue
        
       
        if teacher and teacher.lower() not in schedule.teacher.lower():
            continue
        
       
        if week_type and schedule.week_type not in week_type:
            continue

        
        if days and schedule.day not in days:
            continue
        
        results.append(schedule)
    
    return results
