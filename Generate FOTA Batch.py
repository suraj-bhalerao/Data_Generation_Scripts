import csv
import random
from datetime import datetime, timedelta

def generate_random_imei():
    return ''.join([str(random.randint(0, 9)) for _ in range(15)])

def generate_random_uin():
    return 'ACON4NA' + ''.join([str(random.randint(0, 9)) for _ in range(10)])

def add_device_data(file_path, number_of_records):
    ufw = "5.2.14"
    model = "4G"
    state = "Maharashtra"
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["UIN", "UFW", "MODEL", "STATE", "IMEI"])
        
        for _ in range(number_of_records):
            uin = generate_random_uin()
            imei = generate_random_imei()
            writer.writerow([uin, ufw, model, state, imei])

file_path = "device_data.csv"
number_of_records = 10
add_device_data(file_path, number_of_records)
print(f"{number_of_records} records have been written to {file_path}.")
