from tasks import Task

class Todo:
    def __init__(self):
        self.tasks = {}

    def add_task(self,task_name,priority,due_time):
        added_task = Task(task_name,priority,due_time)
        self.tasks[added_task.id] = added_task
        return f"Task {added_task.name} adds successfully and it's active now."

    def get_all_tasks(self):
        if not self.tasks:
            return []
        return list(self.tasks.items())
    def get_task(self,id:int):
        if not isinstance(id,int):
            raise ValueError("Tasks Id must be an integer from 1000 to 9999! Please try again.")
        else:
            if id in self.tasks.keys():
                return self.tasks[id]
            else:
                return None

    def remove_task(self,id:int):
        if not isinstance(id,int):
            raise ValueError("Tasks Id must be an integer from 1000 to 9999! Please try again.")
        else:
            if id in self.tasks.keys():
                deleted_task = self.tasks.pop(id)
                return deleted_task
            else:
                return None

        