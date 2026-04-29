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
        self.min_hours = min_hours
        self.max_hours = max_hours
        self.overtime_eligibility = overtime_eligibility
             
        pass

    def PayEmployee(self, name, hourly_rate, shifts, overtime_eligibility):
        #assuming each "shift" is 8 hours.
        self.compensation = self.hourly_rate * self.hours_scheduled
        #employee object's compensation = hourly * hours scheduled
        return self.compensation
               

    def EmployeeOvertime(self, hours_worked):
        #takes hours worked (passed in), uses self.hourly_rate to calculate pay
        pass
        
    def assign(self)
        """Assign an employee to a workweek slot.
        removes an employee's available shifts.
        Checks if there's available shifts, then removes one. Returns true,
        If no available shifts, returns false.
        """
        if self.shifts > 0:
            self.shifts -= -1 //remove one of their shifts
            return true
        else:
            return false
    def copy(self):
        return Worker(self.name, self.hourly_rate, self.shifts, self.overtime_eligibility)
        

class WorkWeek:
    """An object that is used to organize employee schedules
        Days, morning/afternoon/night (what shifts), people needed each day
    """
    def __init__(self,days,shifts,workers): #WorkWeek(5,(morning,night),5) -> 5 days to fill for morning shift and night shift, 5 people each day
        self.workweek = []
        self.days = days #int, days of the week with shifts to schedule
        self.shifts = shifts #tuple, shifts (morning, afternoon, night).
        self.workers = workers #int, number of workers per shift
       
        #if do WorkWeek(4,(morning,night),5) then  object should look like
        # [(5,5),(5,5),(5,5),(5,5)] 
        for i in range(0,days):
            for i in range(0,len(shifts))
            workweek.append(int(workers)) #worried about mutability here.
            
        #shift will be a tuple with the hours shifts = (morning,afternoon,night) or like shifts = (morning, night)        
        #each slot = day of the week to work.
        pass

    def EmployeeOvertime(self, hourly_rate, hours_worked):
        #sw = pd.read_csv("workweek.csv", info = ["days", "shifts", "workers"])


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
    if workweek == []
        return {}
    for worker in team:
        if worker.shifts > 0
            for 

if __name__ == "__main__":
    employees = pd.read_csv("employees.csv", names = ["name", "hourly rate", "shifts", "overtime eligibility"])
    #^^ use above function to create employees that we can put into the scheduler
    
    sw = pd.read_csv("workweek.csv", info = ["days", "shifts", "workers"])
    #^^ use above function to create workweek that we can put into the scheduler

    
