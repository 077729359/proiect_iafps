
import flet as ft
from models import Schedule
from search import search_schedules


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
    Schedule(11, "TI-235", "Music", "Isabella Black", "08:00", "09:30", "Even", "Building E", "Monday"),
    Schedule(12, "TI-236", "Psychology", "Liam Red", "10:00", "11:30", "Odd", "Building F", "Tuesday"),
    Schedule(13, "TI-231", "Economics", "Mia Pink", "12:00", "13:30", "Even", "Building A", "Wednesday"),
    Schedule(14, "TI-232", "Philosophy", "Ethan Yellow", "14:00", "15:30", "Odd", "Building B", "Thursday"),
    Schedule(15, "TI-233", "Computer Science", "Ava Orange", "16:00", "17:30", "Even", "Building C", "Friday"),
    Schedule(16, "TI-234", "Data Science", "Noah Violet", "08:00", "09:30", "Odd", "Building D", "Monday"),
    Schedule(17, "TI-235", "Machine Learning", "Sophia Cyan", "10:00", "11:30", "Even", "Building E", "Tuesday"),
    Schedule(18, "TI-236", "Artificial Intelligence", "Lucas Magenta", "12:00", "13:30", "Odd", "Building F", "Wednesday"),
    Schedule(19, "TI-231", "Web Development", "Charlotte Olive", "14:00", "15:30", "Even", "Building A", "Thursday"),
    Schedule(20, "TI-232", "Mobile Development", "Mason Lime", "16:00", "17:30", "Odd", "Building B", "Friday"),
]

def main(page: ft.Page):
    page.title = "Schedule Search"

   
    group_input = ft.TextField(label="Group", width=200)
    subject_input = ft.TextField(label="Subject", width=200)
    teacher_input = ft.TextField(label="Teacher", width=200)

    search_button = ft.ElevatedButton(text="Search", on_click=lambda e: search_schedules_func())
    
  
    results_container = ft.Column()

    def search_schedules_func():
        results_container.controls.clear()
        search_results = search_schedules(
            schedules,
            group_input.value or None,
            subject_input.value or None,
            teacher_input.value or None,
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
        group_input,
        subject_input,
        teacher_input,
        search_button,
        results_container,
    )

ft.app(target=main)
