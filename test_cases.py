#PyTesting

from main import WorkWeek
from main import Employee

AWeek = WorkWeek(2,("morning","night"),6)
#print(AWeek.Peep()) #debugging

"""
Test Employee: Amanda
"""

Worker_Amanda = Employee("Amanda",15,5,True)

def test_WorkWeekArrays():
  assert [6,6,6,6] == AWeek.week
  
def test_EmployeeCreation():
  assert Worker_Amanda.name == "Amanda"
  assert Worker_Amanda.rate == 15
  assert Worker_Amanda.shifts == 5

def test_EmployeeOvertime():
  assert Worker_Amanda.EmployeeOvertime(5) == 75


"""
2nd test employee: Pete
"""

Worker_Pete = Employee("Pete", 20, 4, True)

def test_EmployeeCreation():
  assert Worker_Pete.name == "Pete"
  assert Worker_Pete.rate == 20
  assert Worker_Pete.shifts == 4

def test_EmployeeOvertime():
  assert Worker_Pete.EmployeeOvertime(4) == 80

"""
3rd Test Employee: Ronny
"""

Worker_Ronny = Employee("Ronny", 14, 4, True)

def test_EmployeeCreation():
  assert Worker_Ronny.name == "Ronny"
  assert Worker_Ronny.rate == 14
  assert Worker_Ronny.shifts == 4

def test_EmployeeOvertime():
  assert Worker_Ronny.EmployeeOvertime(6) == 84



