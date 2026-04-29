#PyTesting

from main import WorkWeek
from main import Employee

AWeek = WorkWeek(2,("morning","night"),6)
#print(AWeek.Peep()) #debugging

Worker_Amanda = Employee("Amanda",15,5,True)

def test_WorkWeekArrays():
  assert [6,6,6,6] == AWeek.week
  
def test_EmployeeCreation():
  assert Worker_Amanda.name == "Amanda"
  assert Worker_Amanda.rate == 15
  assert Worker_Amanda.shifts == 5

def test_EmployeeOvertime():
  assert Worker_Amanda.EmployeeOvertime(5) == 75
