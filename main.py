##helllooosdgodsjgudhguds 

##welcome to employee scheduler

##https://docs.google.com/document/d/1YpV-ogQQxIFtVheAZmlEN7b4XcfP5fMGdnFcMEgYbpI/edit?tab=t.0
## ^^ the document with the stuff
import pandas as pd

class Employee:
    """The employee class:
    takes name, hourly_rate, shifts, overtime_eligibility"""
    def __init__(self,name="John Doe", hourly_rate=0, shifts=0, overtime_eligibility=False):
        self.name = name
        self.hourly_rate = hourly_rate
        self.shifts = shifts
        self.overtime_eligibility = overtime_eligibility
             
        pass

    def PayEmployee(self, hours_scheduled=0):    
    """Calculates and designates the current Employee's pay.

    Params:
    - name (string)
    - hourly_rate (float)
    - shifts (int)
    - overtime_eligibility (bool)

    Returns:
    - compensation (float)

    Authors: Alexis Smith, Jordan Williams
    """
        #assuming each "shift" is 8 hours.
        self.hours_scheduled = hours_scheduled
        self.compensation = self.hourly_rate * self.hours_scheduled
        #employee object's compensation = hourly * hours scheduled
        return self.compensation

    def EmployeeOvertime(self, hours_worked=0):              
    """Calculates and designates a given Employee's overtime pay.

    Params:
    - hours_worked (int)

    Returns:
    - overtime, which is hours_worked times the hourly_rate Employee attribute
    """
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
            self.shifts -= 1 #remove one of their shifts
            return True
        else:
            return False
            
    """
    Copies an Employee object for future usage (helper method).

    Returns:
    The passed Employee object.
    
    """                    
    def copy(self):
            """
        Copies an Employee object for future usage.

        Returns:
        The passed Employee object.

        Authors: Alexis Smith, Jordan Williams
        """      
        return Employee(self.name, self.hourly_rate, self.shifts, self.overtime_eligibility)

    """
    Assorted custom magic methods (helper method)
    """
    #for debugging
    def __repr__(self):
        return (f"{self.name},{self.shifts},{self.hourly_rate}")
        
    def __str__(self):
        return (f"{self.name}")
    
    def __lt__(self, other): #allows for sorting of employee objects by the number of shifts they have
        if not isinstance(other, Employee):
            return NotImplemented 
        return self.shifts > other.shifts

"""
Return all employee entries from a given .csv file parameter. 

Authors: Alexis Smith, Aishwarya Thalla
"""
def get_employees(file):
    df = pd.read_csv(file)
    employees = []
    for i, row in df.iterrows():
        name = row["name"]
        hourly_rate = int(row["hourly_rate"])
        shifts = int(row["shifts"])
        overtime = str(row["overtime_eligibility"]).lower() == "true"
        employees.append(Employee(name, hourly_rate, shifts, overtime))
    return employees
    
"""
Return all workweek entries from a given .csv file parameter. 
Authors: Alexis Smith, Aishwarya Thalla
"""
def get_workweek(file):
    df = pd.read_csv(file)
    workweeks = []
    for i, row in df.iterrows():
        days = int(row["days"])
        shifts = tuple(shift.strip() for shift in row["shifts"].split(","))
        workers = int(row["workers"])
        workweeks.append(WorkWeek(days, shifts, workers))
    return workweeks

class WorkWeek:
    """An object that is used to organize employee schedules
        Days, morning/afternoon/night (what shifts), people needed each day
    """
    def __init__(self, days=0, shifts=(), workers=0): #WorkWeek(5,(morning,night),5) -> 5 days to fill for morning shift and night shift, 5 people each day
        self.week = []
        self.days = days #int, days of the week with shifts to schedule
        self.shifts = shifts #tuple, shifts (morning, afternoon, night).
        self.workers = workers #int, number of workers per shift
       
        #if do WorkWeek(4,(morning,night),5) then  object should look like
        # [(5,5),(5,5),(5,5),(5,5)] 
        for i in range(0, days):
            for i in range(0, len(shifts)):
                self.week.append(int(workers)) #worried about mutability here.
            
        #shift will be a tuple with the hours shifts = (morning,afternoon,night) or like shifts = (morning, night)        
        #each slot = day of the week to work.
        pass
        
    def __str__(self):
        """
        Returns a formatted string of all attributes of a WorkWeek object for debugging purposes
        Authors: Alexis Smith, Jordan Williams
        """
        return f"Workweek: {self.week}, {self.days}, {self.shifts}, {self.workers}"
   
    """
    Calculates Employee overtime
    """
    def EmployeeOvertime(self, hourly_rate=0, hours_worked=0):
        #this function goes unusued?
        #sw = pd.read_csv("workweek.csv", info = ["days", "shifts", "workers"])
        pass
        
    """
    An info()-esque function detailing the properties and attributes of a given WorkWeek.

    Returns:
    - An f-string statement detailing a given WorkWeek
    """
    def __repr__(self):
        return f"WorkWeek: {self.week, self.days, self.shifts, self.workers}"


