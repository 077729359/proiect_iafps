from models import Schedule

def search_schedules(schedules, group=None, subject=None, teacher=None, week_type=None, days=None):
    results = []
    
    for schedule in schedules:
        # Verifică dacă grupa este selectată
        if group and schedule.group not in group:
            continue
            
        # Verifică dacă subiectul este specificat
        if subject and subject.lower() not in schedule.subject.lower():
            continue
        
        # Verifică dacă profesorul este specificat
        if teacher and teacher.lower() not in schedule.teacher.lower():
            continue
        
        # Verifică dacă tipul săptămânii este specificat
        if week_type and schedule.week_type not in week_type:
            continue

        # Verifică dacă ziua este specificată
        if days and schedule.day not in days:
            continue
        
        results.append(schedule)
    
    return results
