import argparse
import datetime
from TaskManager import TaskManager

parser = argparse.ArgumentParser(prog="Task Manager", description="A CLI based task manager that manages tasks",
                                 allow_abbrev=False)
parser.add_argument("-t", "--task", required=False, help="The task name that you want to add")
parser.add_argument("-p", "--priority", required=False, help="Priority from low(1) to high(3). default is 1", type=int, default=1)
parser.add_argument("-d", "--deadline", required=False, help="format: YYYY-MM-DD HH:MM. default is now+24h",
                    default="{0:%Y}:{0:%m}:{0:%d} {0:%H}:{0:%M}".format(datetime.datetime.now() + datetime.timedelta(hours=24)))
parser.add_argument("-f", "--file", required=False, help="json file to store the tasks. defaults to 'tasks.json' in root directory",
                    default="tasks.json")
parser.add_argument("-l", "--list", required=False, help="list all tasks", action='store_true')
parser.add_argument("--sort", required=False, help="sort based on priority, deadline or both. use --asc to sort in ascending order",
                    choices=["priority", "deadline"], nargs='+')
parser.add_argument("--asc", required=False, help="sort in ascending order(less priority & last deadline)", action='store_false')
parser.add_argument("-c", "--clean", required=False, help="cleans all tasks", action='store_true')

args = parser.parse_args()

task_manager = TaskManager(file=args.file)
if args.clean:
    task_manager.clean()
    print("cleaned")
if args.task:
    task_manager.add_task(task=args.task, priority=args.priority, deadline=args.deadline)
    print(f"Added new task")
if args.list:
    if len(args.sort)==2:
        task_manager.sort(priority=True, deadline=True, reverse=args.asc)
    elif "priority" in args.sort:
        task_manager.sort(priority=True, deadline=False, reverse=args.asc)
    else:
        task_manager.sort(priority=False, deadline=True, reverse=args.asc)
    task_manager.list_tasks()
