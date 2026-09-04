from datetime import datetime
from enum import Enum
from utils import name_validation

class Priority_enum(Enum):
        HIGH = "High"
        MEDIUM = "Medium"
        LOW = "Low"   

class Task:
    ids = iter(range(1000,9999))
    def __init__(self,task_name :str,priority: Priority_enum ,due_time: datetime):
        
        now = datetime.now()
        self.name = name_validation(task_name)
        self.priority = priority
        self.status = False
        self.time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.id = next(self.ids)
        self.due_time = due_time

    @property
    def priority(self):
         return self._priority
    @priority.setter
    def priority(self,value):
         if not isinstance(value,Priority_enum):
              raise TypeError("Invalid entry,for priority you can only choose between HIGH,MEDIUM and LOW. Please try again")
         self._priority = value
    @property
    def due_time(self):
         return self._due_time
    @due_time.setter
    def due_time(self,value):
         if not isinstance(value,datetime):
              raise ValueError("Invalide dateTime format! Please try again")
         self._due_time = value.strftime("%Y-%m-%d %H:%M:%S")

    def mark_as_done(self):
        if self.status is True:
            raise ValueError("Task is already completed!")
        
        self.status = True
        return f"Congratulation! Task {self.name} is finished now."

    def mark_as_active_again(self):
        if self.status is False:
            raise ValueError("Task is already pending!")
        
        self.status = False
        return f"Task {self.name} status is active again."
    

    def __str__(self):
        return f"Task atributes: name = {self.name}, priority = {self.priority.value}, status = {self.status}, added_time = {self.time}"
    def __repr__(self):
        return f"Task atributes: name = {self.name}, priority = {self.priority.value}, status = {self.status}, added_time = {self.time}"

