# INST326_FinalProject_2026
Final Project for INST326, scheduler code.

CSV: 
Employees:
name = string
hourly_rate = int
min_hours = int
max_hours = int
overtime_eligibility = boolean

Workweek:
days = int
shift = tuple (ie: morning, night || morning,evening,night)
people = int

example: WorkWeek(5,(morning,night),5) -> 5 days to fill for morning shift and night shift, 5 people each day
