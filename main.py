##helllooosdgodsjgudhguds 

##welcome to employee scheduler

##https://docs.google.com/document/d/1YpV-ogQQxIFtVheAZmlEN7b4XcfP5fMGdnFcMEgYbpI/edit?tab=t.0
## ^^ the document with the stuff
import pandas as pd

"""
TO DO LIST:

> A job has employees (employee objects) that have employee name (string), hourly wage, min hours, max hours, overtime eligibility (boolean), is_available (boolean, for the staffing algorithm)
    >can add/override each thing, dont need to instantiate with this?
    
> create "workweek" object (Days, morning/afternoon/night (what shifts), people needed each day) ASSUMES that each day has same hours/needed employees
    >template? empty? just basically a "hey i need this"
    >shifts have times that can be returned i guess idk where this goes

> Algorithm//  add employees to a "workweek" object, return a filled out "schedule" object (is a workweek?) based on employee stats & needed work for the job.
    >this is done by the scheduler algorithm.
    >assumes one person by shift
    
    > return Day 1: Abby/Morning, Dave/Morning, Carol/Afternoon, Sarah/Night || Day 2: Carol/Morning, 
    


Data -> i/o csv => the thing that reads. (Exercise 2 - Finder as a base?)

Initial docstrings and unit tests

Employee Class

Employee Preferences (in class? out? subclass?)

Schedule class (object?)

Scheduling Algorithm

Overtime function (returns hours of overtime worked)

Employee Pay function (counting overtime)

Testing/Fixing
"""

class Employee:
    """The employee class"""
    def __init__(self,name, hourly_rate, shifts, overtime_eligibility):
        self.name = name
        self.hourly_rate = hourly_rate
        self.shifts = shifts
        self.overtime_eligibility = overtime_eligibility
             
        pass
        
    """
    Calculates and designates a given Employee's pay.

    Params:
    - name (string)
    - hourly_rate (float)
    - shifts (int)
    - overtime_eligibility (bool)

    Returns:
    - compensation (float)
    """
    def PayEmployee(self, name, hourly_rate, shifts, overtime_eligibility):
        #assuming each "shift" is 8 hours.
        self.compensation = self.hourly_rate * self.hours_scheduled
        #employee object's compensation = hourly * hours scheduled
        return self.compensation
               
    """
    Calculates and designates a given Employee's overtime pay.

    Params:
    - hours_worked (int)

    Returns:
    - overtime, which is hours_worked times the hourly_rate Employee attribute
    """
    def EmployeeOvertime(self, hours_worked):
        #takes hours worked (passed in), uses self.hourly_rate to calculate pay
        return hours_worked * self.hourly_rate
        pass
        
    def assign(self):
        """Assign an employee to a workweek slot.
        removes an employee's available shifts.
        Checks if there's available shifts, then removes one. Returns true,
        If no available shifts, returns false.
        """
        if self.shifts > 0:
            self.shifts -= -1 #remove one of their shifts
            return True
        else:
            return False
    """
    Copies an Employee object for future usage.

    Returns:
    The passed Employee object.
    
    """                    
    def copy(self):
        return Employee(self.name, self.hourly_rate, self.shifts, self.overtime_eligibility)
    """
    The following functions: name(), shifts(), and rate() are designated as helper
    functions for debugging with the Employee class. 

    Returns:
    The Employee object's attribute that corresponds with the function name.
    
    """    
    #for debugging    
    def name(self):
        return self.name
    
    def shifts(self):
        return self.shifts
    
    def rate(self):
        return self.hourly_rate
    

class WorkWeek:
    """An object that is used to organize employee schedules
        Days, morning/afternoon/night (what shifts), people needed each day
    """
    def __init__(self,days,shifts,workers): #WorkWeek(5,(morning,night),5) -> 5 days to fill for morning shift and night shift, 5 people each day
        self.week = []
        self.days = days #int, days of the week with shifts to schedule
        self.shifts = shifts #tuple, shifts (morning, afternoon, night).
        self.workers = workers #int, number of workers per shift
       
        #if do WorkWeek(4,(morning,night),5) then  object should look like
        # [(5,5),(5,5),(5,5),(5,5)] 
        for i in range(0,days):
            for i in range(0,len(shifts)):
                self.week.append(int(workers)) #worried about mutability here.
            
        #shift will be a tuple with the hours shifts = (morning,afternoon,night) or like shifts = (morning, night)        
        #each slot = day of the week to work.
        pass
    """
    
    """
    def EmployeeOvertime(self, hourly_rate, hours_worked):
        #sw = pd.read_csv("workweek.csv", info = ["days", "shifts", "workers"])
        pass
        
    """
    An info()-esque function detailing the properties and attributes of a given WorkWeek.

    Returns:
    - An f-string statement detailing a given WorkWeek
    """
    def Peep(self):
        return f"WorkWeek: {self.week, self.days, self.shifts, self.workers}"

class Scheduler: ##algorithm
    """the main thing here
    Approach: a greedy algorithm to pick “the best employee for this time slot”
        
    Rules: 
    • Match employees to shift based on their availability (first priority)
    • Don't violate labor laws (how many hours)
    • Respect minimum/maximum hour restrictions per-employee basis
    • Avoid scheduling conflicts (don't put too many/few people on shift, but also literally don't put people who hate each other on the same shift)
    
    """
    def __init__(self):
        pass
    
    def algorithm(self):
        pass


def Schedule(team,workweek):
    """the schedule algorithm to assign workers to a workweek
    Arguments:
    team: list of employee objects
    workweek: slots and times for what the workweek looks like
    """
    if workweek == []:
        return {} #empty
    for worker in team:
        if worker.shifts > 0:
            for slots in workweek.week: #slots is the int variable for "workers" per shift
                wc = worker.copy()
                new_team = []
                wc.assign()
                #decrement the worker total in the shift of workweek's week list []
                

if __name__ == "__main__":
    employees = pd.read_csv("employees.csv", names = ["name", "hourly rate", "shifts", "overtime eligibility"])
    #^^ use above function to create employees that we can put into the scheduler
    
    sw = pd.read_csv("workweek.csv", info = ["days", "shifts", "workers"])
    #^^ use above function to create workweek that we can put into the scheduler
