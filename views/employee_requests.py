import sqlite3
import json
from models import Employee, Location

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
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
      e.id,
      e.name,
      e.address,
      e.location_id,
      l.name location_name,
      l.address location_address
    FROM Employee e
    JOIN Location l
        ON l.id = e.location_id
    """)
    
    employees = []
    
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      employee = Employee(row["id"], row["name"], row["address"], row["location_id"])
      
      location = Location(row['id'], row['location_name'], row['location_address'])
      
      employee.location = location.__dict__
      
      employees.append(employee.__dict__)
      
    return json.dumps(employees)

def get_single_employee(id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        e.id,
        e.name,
        e.address,
        e.location_id
    FROM employee e
    WHERE e.id = ?
    """, (id,))
    
    employees = []
    dataset = db_cursor.fetchall()
    
    for row in dataset:
      employee = Employee(row["id"], row["name"], row["address"], row["location_id"])
      
      employees.append(employee.__dict__)
      
    return json.dumps(employees)
  
def get_employees_by_location(location_id):
  with sqlite3.connect("./kennel.sqlite3") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    
    db_cursor.execute("""
    SELECT
        e.id,
        e.name,
        e.address,
        e.location_id
    FROM employee e
    WHERE e.id = ?
    """, (location_id,))
    
    data = db_cursor.fetchone()
    
    employee = Employee(data["id"], data["name"], data["address"], data["location_id"])
    
    return json.dumps(employee.__dict__)
  
def create_employee(employee):
    
  max_id = EMPLOYEES[-1]["id"]
  
  new_id = max_id + 1

  employee["id"] = new_id

  EMPLOYEES.append(employee)

  return employee

def delete_employee(id):
  
  employee_index = -1
  
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      employee_index = index
      
  if employee_index >= 0:
    EMPLOYEES.pop(employee_index)
    
def update_employee(id, new_employee):
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id:
      EMPLOYEES[index] = new_employee
      break
