import csv
import random
from datetime import datetime, timedelta
import sys

# Mapping technology -> device model
DEVICE_MODEL_MAP = {
    "2G": "AEPL051300",
    "4G": "AEPL051400"
}

# Pools for dynamic values
CARD_STATUS_POOL = ["Active", "Inactive", "Pending"]
DEALER_STATE_POOL = ["Maharashtra", "Karnataka", "Tamil Nadu", "Delhi"]
VEHICLE_MODEL_POOL = ["COMM", "SUV", "Sedan", "Truck", "Electric"]
UIN_PREFIX = "ACON4NA2024"

def generate_random_imei():
    return ''.join(str(random.randint(0, 9)) for _ in range(15))

def generate_random_uin():
    return UIN_PREFIX + ''.join(str(random.randint(0, 9)) for _ in range(6))

def generate_random_vin():
    return "ACCDEV" + ''.join(str(random.randint(0, 9)) for _ in range(9))

def generate_random_iccid():
    return "8991" + ''.join(str(random.randint(0, 9)) for _ in range(16))

def random_date_between(start_date, end_date):
    delta = end_date - start_date
    return (start_date + timedelta(days=random.randint(0, delta.days))).strftime("%m/%d/%Y")

def generate_sim_batch_csv(technology: str = "4G", num_records: int = 10):
    tech = technology.upper()
    if tech not in DEVICE_MODEL_MAP:
        raise ValueError("Unsupported technology. Choose '2G' or '4G'.")

    device_model = DEVICE_MODEL_MAP[tech]
    card_status = random.choice(CARD_STATUS_POOL)
    dealer_state = random.choice(DEALER_STATE_POOL)
    vehicle_model = random.choice(VEHICLE_MODEL_POOL)

    current_year = datetime.now().year
    bootstrap_start = datetime(current_year, 1, 1)
    bootstrap_end = datetime(current_year + 5, 12, 31)
    dispatch_start = datetime(current_year, 1, 1)
    dispatch_end = datetime(current_year + 1, 12, 31)

    date_str = datetime.today().strftime("%Y%m%d")
    output_file = f"sim_batch_{tech}_{date_str}.csv"

    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "uin", "vinNo", "iccid", "imei",
            "cardStatus", "deviceModel",
            "bootstrapExpiryDate", "dealerState",
            "vehicleModel", "vehicleDispatchDate"
        ])

        for _ in range(num_records):
            writer.writerow([
                generate_random_uin(),
                generate_random_vin(),
                generate_random_iccid(),
                generate_random_imei(),
                card_status,
                device_model,
                random_date_between(bootstrap_start, bootstrap_end),
                dealer_state,
                vehicle_model,
                random_date_between(dispatch_start, dispatch_end)
            ])

    print(f"✅ SIM batch ({tech}) with {num_records} records written to: {output_file}")
    return output_file