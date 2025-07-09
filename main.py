import flet as ft

def main(page: ft.Page):
    page.title = "Modern To-Do App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = "auto"
    page.theme_mode = "light"
    page.bgcolor = ft.Colors.BLUE_GREY_50

    # Title
    title = ft.Text(
        "📝 To-Do List", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900
    )

    # Task list container
    tasks = ft.Column(spacing=10, scroll=ft.ScrollMode.ADAPTIVE)

    # Add task field
    task_input = ft.TextField(
        hint_text="Add a new task...",
        expand=True,
        bgcolor=ft.Colors.WHITE,
        border_radius=8,
        filled=True,
        content_padding=10,
    )

    def add_task(e):
        task_text = task_input.value.strip()
        if not task_text:
            return
        new_task = ft.Checkbox(
            label=task_text,
            value=False,
            fill_color=ft.Colors.LIGHT_BLUE_700,
            on_change=lambda e: update_ui()
        )
        tasks.controls.append(
            ft.Container(
                content=ft.Row([
                    new_task,
                    ft.IconButton(icon=ft.Icons.DELETE_OUTLINE, icon_color=ft.Colors.RED_400, on_click=lambda e, t=new_task: remove_task(t))
                ]),
                padding=10,
                border_radius=12,
                bgcolor=ft.Colors.WHITE,
                shadow=ft.BoxShadow(
                    blur_radius=6,
                    color=ft.Colors.with_opacity(0.2, ft.Colors.BLACK)
                )
            )
        )
        task_input.value = ""
        page.update()

    def remove_task(task):
        tasks.controls = [
            c for c in tasks.controls if not isinstance(c.content, ft.Row) or c.content.controls[0] != task
        ]
        page.update()

    def update_ui():
        page.update()

    # Add button
    add_btn = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.WHITE,
        bgcolor=ft.Colors.LIGHT_BLUE_700,
        on_click=add_task,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    # Layout
    page.add(
        ft.Container(
            content=ft.Column([
                title,
                ft.Row([task_input, add_btn], spacing=10),
                tasks,
            ]),
            margin=20,
            padding=20,
            border_radius=20,
            bgcolor=ft.Colors.BLUE_GREY_100,
            shadow=ft.BoxShadow(
                blur_radius=10,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
            )
        )
    )

ft.app(target=main)
