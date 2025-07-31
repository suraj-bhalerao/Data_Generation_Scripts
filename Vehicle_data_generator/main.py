from institutional_sales import generate_institutional_sales
from sim_batch_gen import generate_sim_batch_csv
from ticketing_tool_json_gen import generate_json_data
from fota_batch_gen_4g import generate_fota_batch_csv

def main():
    print("\n--- Vehicle Data Generator ---")
    print("1. Generate Random Excel Vehicle Data")
    print("2. Generate Sim Batch Details for (2G/4G)")
    print("3. Generate Ticketing tool JSON for (2G/4G)")
    print("4. Generate FOTA Batch CSV Data (4G)")
    print("5. Generate Institutional Sales Data (2G/4G)")
    choice = input("Enter your choice : ")

    if choice == '1':
        generate_excel_random()
    elif choice == '2':
        device_type = input("Enter device type : ") or "4G"
        number_of_records = int(input("Enter number of records (default: 10): ") or 10)
        generate_sim_batch_csv(device_type, number_of_records)
    elif choice == '3':
        device_type = input("Enter device type : ") or "4G"
        number_of_records = int(input("Enter number of records (default: 2): ") or 2)
        generate_json_data(device_type, number_of_records)
    elif choice == '4':
        output_file = input("Enter output file name for FOTA batch (default: fota_batch.csv): ") or "fota_batch.csv"
        record_count = int(input("Enter number of records for FOTA batch (default: 20): ") or 20)
        generate_fota_batch_csv(output_file, record_count)
    elif choice == '5':
        device_type = input("Enter device type (2G/4G, default: 4G): ") or "4G"
        number_of_records = int(input("Enter number of records (default: 10): ") or 10)
        output_dir = input("Enter output directory (leave blank for current): ") or None
        generate_institutional_sales(device_type, number_of_records, output_dir)
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
