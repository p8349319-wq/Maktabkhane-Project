from tasks import Task,Priority_enum
from csv import DictWriter,DictReader
from datetime import strptime,datetime

class Todo:
    def __init__(self):
        self.tasks = {}
        self.load_csv()

    def add_task(self,task_name,priority,due_time):
        added_task = Task(task_name,priority,due_time)
        self.tasks[added_task.id] = added_task
        self.save_csv
        return f"Task {added_task.name} adds successfully and it's active now."

    def get_all_tasks(self):
        if not self.tasks:
            return []
        return list(self.tasks.values())
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
            if id in self.tasks:
                deleted_task = self.tasks.pop(id)
                self.save_csv()
                return deleted_task
            else:
                return None

    def  get_tasks_sorted_by_priority(self):
        return list(sorted(self.tasks.values(),key=lambda task: task.priority.value,reverse=True))

    def save_csv(self):
        with open("Tasks.csv","w",newline="") as output_file:
            fieldnames = [
                "ID",
                "Name",
                "Added_time",
                "Priority",
                "Due_time",
                "Status"
            ]
            csv_writer = DictWriter(output_file,fieldnames=fieldnames)
            csv_writer.writeheader()
            for task in self.get_all_tasks(): 
                csv_writer.writerow({
                    "ID" : task.id,
                    "Name" : task.name,
                    "Added_time" : task.time,
                    "Priority" : task.priority.value,
                    "Due_time" : task.due_time,
                    "Status" : task.status
                }) 

    def load_csv(self):
        try:
            with open("Tasks.csv", "r") as input_file:
                csv_reader = DictReader(input_file)
                if not csv_reader.fieldnames:
                    return "CSV file is empty or has no header row"
            
                for row_num, row in enumerate(csv_reader, start=2):
                    try:
                        task_id = int(row["ID"])
                        task_name = row['Name']
                        task_priority_value = int(row['Priority'])
                        task_status = row['Status'] == 'True'
                        task_created_time = row['Added_time']
                        task_due_time = row['Due_time']
                    
                        priority = Priority_enum(task_priority_value)
                        due_time = datetime.strptime(task_due_time, "%Y-%m-%d %H:%M:%S")
                    
                        task = Task(task_name, priority, due_time)
                        task.id = task_id
                        task.status = task_status
                        task.time = task_created_time
                    
                        self.tasks[task.id] = task
                    
                    except KeyError as e:
                        return f"Error at row {row_num}: Missing column {e}. Check CSV headers."
                    except ValueError as e:
                        return f"Error at row {row_num}: Invalid data format. {e}"
                    except Exception as e:
                        return f"Error at row {row_num}: {e}"
            
                if self.get_all_tasks():
                    highest_id = max(task.id for task in self.get_all_tasks())
                    Task.id_generator(highest_id + 1)
                        
        except FileNotFoundError:
            return "Tasks.csv file not found. Starting with empty task list."
        except Exception as e:
            return f"Error loading CSV: {e}"
                    

            
    

        