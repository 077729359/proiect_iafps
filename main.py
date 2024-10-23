import flet as ft
from models import Schedule
from search import search_schedules

# Exemplu de date de program
schedules = [
    Schedule(1, "TI-231", "Matematica", "Ion Popescu", "08:00", "09:30", "Pară", "Clădirea A", "Luni"),
    Schedule(2, "TI-232", "Programare", "Maria Ionescu", "10:00", "11:30", "Impară", "Clădirea B", "Marți"),
    Schedule(3, "TI-233", "Fizica", "Andrei Georgescu", "12:00", "13:30", "Pară", "Clădirea C", "Miercuri"),
    Schedule(4, "TI-234", "Chimie", "Laura Dobre", "14:00", "15:30", "Impară", "Clădirea D", "Joi"),
    Schedule(5, "TI-235", "Biologie", "Emilia Vasilescu", "16:00", "17:30", "Pară", "Clădirea E", "Vineri"),
    Schedule(6, "TI-236", "Statistica", "Radu Iliescu", "08:00", "09:30", "Impară", "Clădirea F", "Luni"),
    Schedule(7, "TI-231", "Engleză", "Elena Grigorescu", "09:30", "11:00", "Pară", "Clădirea A", "Marți"),
    Schedule(8, "TI-232", "Istorie", "Mihai Florescu", "11:00", "12:30", "Impară", "Clădirea B", "Miercuri"),
    Schedule(9, "TI-233", "Geografie", "Sorina Albu", "13:30", "15:00", "Pară", "Clădirea C", "Joi"),
    Schedule(10, "TI-234", "Artă", "Olivia Negru", "15:00", "16:30", "Impară", "Clădirea D", "Vineri"),
]

def main(page: ft.Page):
    page.title = "Căutare Orar"

    subject_input = ft.TextField(label="Materie", width=200)
    teacher_input = ft.TextField(label="Profesor", width=200)

    # Checkbox pentru grupe (aranjate orizontal în `Row`)
    group_options = ["TI-231", "TI-232", "TI-233", "TI-234", "TI-235", "TI-236"]
    selected_groups = []
    
    group_input = ft.Row()  # Grupurile vor fi afișate orizontal
    for group in group_options:
        cb = ft.Checkbox(label=group, value=False)
        selected_groups.append(cb)
        group_input.controls.append(cb)

    # Checkbox pentru tipul săptămânii (aranjate orizontal în `Row`)
    week_type_options = ["Pară", "Impară"]
    selected_week_types = []
    
    week_type_input = ft.Row()  # Tipurile săptămânii vor fi afișate orizontal
    for week_type in week_type_options:
        cb = ft.Checkbox(label=week_type, value=False)
        selected_week_types.append(cb)
        week_type_input.controls.append(cb)

    # Checkbox pentru zilele săptămânii (aranjate orizontal în `Row`)
    day_options = ["Luni", "Marți", "Miercuri", "Joi", "Vineri"]
    selected_days = []
    
    day_input = ft.Row()  # Zilele săptămânii vor fi afișate orizontal
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

    # Adăugarea secțiunilor de input
    page.add(
        ft.Text("Alege grupele:"),
        group_input,  # Grupuri afișate orizontal
        ft.Text("Alege tipul săptămânii:"),
        week_type_input,  # Tipuri săptămână afișate orizontal
        ft.Text("Alege zilele săptămânii:"),
        day_input,  # Zile afișate orizontal
        search_button,
        ft.Container(height=20),  # Spațiu între buton și rezultatele afișate
        results_container,
    )

ft.app(target=main)
