import json
from pathlib import Path

class TaskManager:
    def __init__(self, task: str, file: str, priority: int, deadline: str):
        self.task = task
        self.priority = priority
        self.deadline = deadline
        self.file = file
        self._read_tasks(file)

    def __str__(self) -> None:
        print(f"priority: {self.priority} {self.deadline} {self.task}")

    def _read_tasks(self, file: str) -> list[dict]:
        try:
            file_path = Path(file)
            file_content = None
            if file_path.is_file():
                with file_path.open('r') as tasks_file:
                    file_content = tasks_file.read()
            else:
                file_path.touch()
            if not file_content:
                file_content = []
                self.tasks_data = []
                file_path.write_text(str(self.tasks_data))
                return file_content
            else:
                self.tasks_data = json.loads(file_content)
        except Exception as e:
            print(f"Error reading file {file}")
            print(e)

    def _write_tasks(self, file: str, tasks_data: list[dict]) -> list[dict]:
        try:
            file_path = Path(file)
            if file_path.is_file():
                with file_path.open('w') as tasks_file:
                    json.dump(tasks_data, fp=tasks_file, indent=4)
            else:
                print(f"unable to write to {file_path}")
        except Exception as e:
            print(f"Error writing file {file}")
            print(e)

    def add_task(self) -> None:
        curr_task = dict()
        curr_task["task"] = self.task
        curr_task["priority"] = self.priority
        curr_task["deadline"] = self.deadline
        if not self.tasks_data:
            self.tasks_data = []
        self.tasks_data.append(curr_task)
        self._write_tasks(self.file, self.tasks_data)

    def clean(self) -> None:
        self.tasks_data = []