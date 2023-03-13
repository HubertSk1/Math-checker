from random import randint
class Task():
    def __init__(self, task):
        self.task_type = task
        self.first_number = None
        self.secend_number = None
        self.result = None
        self.equation = None
        self.set_task()

#["Mnożenie 0-10", "Dzielenie 0-10", "Dodawanie 0-1000", "Odejmowanie 0-1000","Mnożenie 0-100","Dzielenie 0-100"]
    def set_task(self):
        #Mnożenie 0-10
        if self.task_type == "Mnożenie 0-10":
            self.first_number = randint(0,10)
            self.secend_number = randint(0,10)
            self.result = self.first_number * self.secend_number 
            self.equation = f'{self.first_number} \u00B7 {self.secend_number} = ?'
        #Dzielenie 0-10
        if self.task_type == "Dzielenie 0-10":
            a = randint(0,10)
            b = randint(1,10)
            c = a* b 
            self.first_number = c
            self.secend_number = b
            self.result = a
            self.equation= f' {self.first_number}:{self.secend_number} = ?'
        #Dodawanie 0-1000
        if self.task_type == "Dodawanie 0-1000":
            self.first_number = randint(100,1000)
            self.secend_number = randint(0,1000)
            self.result = self.first_number + self.secend_number 
            self.equation = f'{self.first_number} + {self.secend_number} = ?'
        #Odejmowanie 0-1000
        if self.task_type == "Odejmowanie 0-1000":
            a = randint(0,1000)
            b = randint(0,1000)
            self.first_number = max(a,b)
            self.secend_number = min(a,b)
            self.result = self.first_number - self.secend_number
            self.equation = f"{self.first_number} - {self.secend_number} = ?"
        #Mnożenie 0-100
        if self.task_type == "Mnożenie 0-100":
            self.first_number = randint(0,10)
            self.secend_number = randint(0,100)
            self.result = self.first_number * self.secend_number 
            self.equation = f'{self.first_number} \u00B7 {self.secend_number} = ?'
        #Dzielenie 0-100
        if self.task_type == "Dzielenie 0-100":
            a = randint(0,100)
            b = randint(1,10)
            c = a* b 
            self.first_number = c
            self.secend_number = b
            self.result = a
            self.equation= f' {self.first_number}:{self.secend_number} = ?'