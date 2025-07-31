import json
import random
from datetime import datetime

# Device model mapping
DEVICE_MODEL_MAP = {
    "2G": "AEPL051300",
    "4G": "AEPL051400"
}

# Static data provided
ICCID_VALUES = [
    "89916420534724548021", "89916420534724548022", "89916420534724548023",
    "89916420534724548024", "89916420534724548025", "89916420534724548026",
    "89916420534724548027", "89916420534724548028", "89916420534724548029",
    "89916420534724548030", "89916420534724548031", "89916420534724548032",
    "89916420534724548033", "89916420534724548034", "89916420534724548035",
    "89916420534724548036", "89916420534724548037", "89916420534724548038",
    "89916420534724548039", "89916420534724548040", "89916420534724548041"
]
UIN_VALUES = ["ACON4NA202200082103"] * 20
VIN_VALUES = ["ACCDEV20222576271"] * 20
IMEI_VALUES = ["868274067382103"] * 20  # fixed as provided

# RTO pools (state code -> list of office codes)
RTO_MAP = {
    "MH": ["MH 12", "MH 14", "MH 01"],
    "TN": ["TN 05", "TN 07"],
    "RJ": ["RJ 14", "RJ 01"],
    "KA": ["KA 03", "KA 05"],
    "DL": ["DL 01", "DL 02"],
    "KL": ["KL 14", "KL 07"],
    "GJ": ["GJ 01", "GJ 05"]
}

# Helper generators
def _pick_rto():
    state = random.choice(list(RTO_MAP.keys()))
    office = random.choice(RTO_MAP[state])
    return office, state

def _generate_random_reg_number():
    return random.choice(['MH', 'TN', 'RJ', 'KA', 'DL']) + str(random.randint(10, 99)) + \
        ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + str(random.randint(1000, 9999))

def generate_json_data(device_type: str, num_records: int):
    tech = device_type.upper()
    if tech not in DEVICE_MODEL_MAP:
        raise ValueError("Invalid device type; must be '2G' or '4G'.")

    device_model = DEVICE_MODEL_MAP[tech]
    device_make = "ACCOLADE"

    if num_records > len(ICCID_VALUES):
        print(f"⚠️ Requested {num_records} records but only {len(ICCID_VALUES)} unique ICCIDs/VINs/etc.; some will repeat.")

    base_data_template = {
        "VIN_NO": "",
        "ICCID": "",
        "UIN_NO": "",
        "DEVICE_IMEI": "",
        "DEVICE_MAKE": device_make,
        "DEVICE_MODEL": device_model,
        "ENGINE_NO": "ENGINE_SR_N_30032103",
        "REG_NUMBER": "",
        "REGISTERED_MOBILE_NUMBER": "7385862781",
        "VEHICLE_OWNER_FIRST_NAME": "",
        "VEHICLE_OWNER_MIDDLE_NAME": "",
        "VEHICLE_OWNER_LAST_NAME": "LastName",
        "ADDRESS_LINE_1": "Sample Address Line 1",
        "ADDRESS_LINE_2": "Sample Address Line 2",
        "VEHICLE_OWNER_CITY": "City",
        "VEHICLE_OWNER_DISTRICT": "District",
        "VEHICLE_OWNER_STATE": "Kerala",
        "VEHICLE_OWNER_COUNTRY": "India",
        "VEHICLE_OWNER_PINCODE": "123456",
        "VEHICLE_OWNER_REGISTERED_MOBILE": "7385862781",
        "POS_CODE": "AB123",
        "POA_DOC_NAME": "POA123",
        "POA_DOC_NO": "POA1234",
        "POI_DOC_TYPE": "ADHAR123",
        "POI_DOC_NO": "ADHAR1234",
        "RTO_OFFICE_CODE": "",
        "RTO_STATE": "",
        "PRIMARY_OPERATOR": "AIRTEL",
        "SECONDARY_OPERATOR": "BSNL",
        "PRIMARY_MOBILE_NUMBER": "8765284847",
        "SECONDARY_MOBILE_NUMBER": "7992635726",
        "VEHICLE_MODEL": "Bugatti",
        "DEALER_CODE": "1133",
        "COMMERCIAL_ACTIVATION_START_DATE": "2024-10-04",
        "COMMERCIAL_ACTIVATION_EXPIRY_DATE": "2027-10-05",
        "MFG_YEAR": "2024",
        "ACCOLADE_POSTING_DATE_TIME": "2024-10-04",
        "INVOICE_DATE": "2024-10-04",
        "INVOICE_NUMBER": "AEPL18012024-01",
        "CERTIFICATE_VALIDITY_DURATION_IN_YEAR": 2
    }

    vehicles = []
    for i in range(num_records):
        vehicle = base_data_template.copy()

        # cycle through provided lists if needed
        vehicle["VIN_NO"] = VIN_VALUES[i % len(VIN_VALUES)]
        vehicle["ICCID"] = ICCID_VALUES[i % len(ICCID_VALUES)]
        vehicle["UIN_NO"] = UIN_VALUES[i % len(UIN_VALUES)]
        vehicle["DEVICE_IMEI"] = IMEI_VALUES[i % len(IMEI_VALUES)]
        vehicle["VEHICLE_OWNER_FIRST_NAME"] = f"Owner_{i+1}"
        vehicle["REG_NUMBER"] = _generate_random_reg_number()

        # dynamic RTO
        rto_office, rto_state = _pick_rto()
        vehicle["RTO_OFFICE_CODE"] = rto_office
        vehicle["RTO_STATE"] = rto_state

        # Optional: vary OWNER LOCATION based on RTO state (simple mapping)
        if rto_state == "MH":
            vehicle["VEHICLE_OWNER_STATE"] = "Maharashtra"
        elif rto_state == "TN":
            vehicle["VEHICLE_OWNER_STATE"] = "Tamil Nadu"
        elif rto_state == "RJ":
            vehicle["VEHICLE_OWNER_STATE"] = "Rajasthan"
        elif rto_state == "KA":
            vehicle["VEHICLE_OWNER_STATE"] = "Karnataka"
        elif rto_state == "DL":
            vehicle["VEHICLE_OWNER_STATE"] = "Delhi"
        elif rto_state == "KL":
            vehicle["VEHICLE_OWNER_STATE"] = "Kerala"
        elif rto_state == "GJ":
            vehicle["VEHICLE_OWNER_STATE"] = "Gujarat"

        # Validations
        if not vehicle["REG_NUMBER"]:
            raise ValueError("REG_NUMBER cannot be blank.")
        if not vehicle["VEHICLE_OWNER_REGISTERED_MOBILE"]:
            raise ValueError("Vehicle owner's registered mobile is required.")

        vehicles.append(vehicle)

    # Write to JSON file
    date_str = datetime.today().strftime("%Y%m%d")
    output_name = f"vehicle_data_{tech}_{date_str}.json"
    with open(output_name, "w") as f:
        json.dump(vehicles, f, indent=4)

    print(f"✅ Generated {len(vehicles)} records for {tech} saved to '{output_name}'")
    return vehicles
