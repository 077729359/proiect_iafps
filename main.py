import flet as ft
from models import Schedule
from search import search_schedules
from csv_loader import load_schedule_from_csv

schedules = load_schedule_from_csv("data_base.csv")

display_type = "list"

def main(page: ft.Page):
    page.title = "Căutare Orar"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window_width = 720
    page.window_height = 480

    def get_text_size():
        return max(12, min(20, int(page.window_width / 50)))

    subject_input = ft.TextField(label="Materie", expand=True)
    teacher_input = ft.TextField(label="Profesor", expand=True)

    input_row = ft.Row(controls=[subject_input, teacher_input], spacing=10, expand=True)

    group_options = ["TI-231", "TI-232", "TI-233", "TI-234", "TI-235", "TI-236"]
    selected_groups = []
    
    group_input = ft.Row(expand=True)
    for group in group_options:
        cb = ft.Checkbox(label=group, value=False)
        selected_groups.append(cb)
        group_input.controls.append(cb)

    week_type_options = ["Pară", "Impară"]
    selected_week_types = []
    
    week_type_input = ft.Row(expand=True)
    for week_type in week_type_options:
        cb = ft.Checkbox(label=week_type, value=False)
        selected_week_types.append(cb)
        week_type_input.controls.append(cb)

    day_options = ["Luni", "Marți", "Miercuri", "Joi", "Vineri"]
    selected_days = []
    
    day_input = ft.Row(expand=True)
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
            dialog = ft.AlertDialog(
                title=ft.Text("Rezultatele căutării", weight="bold"),
                content=ft.Text("Nu s-au găsit rezultate", color="red", size=get_text_size(), weight="bold")
            )
            page.overlay.append(dialog)
            dialog.open = True
        else:
            if display_type == "list":
                results_container = ft.Column()
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

                scrollable_content = ft.Container(
                    content=ft.ListView(
                        controls=results_container.controls,
                        expand=True
                    ),
                    width=800,
                    height=list_height,
                    padding=3
                )

                dialog = ft.AlertDialog(
                    title=ft.Row([
                        ft.Text("Rezultatele căutării", weight="bold", expand=True),
                    ]),
                    content=scrollable_content
                )
                page.overlay.append(dialog)  
                dialog.open = True
            else:
                dialog_grid = ft.Column(spacing=10, expand=True)
                row = ft.Row(wrap=True, spacing=10, expand=True)

                columns_per_row = 10000  

                for i, schedule in enumerate(search_results):
                    result_dialog = ft.Container(
                        content=ft.Column([
                            ft.Text(f"Grupa: {schedule.grupa}", expand=True),
                            ft.Text(f"Materie: {schedule.subject}", expand=True),
                            ft.Text(f"Profesor: {schedule.teacher}", expand=True),
                            ft.Text(f"Început: {schedule.start_time}", expand=True),
                            ft.Text(f"Final: {schedule.end_time}", expand=True),
                            ft.Text(f"Tip săptămână: {schedule.week_type}", expand=True),
                            ft.Text(f"Clădire: {schedule.building}", expand=True),
                            ft.Text(f"Zi: {schedule.day}", expand=True),
                        ]),
                        border=ft.BorderSide(1, "black"),
                        padding=15,
                        width=200,
                        height=250
                    )
                    row.controls.append(result_dialog)

                    if (i + 1) % columns_per_row == 0:
                        dialog_grid.controls.append(row)
                        row = ft.Row(wrap=True, spacing=10, expand=True)

                if row.controls:
                    dialog_grid.controls.append(row)

                scrollable_container = ft.Container(
                    content=ft.ListView(
                        controls=[dialog_grid],
                        expand=True,
                        height=page.window_height - 100
                    ),
                    width=1200
                )

                dialog = ft.AlertDialog(
                    title=ft.Text("Rezultatele căutării", weight="bold"),
                    content=scrollable_container
                )
                page.overlay.append(dialog)
                dialog.open = True

        page.update()
        reset_inputs()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_icon.icon = ft.icons.NIGHTLIGHT_ROUND  
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_icon.icon = ft.icons.WB_SUNNY  
        page.update()

    theme_icon = ft.IconButton(
        icon=ft.icons.WB_SUNNY,
        on_click=toggle_theme,
        tooltip="Schimbă tema"
    )

    def toggle_display_type(e):
        global display_type
        display_type = "grid" if display_type == "list" else "list"
        update_display_icon()
        page.update()

    def update_display_icon():
        if display_type == "list":
            display_icon.icon = ft.icons.LIST
        else:
            display_icon.icon = ft.icons.GRID_ON

    display_icon = ft.IconButton(
        icon=ft.icons.LIST,
        tooltip="Mod de afișare",
        on_click=toggle_display_type
    )

    search_button = ft.ElevatedButton(text="Caută", on_click=lambda e: search_schedules_func(), expand=True)

    page.add(
        input_row,
        ft.Text("Selectați grupa:", expand=True, size=get_text_size()),
        group_input,
        ft.Text("Selectați tipul săptămânii:", expand=True, size=get_text_size()),
        week_type_input,
        ft.Text("Selectați ziua:", expand=True, size=get_text_size()),
        day_input,
        search_button,
        ft.Row([theme_icon, display_icon], alignment=ft.MainAxisAlignment.END, expand=True)
    )

    page.on_resize = lambda e: update_text_sizes()

    def update_text_sizes():
        subject_input.size = get_text_size()
        teacher_input.size = get_text_size()
        
        for cb in selected_groups:
            cb.size = get_text_size()
            
        for cb in selected_week_types:
            cb.size = get_text_size()
            
        for cb in selected_days:
            cb.size = get_text_size()
            
        page.update()

ft.app(target=main)
