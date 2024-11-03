import flet as ft
from models import Schedule
from search import search_schedules
from csv_loader import load_schedule_from_csv

# Încărcați programul din fișierul CSV
schedules = load_schedule_from_csv("db.csv")

def main(page: ft.Page):
    page.title = "Căutare Orar"

    subject_input = ft.TextField(label="Materie", width=200)
    teacher_input = ft.TextField(label="Profesor", width=200)

    group_options = ["TI-231", "TI-232", "TI-233", "TI-234", "TI-235", "TI-236"]
    selected_groups = []
    
    group_input = ft.Row()  
    for group in group_options:
        cb = ft.Checkbox(label=group, value=False)
        selected_groups.append(cb)
        group_input.controls.append(cb)

    week_type_options = ["Pară", "Impară"]
    selected_week_types = []
    
    week_type_input = ft.Row()  
    for week_type in week_type_options:
        cb = ft.Checkbox(label=week_type, value=False)
        selected_week_types.append(cb)
        week_type_input.controls.append(cb)

    day_options = ["Luni", "Marți", "Miercuri", "Joi", "Vineri"]
    selected_days = []
    
    day_input = ft.Row() 
    for day in day_options:
        cb = ft.Checkbox(label=day, value=False)
        selected_days.append(cb)
        day_input.controls.append(cb)

    search_button = ft.ElevatedButton(text="Caută", on_click=lambda e: search_schedules_func())
    
    results_container = ft.Column()

    def search_schedules_func():
        results_container.controls.clear()

        selected_groups_values = [cb.label for cb in selected_groups if cb.value]
        selected_week_types_values = [cb.label for cb in selected_week_types if cb.value]
        selected_days_values = [cb.label for cb in selected_days if cb.value]

        search_results = search_schedules(
            schedules,
            group=selected_groups_values or None,
            subject=subject_input.value or None,
            teacher=teacher_input.value or None,
            week_type=selected_week_types_values or None,
            days=selected_days_values or None,
        )

        if not search_results:
            results_container.controls.append(ft.Text("Nu s-au găsit rezultate", color="red", size=20, weight="bold"))
        else:
            for schedule in search_results:
                result_row = ft.Row([
                    ft.Text(schedule.grupa, width=100),
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
        ft.Text("Selectați grupa:"),
        group_input,
        ft.Text("Selectați tipul săptămânii:"),
        week_type_input,
        ft.Text("Selectați ziua:"),
        day_input,
        search_button,
        results_container,
    )

ft.app(target=main)
