# we are building a CLI task manager with functionality to add, delete, complete task, search tasks and save tasks to json
# concepts we will be using: OOP, File Handling, Context Managers

import uuid
import json
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


app = typer.Typer(help="A simple CLI task manager.")
console = Console()

PRIORITY_COLORS = {"high": "red", "medium": "yellow", "low": "blue"}


class TaskManager:
    def __init__(self):
        self.tasks = []
        self._load()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._save()
        return False

    def _load(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def add_task(self, title: str, priority: str = "medium"):
        self.tasks.append({'id': str(uuid.uuid4())[:8], 'title': title, 'priority': priority, 'completed': False})

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                break

    def _save(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=4)


def _colored_priority(priority: str) -> str:
    color = PRIORITY_COLORS.get(priority, "white")
    return f"[{color}]{priority}[/{color}]"


def _build_task_table(title: str, tasks: list) -> Table:
    table = Table(title=title)
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Priority")
    table.add_column("Completed", style="green")

    for task in tasks:
        table.add_row(
            task['id'],
            task['title'],
            _colored_priority(task['priority']),
            "✓" if task['completed'] else "✗",
        )
    return table


@app.command()
def add(
    title: str = typer.Argument(..., help="Task title"),
    priority: str = typer.Option("medium", "--priority", "-p", help="low | medium | high"),
):
    """Add a new task with an optional priority (low, medium, high)."""
    if priority not in PRIORITY_COLORS:
        console.print("[red]Priority must be low, medium, or high.[/red]")
        raise typer.Exit(code=1)

    with TaskManager() as tm:
        tm.add_task(title, priority)

    console.print(f"[green]Task added:[/green] {title} with priority {_colored_priority(priority)}")


@app.command(name="list")
def list_tasks():
    """List all tasks in a table."""
    tm = TaskManager()
    if not tm.tasks:
        console.print("[yellow]No tasks yet. Add one with: add \"task name\"[/yellow]")
        return

    table = _build_task_table("Tasks", tm.tasks)
    console.print(Panel(table, title="My Tasks", border_style="cyan"))


@app.command()
def delete(task_id: str = typer.Argument(..., help="Task ID to delete")):
    """Delete a task by its ID."""
    confirmed = typer.confirm(f"Delete task {task_id}?")
    if not confirmed:
        console.print("[yellow]Aborted.[/yellow]")
        raise typer.Exit()

    with TaskManager() as tm:
        before = len(tm.tasks)
        tm.delete_task(task_id)
        deleted = before - len(tm.tasks)

    if deleted:
        console.print(f"[red]Task deleted:[/red] {task_id}")
    else:
        console.print(f"[yellow]No task found with ID:[/yellow] {task_id}")


@app.command()
def complete(task_id: str = typer.Argument(..., help="Task ID to mark as completed")):
    """Mark a task as complete by its ID."""
    found = False
    with TaskManager() as tm:
        for task in tm.tasks:
            if task['id'] == task_id:
                tm.complete_task(task_id)
                found = True
                break

    if found:
        console.print(f"[green]Task completed:[/green] {task_id}")
    else:
        console.print(f"[yellow]No task found with ID:[/yellow] {task_id}")


@app.command()
def search(query: str = typer.Argument(..., help="Search query for task title")):
    """Search tasks by title keyword."""
    tm = TaskManager()
    results = [task for task in tm.tasks if query.lower() in task['title'].lower()]
    if not results:
        console.print(f"[yellow]No tasks found matching:[/yellow] {query}")
        return

    table = _build_task_table(f"Search Results for '{query}'", results)
    console.print(Panel(table, title="Search Results", border_style="cyan"))


if __name__ == "__main__":
    app()
