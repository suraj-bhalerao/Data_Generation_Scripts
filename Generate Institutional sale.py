import pandas as pd
import random
from faker import Faker

fake = Faker()

# Number of rows to generate
num_rows = 10

# Define a function to generate random data based on column types
def generate_data():
    return {
        'VIN_NO': random.randint(1000, 9999),
        'ICCID': fake.unique.numerify('8991642###########'),
        'UIN_NO': fake.unique.bothify('ACON4NA##########'),
        'DEVICE_IMEI': fake.unique.numerify('8615640########'),
        'DEVICE_MAKE': fake.random_element(['ACCOLADE', 'FLEET', 'TRACKPRO']),
        'DEVICE_MODEL': fake.bothify('AEPL######'),
        'ENGINE_NO': fake.bothify('ENGINE_SR_N_#######'),
        'REG_NUMBER': fake.bothify('MH##??####'),
        'REGISTERED_MOBILE_NUMBER': fake.unique.numerify('##########'),
        'VEHICLE_OWNER_FIRST_NAME': fake.first_name(),
        'SECONDARY_MOBILE_NUMBER': fake.unique.numerify('##########'),
        'VEHICLE_MODEL': fake.random_element(['HARRIER', 'SAFARI', 'NEXON', 'TIAGO']),
        'DEALER_CODE': fake.random_int(1000, 9999),
        'COMMERCIAL_ACTIVATION_START_DATE': fake.date_this_decade(),
        'COMMERCIAL_ACTIVATION_EXPIRY_DATE': fake.date_this_decade(),
        'MFG_YEAR': fake.year(),
        'ACCOLADE_POSTING_DATE_TIME': fake.date_this_year(),
        'INVOICE_DATE': fake.date_this_year(),
        'INVOICE_NUMBER': fake.bothify('AEPL######-##'),
        'CERTIFICATE_VALIDITY_DURATION_IN_YEAR': random.randint(1, 5)
    }

# Generate the data
data = [generate_data() for _ in range(num_rows)]
df = pd.DataFrame(data)

# Save the generated data to an Excel file
df.to_excel('Generated_Institutional_Sales.xlsx', index=False)

print('Data generation complete. File saved as Generated_Institutional_Sales.xlsx.')
