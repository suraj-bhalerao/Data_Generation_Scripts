import pandas as pd
import random
from datetime import datetime, timedelta
import os

# 2G and 4G device models
DEVICE_MODELS = {
    "2G": "ACONITS140I",
    "4G": "AEPL051400"
}

def generate_random_imei():
    return ''.join(str(random.randint(0, 9)) for _ in range(15))

def generate_random_engine_no():
    return 'B6.7B6A250D02102' + ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))

def generate_random_reg_number():
    return random.choice(['MH', 'TN', 'RJ', 'KA', 'DL']) + str(random.randint(10, 99)) + \
           ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + str(random.randint(1000, 9999))

def generate_random_mobile_number():
    return int('9' + ''.join(str(random.randint(0, 9)) for _ in range(9)))

def generate_institutional_sales(device_type="4G", number_of_records=10, output_dir=None):
    if device_type not in DEVICE_MODELS:
        raise ValueError("Invalid device type. Must be '2G' or '4G'.")

    if output_dir is None:
        output_dir = os.getcwd()
    os.makedirs(output_dir, exist_ok=True)

    base_vin = "SURAJ30072025"
    device_model = DEVICE_MODELS[device_type]
    device_make = "Accolade"
    uin_no = "ACON4CA032100000069"
    start_date = datetime.today()
    expiry_date = start_date + timedelta(days=730)

    iccid_list = [f"8991{str(100000000000000 + i)}" for i in range(number_of_records)]

    records = []

    for i in range(number_of_records):
        rto_office_code, rto_state = random.choice([
            ("MH 12", "MH"), ("TN 5", "TN"), ("RJ 14", "RJ"), ("KA 03", "KA"), ("DL 01", "DL")
        ])

        record = {
            "VIN_NO": f"{base_vin}_{i + 1}",
            "ICCID": iccid_list[i],
            "UIN_NO": uin_no,
            "DEVICE_IMEI": generate_random_imei(),
            "DEVICE_MAKE": device_make,
            "DEVICE_MODEL": device_model,
            "ENGINE_NO": generate_random_engine_no(),
            "REG_NUMBER": generate_random_reg_number(),
            "VEHICLE_OWNER_FIRST_NAME": "SBSB",
            "VEHICLE_OWNER_MIDDLE_NAME": "S",
            "VEHICLE_OWNER_LAST_NAME": "BHALERAO",
            "ADDRESS_LINE_1": "SHIVANE",
            "ADDRESS_LINE_2": "SHIVANE",
            "VEHICLE_OWNER_CITY": "PUNE",
            "VEHICLE_OWNER_DISTRICT": "PUNE",
            "VEHICLE_OWNER_STATE": "MAHARASHTRA",
            "VEHICLE_OWNER_COUNTRY": "INDIA",
            "VEHICLE_OWNER_PINCODE": 411045,
            "VEHICLE_OWNER_REGISTERED_MOBILE": generate_random_mobile_number(),
            "POS_CODE": "AB123",
            "POA_DOC_NAME": "PANAB123",
            "POA_DOC_NO": "PAN1AB123",
            "POI_DOC_TYPE": "ADHARAB123",
            "POI_DOC_NO": "ADHARXYZ123",
            "RTO_OFFICE_CODE": rto_office_code,
            "RTO_STATE": rto_state,
            "PRIMARY_OPERATOR": random.choice(["BSNL", "Airtel", "Jio"]),
            "SECONDARY_OPERATOR": random.choice(["BHA", "Vodafone"]),
            "PRIMARY_MOBILE_NUMBER": generate_random_mobile_number(),
            "SECONDARY_MOBILE_NUMBER": generate_random_mobile_number(),
            "VEHICLE_MODEL": random.choice(["NANO", "Sedan", "SUV", "Electric", "Truck"]),
            "DEALER_CODE": random.randint(1000, 9999),
            "COMMERCIAL_ACTIVATION_START_DATE": start_date.strftime('%Y-%m-%d'),
            "COMMERCIAL_ACTIVATION_EXPIRY_DATE": expiry_date.strftime('%Y-%m-%d'),
            "MFG_YEAR": random.choice([2022, 2023, 2024]),
            "ACCOLADE_POSTING_DATE_TIME": start_date.strftime('%Y-%m-%d'),
            "INVOICE_DATE": start_date.strftime('%Y-%m-%d'),
            "INVOICE_NUMBER": f"AEPL{random.randint(100000000, 999999999)}",
            "CERTIFICATE_VALIDITY_DURATION_IN_YEAR": 3
        }

        records.append(record)

    df = pd.DataFrame(records)
    file_name = f"Institutional_Sales_{device_type}_{datetime.today().strftime('%Y%m%d')}.xlsx"
    output_path = os.path.join(output_dir, file_name)
    df.to_excel(output_path, index=False)

    print(f"✅ Institutional Sales file generated: {output_path}")
