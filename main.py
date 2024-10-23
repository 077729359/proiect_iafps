import flet as ft
from models import Schedule
from search import search_schedules

# Exemplu de date de program
schedules = [
    Schedule(1, "TI-231", "Mathematics", "John Doe", "08:00", "09:30", "Even", "Building A", "Monday"),
    Schedule(2, "TI-232", "Programming", "Mary Smith", "10:00", "11:30", "Odd", "Building B", "Tuesday"),
    Schedule(3, "TI-233", "Physics", "Andrew Johnson", "12:00", "13:30", "Even", "Building C", "Wednesday"),
    Schedule(4, "TI-234", "Chemistry", "Laura Adams", "14:00", "15:30", "Odd", "Building D", "Thursday"),
    Schedule(5, "TI-235", "Biology", "Emma Brown", "16:00", "17:30", "Even", "Building E", "Friday"),
    Schedule(6, "TI-236", "Statistics", "James Smith", "08:00", "09:30", "Odd", "Building F", "Monday"),
    Schedule(7, "TI-231", "English", "Emily White", "09:30", "11:00", "Even", "Building A", "Tuesday"),
    Schedule(8, "TI-232", "History", "Michael Green", "11:00", "12:30", "Odd", "Building B", "Wednesday"),
    Schedule(9, "TI-233", "Geography", "Sarah Blue", "13:30", "15:00", "Even", "Building C", "Thursday"),
    Schedule(10, "TI-234", "Art", "Oliver Grey", "15:00", "16:30", "Odd", "Building D", "Friday"),
]

def main(page: ft.Page):
    page.title = "Schedule Search"

    group_input = ft.Column()
    subject_input = ft.TextField(label="Subject", width=200)
    teacher_input = ft.TextField(label="Teacher", width=200)

    # Checkbox pentru grupe
    group_options = ["TI-231", "TI-232", "TI-233", "TI-234", "TI-235", "TI-236"]
    selected_groups = []

    for group in group_options:
        cb = ft.Checkbox(label=group, value=False)
        selected_groups.append(cb)
        group_input.controls.append(cb)

    # Checkbox pentru tipul săptămânii
    week_type_input = ft.Column()
    week_type_options = ["Even", "Odd"]
    selected_week_types = []

    for week_type in week_type_options:
        cb = ft.Checkbox(label=week_type, value=False)
        selected_week_types.append(cb)
        week_type_input.controls.append(cb)

    # Checkbox pentru zilele săptămânii
    day_input = ft.Column()
    day_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    selected_days = []

    for day in day_options:
        cb = ft.Checkbox(label=day, value=False)
        selected_days.append(cb)
        day_input.controls.append(cb)

    search_button = ft.ElevatedButton(text="Caută", on_click=lambda e: search_schedules_func())
    
    results_container = ft.Column()

    def search_schedules_func():
        results_container.controls.clear()
        
        # Colectarea valorilor selectate pentru grupe
        selected_groups_values = [cb.label for cb in selected_groups if cb.value]
        
        # Colectarea valorilor selectate pentru tipul săptămânii
        selected_week_types_values = [cb.label for cb in selected_week_types if cb.value]
        
        # Colectarea valorilor selectate pentru zile
        selected_days_values = [cb.label for cb in selected_days if cb.value]

        search_results = search_schedules(
            schedules,
            group=selected_groups_values or None,
            subject=subject_input.value or None,
            teacher=teacher_input.value or None,
            week_type=selected_week_types_values or None,
            days=selected_days_values or None,
        )

        for schedule in search_results:
            result_row = ft.Row([
                ft.Text(str(schedule.id), width=50),
                ft.Text(schedule.group, width=100),
                ft.Text(schedule.subject, width=150),
                ft.Text(schedule.teacher, width=100),
                ft.Text(schedule.start_time, width=80),
                ft.Text(schedule.end_time, width=80),
                ft.Text(schedule.week_type, width=80),
                ft.Text(schedule.building, width=100),
                ft.Text(schedule.day, width=100),
            ])
            results_container.controls.append(result_row)

        page.update()

    page.add(
        ft.Text("Alege grupele:"),
        group_input,
        ft.Text("Alege tipul săptămânii:"),
        week_type_input,
        ft.Text("Alege zilele săptămânii:"),
        day_input,
        search_button,
        results_container,
    )

ft.app(target=main)
