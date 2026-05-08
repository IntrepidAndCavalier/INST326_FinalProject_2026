#PyTesting

from main import WorkWeek
from main import Employee
from main import get_employees
from main import get_workweek

AWeek = WorkWeek(2,("morning","night"),6)
#print(AWeek.Peep()) #debugging

"""
Test Employee: Amanda
"""

Worker_Amanda = Employee("Amanda",15,5,True)

def test_WorkWeekArrays():
  assert [6,6,6,6] == AWeek.week
  
def test_AmandaCreation():
  assert Worker_Amanda.name == "Amanda"
  assert Worker_Amanda.hourly_rate == 15
  assert Worker_Amanda.shifts == 5

def test_AmandaOvertime():
  assert Worker_Amanda.EmployeeOvertime(5) == 75


"""
2nd test employee: Pete
"""

Worker_Pete = Employee("Pete", 20, 4, True)

def test_PeteCreation():
  assert Worker_Pete.name == "Pete"
  assert Worker_Pete.hourly_rate == 20
  assert Worker_Pete.shifts == 4

def test_PeteOvertime():
  assert Worker_Pete.EmployeeOvertime(4) == 80

"""
3rd Test Employee: Ronny
"""

Worker_Ronny = Employee("Ronny", 14, 4, True)

def test_RonnyCreation():
  assert Worker_Ronny.name == "Ronny"
  assert Worker_Ronny.hourly_rate == 14
  assert Worker_Ronny.shifts == 4

def test_RonnyOvertime():
  assert Worker_Ronny.EmployeeOvertime(6) == 84

"""
4th Test Employee: Gerald
"""

Worker_Gerald = Employee("Gerald", 10, 3, True)

def test_GeraldCreation():
  assert Worker_Gerald.name == "Gerald"
  assert Worker_Gerald.hourly_rate == 10
  assert Worker_Gerald.shifts == 3

def test_GeraldOvertime():
  assert Worker_Gerald.EmployeeOvertime(3) == 30

"""
Test get_employees
"""
def test_get_employees_count():
  employees = get_employees("employees.csv")
  assert len(employees) == 21

def test_get_employees_first_row():
  employees = get_employees("employees.csv")
  elizabeth = employees[0]
  assert elizabeth.name == "Elizabeth"
  assert elizabeth.hourly_rate == 30
  assert elizabeth.shifts == 4
  assert elizabeth.overtime_eligibility == True

"""
Test get_workweek
"""
def test_get_workweek_count():
  workweeks = get_workweek("workweek.csv")
  assert len(workweeks) == 5

def test get_workweek_first_row():
  workweeks = get_workweek("workweek.csv")
  workweek = workweeks[0]
  assert workweek.days == 5
  assert workweek.shifts == ("morning","night")
  assert workweek.workers == 6