def Schedule(workers,workweek):
    """the main schedule algorithm to assign workers to a workweek
    Arguments:
    team: list of employee objects
    workweek: slots and times for what the workweek looks like
    
    Returns: a list of available employees given the workweek criteria.
    
    Goals:
    Always fill entire schedule
    Do not exceed employee shift limits
    Allow worker's wanted shifts to go unused if necessary
    
    Authors: Elizabeth Metzler & Aishwarya Thalla
    """    
  
    feasibility(workers,workweek) #could throw value error if failed
    
    #STARTER VARIABLES
    shift_dict = {}
    assignments =[] #empty assignment/"schedule" structure. Will be the final return object.

    #making a copy of each employee so original data will not be affected (maintain mutability)
    team = []
    for employee in workers:
        team.append(employee.copy()) #add all the new employees into a NEW 'team' object to iterate over later. (maintain mutability)
            
    template_week = [] #used to maintain structure for iterating and slotting employees
    for needed in workweek.week:
        for _ in range(needed): #needed = whatever number of employees was passed into the shift from workweek (ie [5,5,5,5] needed = 5... but replaced with _ in template week
            template_week.append("_")
        
    for employee in team:
        shift_dict[employee.name] = 0
            
    for _ in template_week:
        available = []
            
        for employee in team:
            if employee.shifts > 0:
                available.append(employee)
                
        if not available:
            raise ValueError("Ran out of workers while scheduling")
            
            #sort for fairness
        available.sort(reverse=True)
        worker = available[0]
            
        for employee in available: #look through the sorted list, find least assigned person
            #note: since already sorted by shifts in descending order, this finds the person with the most desired shifts and least assignments
            if shift_dict[employee.name] < shift_dict[worker.name]:
                worker = employee #not assigned yet
            
        #GREAT we got the employee with most wanted shifts, least assignments.
        #assign her.
        worker.assign()
        shift_dict[worker.name] +=1 #increment fairness counter
        assignments.append(worker) #add to final roster
            
    return assignments
                

def feasibility(team,workweek): #helper function for Scheduler
        """A helper function to use in conjunction with the Schedule function, sums the days of the week and the possible shifts of employees
        to see if a desired workweek can be created with the given parameters
        
        Arguments: 
        team, a list of employee objects
        workweek, a workweek class object
        
        Returns: True if possible, ValueError if false
        
        Authors: Elizabeth Metzler & Aishwarya Thalla"""
    
        req = sum(workweek.week)
        possible = sum(employee.shifts for employee in team)
        
        if possible < req:
            raise ValueError(f"Not enough to fill schedule: need: {req} have: {possible} deficit: {req - possible}. Add more workers or increase shift)")

def CalculatePaychecks(assignments):
    """For use after Schedule() is called. Takes assignments and then calls Employee.PayEmployee() to return a dictionary of employee's paychecks
    given the workweek they are working from the generated Schedule()
    
    returns: 
        Dictionary: {Employee name: paycheck}
        
    Authors: Alexis Smith, Elizabeth Metzler"""
    shift_count = {}
    
    #count assigned shifts:
    for employee in assignments:
        shift_count[employee.name] = shift_count.get(employee.name, 0) + 1 #accumulator count
    paychecks = {}
    
    for employee in assignments:
        if employee.name not in paychecks:
            hours = shift_count[employee.name] * 8 
            #Multiplying by 8 because we assume each shift is 8 hours of working, and
            #Employee.PayEmployee takes hours, not #'s of shifts.
            paychecks[employee.name] = employee.PayEmployee(hours)
    return paychecks

"""
Running our final Schedule algorithm within an if __name__ == "__main__" block. 
"""
if __name__ == "__main__":
    """
    Initializing employees and retrieving them from our .csv files, setting up the workweek, and initializing a Schedule to organize employees. 
    """
    employees = get_employees("employees.csv")
    workweeks = get_workweek("workweek.csv")
    workweek_number = int(input("\nEnter the number of the workweek to schedule: ")) -1
    workweek = workweeks[workweek_number]
    week_assignments = Schedule(employees,workweek)
    slot = 0

    """
    Iterates through a given WorkWeek and lists corresponding employee paychecks 
    """
    for day in range(workweek.days):
        for shift in workweek.shifts:
            names = []
            for _ in range(workweek.workers):
                names.append(week_assignments[slot].name)
                slot +=1
            print(f"Day {day+1} - {shift}: {', '.join(names)}")
    paychecks = CalculatePaychecks(week_assignments)

    print("\n Paychecks:")
    for name in paychecks:
        print(f"{name}:, ${paychecks[name]}")
            
    #employees = pd.read_csv("employees.csv", names = ["name", "hourly rate", "shifts", "overtime eligibility"])
    #^^ use above function to create employees that we can put into the scheduler
    
    #sw = pd.read_csv("workweek.csv", info = ["days", "shifts", "workers"])
    #^^ use above function to create workweek that we can put into the scheduler

    #below code meant to print employees and workweek lists to verify functionality, will be changed/removed after scheduling algorithm is made
    #employees = get_employees("employees.csv")
    #print(f"Loaded {len(employees)} employees: ")
    #for employee in employees:
    #    print(f"{employee.name} | rate: ${employee.rate}/her | shifts: {employee.shifts} | overtime: {employee.overtime_eligibility}")

    #workweeks = get_workweek("workweek.csv")
    #print(f"\nLoaded {len(workweeks)} workweek structures: ")
    #for workweek in workweeks:
    #    print(f"{workweek.__str__()}")
