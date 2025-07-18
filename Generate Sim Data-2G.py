import csv
import random
from datetime import datetime, timedelta

# Function to generate random 17-character chassis number
def generate_random_chassis_no():
    return 'MAT' + ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=14))

# Function to generate random ICCID number (20-digit)
def generate_random_iccid():
    return '8991' + ''.join([str(random.randint(0, 9)) for _ in range(16)])

# Function to generate random IMEI number (15-digit)
def generate_random_imei():
    return ''.join([str(random.randint(0, 9)) for _ in range(15)])

# Function to generate random SERIAL_NO
def generate_random_serial_no():
    return f'{device_model}' + ''.join([str(random.randint(0, 9)) for _ in range(10)])

# Function to generate random engine number
def generate_random_engine_no():
    return 'B6.7B6A250D02102' + ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))

# Function to generate a random registration number
def generate_random_reg_number():
    return random.choice(['MH', 'TN', 'RJ', 'KA', 'DL']) + str(random.randint(10, 99)) + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + str(random.randint(1000, 9999))

# Function to generate random dealer name
def generate_random_dealer_name():
    return random.choice([
        "1001860-Sales-Chennai-PopMeg", "1003530-Sales-Nerul-KAMAL", "1001140-Sales-Hanumangarh-DunacA"
    ])

# Function to generate random RTO office code and state
def generate_random_rto():
    rto_offices = {
        "TN": "TN 5", "MH": "MH 12", "RJ": "RJ 14", "KA": "KA 03", "DL": "DL 01"
    }
    state = random.choice(list(rto_offices.keys()))
    return rto_offices[state], state

# Function to generate random mobile number
def generate_random_mobile_number():
    return '9' + ''.join([str(random.randint(0, 9)) for _ in range(9)])

# Function to generate random dates within a range
def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%d-%b-%y')

# Function to generate random vehicle model
def generate_random_vehicle_model():
    manufacturers = ['HONDA', 'SUZUKI', 'TATA', 'HYUNDAI', 'FORD', 'TOYOTA', 'MAHINDRA', 'BMW', 'MERCEDES', 'KIA']
    models = ['Sedan', 'SUV', 'Hatchback', 'Truck', 'Electric', 'Hybrid']
    return f"{random.choice(manufacturers)} {random.choice(models)}"

# Constants for generating data
number_of_records = 5
device_make = "ACCOLADE"
device_model = "ACON4IA"
primary_operators = ['BHA', 'Airtel', 'Jio']
secondary_operators = ['BSNL', 'Vodafone']
sim_status_options = ['Active', 'Inactive']
activation_status_options = ['Commercial', 'Pending']
vahan_upload_status_options = ['SUCCESS', 'FAILED']

# Date ranges
current_year = datetime.now().year
activation_start_date_range = datetime(current_year - 5, 1, 1)
activation_end_date_range = datetime(current_year + 5, 12, 31)

# File destination
destination_file = "Card_details_sb_2G.csv"

# Writing to CSV
with open(destination_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    headers = [
        "CHASSIS_NO", "ICCID", "IMEI", "SERIAL_NO", "DEVICE_MAKE", "DEVICE_MODEL", 
        "ENGINE_NO", "REG_NUMBER", "DEALER_NAME", "DEALER_CODE", "RTO_OFFICE_CODE", 
        "RTO_STATE", "PRIMARY_OPERATOR", "PRIMARY_MOBILE_NUMBER", "SECONDARY_OPERATOR", 
        "SECONDARY_MOBILE_NUMBER", "VEHICLE_MODEL", "SIM_STATUS", "ACTIVATION_STATUS", 
        "ACTIVATION_STATUS_DATE", "ACTIVATION_EXPIRY", "VAHAN_UPLOAD_STATUS"
    ]
    writer.writerow(headers)

    # Generate and write records
    for _ in range(number_of_records):
        chassis_no = generate_random_chassis_no()
        iccid = generate_random_iccid()
        imei = generate_random_imei()
        serial_no = generate_random_serial_no()
        engine_no = generate_random_engine_no()
        reg_number = generate_random_reg_number()
        dealer_name = generate_random_dealer_name()
        dealer_code = dealer_name.split('-')[0]
        rto_office_code, rto_state = generate_random_rto()
        primary_operator = random.choice(primary_operators)
        primary_mobile_number = generate_random_mobile_number()
        secondary_operator = random.choice(secondary_operators)
        secondary_mobile_number = generate_random_mobile_number()
        vehicle_model = generate_random_vehicle_model()
        sim_status = random.choice(sim_status_options)
        activation_status = random.choice(activation_status_options)
        activation_status_date = generate_random_date(activation_start_date_range, activation_end_date_range)
        activation_expiry = generate_random_date(activation_start_date_range, activation_end_date_range)
        vahan_upload_status = random.choice(vahan_upload_status_options)

        writer.writerow([
            chassis_no, iccid, imei, serial_no, device_make, device_model, engine_no, 
            reg_number, dealer_name, dealer_code, rto_office_code, rto_state, 
            primary_operator, primary_mobile_number, secondary_operator, 
            secondary_mobile_number, vehicle_model, sim_status, activation_status, 
            activation_status_date, activation_expiry, vahan_upload_status
        ])

print(f"{number_of_records} records have been written to {destination_file}.")