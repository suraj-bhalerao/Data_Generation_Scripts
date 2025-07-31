import csv
import random

# --- Static configuration ---
UFW_VERSION = "5.2.14"       # Firmware version
MODEL = "AEPL051401"         # Device model
STATE = "Maharashtra"        # State for all devices
UIN_PREFIX = "ACON4NA2024"   # UIN base

# --- Utility functions ---
def generate_random_imei():
    """Generate a random 15-digit IMEI"""
    return ''.join(str(random.randint(0, 9)) for _ in range(15))

def generate_random_uin():
    """Generate a UIN with a fixed prefix and 6 random digits"""
    return UIN_PREFIX + ''.join(str(random.randint(0, 9)) for _ in range(6))

# --- Main function ---
def generate_fota_batch_csv(file_path, number_of_records):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["UIN", "UFW", "MODEL", "STATE", "IMEI"])

        for _ in range(number_of_records):
            uin = generate_random_uin()
            imei = generate_random_imei()
            writer.writerow([uin, UFW_VERSION, MODEL, STATE, imei])

    print(f"✅ {number_of_records} FOTA records written to '{file_path}'")
