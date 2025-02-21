
# CLI BASED TASK MANAGER

*just to try argparser and to refresh some python concepts*

usage: Task Manager [-h] [-t TASK] [-p PRIORITY] [-d DEADLINE] [-f FILE] [-l] [--sort {priority,deadline} [{priority,deadline} ...]] [--asc] [-c]

A CLI based task manager that manage tasks

**OPTIONS:**

  **-h, --help**: show this help message and exit

  **-t TASK, --task TASK**: The task name that you want to add

  **-p PRIORITY, --priority PRIORITY**: Priority from low(1) to high(3). default is 1

  **-d DEADLINE, --deadline DEADLINE**: format: YYYY-MM-DD HH:MM. default is now+24h

  **-f FILE, --file FILE**: json file to store the tasks. defaults to 'tasks.json' in root directory

**-l, --list**: list all tasks

**--sort {priority,deadline} [{priority,deadline} ...]**: sort based on priority, deadline or both use --asc to sort in ascending order

**--asc**: sort in ascending order(less priority & last deadline)

**-c, --clean**: cleans all tasks

```
>python main.py --task "taskno 200" --priority 2
Added new task
```
```
>python main.py --list
 PRIORITY      DEADLINE         TASK
    1      2025:02:21 22:19     taskno 1
    2      2025:02:22 12:00     taskno 2
    3      2025:02:22 01:00     taskno 3
    3      2025:02:21 01:00     taskno 4
```
```
>python main.py --list --sort priority deadline
 PRIORITY      DEADLINE         TASK
    3      2025:02:21 01:00     taskno 4
    3      2025:02:22 01:00     taskno 3
    2      2025:02:22 12:00     taskno 2
    1      2025:02:21 22:19     taskno 1
```
```
>python main.py --list --sort deadline
 PRIORITY      DEADLINE         TASK
    3      2025:02:21 01:00     taskno 4
    1      2025:02:21 22:19     taskno 1
    3      2025:02:22 01:00     taskno 3
    2      2025:02:22 12:00     taskno 2
```
```
>python main.py --list --sort priority --asc
 PRIORITY      DEADLINE         TASK
    1      2025:02:21 22:19     taskno 1
    2      2025:02:22 12:00     taskno 2
    3      2025:02:22 01:00     taskno 3
    3      2025:02:21 01:00     taskno 4
```