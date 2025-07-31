import json

def generate_vehicle_data():
    base_data = {
        "VIN_NO": "",  
        "ICCID": "", 
        "UIN_NO": "",  
        "DEVICE_IMEI": "",  
        "DEVICE_MAKE": "ACCOLADE",
        "DEVICE_MODEL": "AEPL051401",
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
        "RTO_OFFICE_CODE": "KL14",
        "RTO_STATE": "KL",
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
    iccid_values = [
        "89916420534724548021", "89916420534724548022", "89916420534724548023", 
        "89916420534724548024", "89916420534724548025", "89916420534724548026", 
        "89916420534724548027", "89916420534724548028", "89916420534724548029", 
        "89916420534724548030", "89916420534724548031", "89916420534724548032", 
        "89916420534724548033", "89916420534724548034", "89916420534724548035", 
        "89916420534724548036", "89916420534724548037", "89916420534724548038", 
        "89916420534724548039", "89916420534724548040", "89916420534724548041"
    ]
    UIN_NO = [
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103",
        "ACON4NA202200082103"
    ]
    VIN_NO = [
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271",
        "ACCDEV20222576271"
    ]
    IMEI = [
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103",
        "868274067382103"
    ]
    
    for i in range(5):
        vehicle = base_data.copy()
        vehicle.update({
            "VIN_NO": VIN_NO[i],
            "ICCID": iccid_values[i], 
            "UIN_NO": UIN_NO[i],
            "DEVICE_IMEI": IMEI[i],
            "VEHICLE_OWNER_FIRST_NAME": f"Owner_{i+1}",
            "REG_NUMBER": f"MH14FF92{i+4}", 
            # "VEHICLE_OWNER_REGISTERED_MOBILE": f"73858627{i+81}", 
            # "VEHICLE_OWNER_PINCODE": f"4110{i+1:02d}",
            # "INVOICE_NUMBER": f"AEPL18012024-{i+1:02d}"
        })

        if not vehicle["REG_NUMBER"]:
            raise ValueError("Vehicle Registration Number is required and cannot be left blank.")
        
        if not vehicle["VEHICLE_OWNER_REGISTERED_MOBILE"]:
            raise ValueError("Vehicle Owner’s Registered Mobile Number is required and cannot be left blank.")

        vehicles.append(vehicle)

    return vehicles

try:
    vehicle_data = generate_vehicle_data()
    with open("vehicle_data.json", "w") as json_file:
        json.dump(vehicle_data, json_file, indent=4)
    
    print("Vehicle data successfully generated and saved to vehicle_data.json.")
except ValueError as e:
    print(f"Error: {e}")
