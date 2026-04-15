##helllooosdgodsjgudhguds 

##welcome to employee scheduler

##https://docs.google.com/document/d/1YpV-ogQQxIFtVheAZmlEN7b4XcfP5fMGdnFcMEgYbpI/edit?tab=t.0
## ^^ the document with the stuuf
"""hi"""
"""

> A job has employees (employee objects) that have employee name, hourly wage, min hours, max hours, overtime eligibility, is_available (boolean, for the staffing algorithm)
    >can add/override each thing, dont need to instantiate with this?
    
> create "workweek" object (Days, morning/afternoon/night (what shifts), people needed each day) ASSUMES that each day has same hours/needed employees
    >template? empty? just basically a "hey i need this"
    >shifts have times that can be returned i guess idk where this goes

> Algorithm//  add employees to a "workweek" object, return a filled out "schedule" object (is a workweek?) based on employee stats & needed work for the job.
    >this is done by the scheduler algorithm.
    >assumes one person by shift
    
    > return Day 1: Abby/Morning, Dave/Morning, Carol/Afternoon, Sarah/Night || Day 2: Carol/Morning, 
    
"""

'''TO DO LIST:

Data -> i/o csv => the thing that reads. (Exercise 2 - Finder as a base?)

Initial docstrings and unit tests

Employee Class

Employee Preferences (in class? out? subclass?)

Schedule class (object?)

Scheduling Algorithm

Overtime function (returns hours of overtime worked)

Employee Pay function (counting overtime)

Testing/Fixing
'''

class Employee:
    """The employee class"""
    def __init__(self):
        pass

    def PayEmployee(self, name, hourly_rate, min_hours, max_hours, overtime_eligibility):
        self.compensation = self.hourly_rate * self.hours_scheduled
        return self.compensation

    def EmployeeOvertime(self, hourly_rate, hours_worked):
        pass


class WorkWeek:
    """An object that is used to organize employee schedules
        Days, morning/afternoon/night (what shifts), people needed each day)
    
    """
    def __init__(self,days,shifts,workers): #WorkWeek(5,(morning,night),5) -> 5 days to fill for morning shift and night shift, 5 people each day
        
        #shift will be a tuple with the hours shifts = (morning,afternoon,night) or like shifts = (morning, night)        
        #each slot = day of the week to work.
        pass

    def EmployeeOvertime(self, hourly_rate, hours_worked):
        pass


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



