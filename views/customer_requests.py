import sqlite3
import json
from models import Customer

CUSTOMERS = [
  {
    "id": 1,
    "name": "Ty",
  }, {
    "id": 2,
    "name": "Astrid"
  }
]

def get_all_customers():
#   return CUSTOMERS
  with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(row['id'], row['name'], row ['address'],
                            row['email'], row['password'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
        return json.dumps(customer)
  




def get_single_customer(id):
  requested_customer = None
  
  for customer in CUSTOMERS:
    if customer["id"] == id:
      requested_customer == customer
      
  return requested_customer

def create_customer(customer):
  max_id = CUSTOMERS[-1]["id"]
  
  new_id = max_id + 1
  
  customer["id"] = new_id
  
  CUSTOMERS.append(customer)
  
  return customer   

def delete_customer(id):
  customer_index = -1
  
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      customer_index = index
      
  if customer_index >= 0:
    CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      
      CUSTOMERS[index] = new_customer
      break
