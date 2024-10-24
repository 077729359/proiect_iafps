import flet as ft
from models import Schedule
from search import search_schedules

# Exemplu de date de program
schedules = [

    #orar ti-235 sapt impara
    Schedule(1, "TI-235", "Ed.Fizica", "Tatiana Sport", "11:30", "13:00", "Impară", "Stadion", "Luni"),
    Schedule(2, "TI-235", "Filozofie", "Antoci A.", "13:30", "15:00", "Impară", "3-613", "Luni"),
    Schedule(3, "TI-235", "MN", "Struna V.", "15:15", "16:45", "Impară", "3-516", "Luni"),
    Schedule(4, "TI-235", "CDE", "Cretu V.", "15:15", "16:45", "Impară", "3-3", "Marți"),
    Schedule(5, "TI-235", "ASDN", "Turcan A.", "17:00", "18:30", "Impară", "3-3", "Marți"),
    Schedule(6, "TI-235", "P00", "Gincu S.", "18:45", "20:15", "Impară", "3-3", "Marți"),
    Schedule(7, "TI-235", "CDE", "Litra D.", "9:45", "13:00", "Impară", "3-406", "Miercuri"),
    Schedule(8, "TI-235", "Dreptul", "Ursu V.", "13:30", "15:00", "Impară", "3-3", "Miercuri"),
    Schedule(9, "TI-235", "POO", "Cebotari D.", "15:15", "16:45", "Impară", "3-512", "Miercuri"),
    Schedule(10, "TI-235", "APA", "Scrob S.", "11:30", "13:00", "Impară", "3-114", "Joi"),
    Schedule(11, "TI-235", "IAFPS", "Bagrin V.", "13:30", "15:00", "Impară", "3-519", "Joi"),
    Schedule(12, "TI-235", "POO", "Cebotari D.", "15:15", "16:45", "Impară", "3-512", "Joi"),
    Schedule(13, "TI-235", "APA", "Bagrin V.", "11:30", "13:00", "Impară", "3-3", "Vineri"),
    Schedule(14, "TI-235", "MN", "Patiuc V.", "13:30", "15:00", "Impară", "3-3", "Vineri"),
    Schedule(15, "TI-235", "Filozofia", "Antoci A.", "15:15", "16:45", "Impară", "3-3", "Vineri"),


 #orar ti-235 sapt para

 
    Schedule(16, "TI-235", "Filozofie", "Antoci A.", "13:30", "15:00", "Pară", "3-613", "Luni"),
    Schedule(17, "TI-235", "ASDN", "Spatari A.", "15:15", "16:45", "Pară", "3-606", "Luni"),
    Schedule(18, "TI-235", "CDE", "Cretu V.", "13:30", "16:45", "Pară", "3-3", "Marți"),
    Schedule(19, "TI-235", "ASDN", "Turcan A.", "17:00", "18:30", "Pară", "3-3", "Marți"),
    Schedule(20, "TI-235", "P00", "Gincu S.", "18:45", "20:15", "Pară", "3-3", "Marți"),
    Schedule(21, "TI-235", "Dreptul", "Ursu V.", "13:30", "15:00", "Pară", "3-3", "Miercuri"),
    Schedule(22, "TI-235", "POO", "Cebotari D.", "15:15", "16:45", "Pară", "3-512", "Miercuri"),
    Schedule(23, "TI-235", "ASDN", "Ursu A.", "9:45", "11:15", "Pară", "3-518", "Joi"),
    Schedule(24, "TI-235", "APA", "Scrob S.", "11:30", "13:00", "Pară", "3-114", "Joi"),
    Schedule(25, "TI-235", "IAFPS", "Bagrin V.", "13:30", "15:00", "Pară", "3-519", "Joi"),
    Schedule(26, "TI-235", "POO", "Cebotari D.", "15:15", "16:45", "Pară", "3-512", "Joi"),
    Schedule(27, "TI-235", "APA", "Bagrin V.", "11:30", "13:00", "Pară", "3-3", "Vineri"),
    Schedule(28, "TI-235", "MN", "Patiuc V.", "13:30", "15:00", "Pară", "3-3", "Vineri"),
    Schedule(29, "TI-235", "Filozofia", "Antoci A.", "15:15", "16:45", "Pară", "3-3", "Vineri"),

]

def main(page: ft.Page):
    page.title = "Căutare Orar"

    subject_input = ft.TextField(label="Materie", width=200)
    teacher_input = ft.TextField(label="Profesor", width=200)

    subject_teacher_row = ft.Row(controls=[subject_input, teacher_input], spacing=10)

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
    not_found_message = ft.Text("Nu sunt extrasens", color="red", size=20, weight="bold")

    def search_schedules_func():
        results_container.controls.clear()

        # Verificăm dacă nu s-a selectat nimic
        if (not any(cb.value for cb in selected_groups) and
            not subject_input.value and
            not teacher_input.value and
            not any(cb.value for cb in selected_week_types) and
            not any(cb.value for cb in selected_days)):
            results_container.controls.append(not_found_message)
            page.update()
            return

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
            results_container.controls.append(not_found_message)
        else:
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
        subject_teacher_row,
        ft.Text("Alege grupele:"),
        group_input,
        ft.Text("Alege tipul săptămânii:"),
        week_type_input,
        ft.Text("Alege zilele săptămânii:"),
        day_input,
        search_button,
        ft.Container(height=20),
        results_container,
    )

ft.app(target=main)
