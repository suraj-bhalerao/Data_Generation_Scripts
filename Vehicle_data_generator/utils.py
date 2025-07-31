import random

def generate_random_imei():
    return ''.join(str(random.randint(0, 9)) for _ in range(15))

def generate_random_engine_no():
    return 'B6.7B6A250D02102' + ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))

def generate_random_reg_number():
    return random.choice(['MH', 'TN', 'RJ', 'KA', 'DL']) + str(random.randint(10, 99)) + \
           ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2)) + str(random.randint(1000, 9999))

def generate_random_mobile_number():
    return int('9' + ''.join(str(random.randint(0, 9)) for _ in range(9)))