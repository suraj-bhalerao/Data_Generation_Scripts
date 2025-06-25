import csv
import random
from datetime import datetime, timedelta

# Function to generate random IMEI number
def generate_random_imei():
    return ''.join([str(random.randint(0, 9)) for _ in range(15)])

# Function to generate random ICCID number
def generate_random_iccid():
    return '8991' + ''.join([str(random.randint(0, 9)) for _ in range(16)])

# Function to generate random VIN number
def generate_random_vin():
    return 'ACCDEV' + ''.join([str(random.randint(0, 9)) for _ in range(9)])

# Function to generate random UIN
def generate_random_uin():
    return 'ACON4NA2024' + ''.join([str(random.randint(0, 9)) for _ in range(6)])

# Function to generate random dates within a range
def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%m/%d/%Y')

# Constants for the file
destination_file = "generated_records.csv"
number_of_records = 100

# Static fields
card_status = "Active"
dealer_state = "Maharashtra"
device_model = "AEPL051400"
vehicle_model = "COMM"

# Date ranges
current_year = datetime.now().year
bootstrap_start_date = datetime(current_year, 1, 1)
bootstrap_end_date = datetime(current_year + 5, 12, 31)
dispatch_start_date = datetime(current_year, 1, 1)
dispatch_end_date = datetime(current_year + 1, 12, 31)

# Writing to CSV
with open(destination_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow([
        "uin", "vinNo", "iccid", "imei", "cardStatus", "deviceModel", "bootstrapExpiryDate", 
        "dealerState", "vehicleModel", "vehicleDispatchDate"
    ])

    # Write records
    for _ in range(number_of_records):
        uin = generate_random_uin()
        vin_no = generate_random_vin()
        iccid = generate_random_iccid()
        imei = generate_random_imei()
        bootstrap_expiry_date = generate_random_date(bootstrap_start_date, bootstrap_end_date)
        vehicle_dispatch_date = generate_random_date(dispatch_start_date, dispatch_end_date)

        writer.writerow([
            uin, vin_no, iccid, imei, card_status, device_model, bootstrap_expiry_date,
            dealer_state, vehicle_model, vehicle_dispatch_date
        ])

print(f"{number_of_records} records have been written to {destination_file}.")
