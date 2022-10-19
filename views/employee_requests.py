from curses.ascii import EM
from .location_requests import LOCATIONS
import random
EMPLOYEES = [
  {
    "name": "Rochelle",
    "id": 1,
    "locationId": 1,
  }, {
    "name": "Cat",
    "id": 2,
    "locationId": 2
  }
]

def get_all_employees():
  return EMPLOYEES

def get_single_employee(id):
  requested_employee = None
  
  for employee in EMPLOYEES:
    if employee["id"] == id:
            requested_employee = employee

    return requested_employee
  
def create_employee(employee):
    
  max_id = EMPLOYEES[-1]["id"]
  
  new_id = max_id + 1

  employee["id"] = new_id
    
  # new_location_id = random.choice(LOCATIONS["id"])
  # print(new_location_id) 
  # employee["locationId"] = new_location_id

  EMPLOYEES.append(employee)

  return employee

def delete_employee(id):
  
  employee_index = -1
  
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      employee_index = index
      
  if employee_index >= 0:
    EMPLOYEES.pop(employee_index)
