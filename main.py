import flet as ft
from models import Schedule
from search import search_schedules
from csv_loader import load_schedule_from_csv

schedules = load_schedule_from_csv("db.csv")

def main(page: ft.Page):
    page.title = "Căutare Orar"

    subject_input = ft.TextField(label="Materie", width=200)
    teacher_input = ft.TextField(label="Profesor", width=200)

    input_row = ft.Row(controls=[subject_input, teacher_input], spacing=10)

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

    def reset_inputs():
        subject_input.value = ""
        teacher_input.value = ""
        for cb in selected_groups:
            cb.value = False
        for cb in selected_week_types:
            cb.value = False
        for cb in selected_days:
            cb.value = False
        page.update()

    def search_schedules_func():
        
        page.overlay.clear()  

        results_container = ft.Column()

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
            results_container.controls.append(
                ft.Text("Nu s-au găsit rezultate", color="red", size=20, weight="bold")
            )
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

        
        results_count = len(search_results)
        list_height = 200 if results_count < 10 else 500  
        

        scrollable_content = ft.ListView(
            controls=results_container.controls,
            expand=True,  
        )

       
        scrollable_container = ft.Container(
            content=scrollable_content,
            height=list_height,  
            width=1200,  
            padding=3
        )

        dialog = ft.AlertDialog(
            title=ft.Row([
                ft.Text("Rezultatele căutării", weight="bold", expand=True),
              
            ]),
            content=scrollable_container,  
        )
        page.overlay.append(dialog)  
        dialog.open = True
        page.update()

        reset_inputs()  

    search_button = ft.ElevatedButton(text="Caută", on_click=lambda e: search_schedules_func())

    page.add(
        input_row,
        ft.Text("Selectați grupa:"),
        group_input,
        ft.Text("Selectați tipul săptămânii:"),
        week_type_input,
        ft.Text("Selectați ziua:"),
        day_input,
        search_button,
    )

ft.app(target=main)





