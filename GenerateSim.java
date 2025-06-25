import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class GenerateSim {
    private static final int NUMBER_OF_RECORDS = 10;
    private static final String CSV_FILE = "Card_details_sb_aft_1.csv";
    private static final Random RANDOM = new Random();
    private static final DateTimeFormatter DATE_FORMATTER = DateTimeFormatter.ofPattern("dd-MMM-yy");

    private static String generateChassisNo() {
        return "AFT" + getRandomAlphaNumeric(14);
    }

    private static String generateICCID() {
        return "8991" + getRandomNumeric(16);
    }

    private static String generateIMEI() {
        return getRandomNumeric(15);
    }

    private static String generateSerialNo() {
        return "ACON4IA" + getRandomNumeric(10);
    }

    private static String generateEngineNo() {
        return "B6.7B6A250D02102" + getRandomAlphaNumeric(10);
    }

    private static String generateRegNumber() {
        String[] states = {"MH", "TN", "RJ", "KA", "DL"};
        return states[RANDOM.nextInt(states.length)] + RANDOM.nextInt(90) + getRandomAlpha(2) + RANDOM.nextInt(9000);
    }

    private static String generateDealerName() {
        String[] dealers = {
                "1001860-Sales-Chennai-PopMeg",
                "1003530-Sales-Nerul-KAMAL",
                "1001140-Sales-Hanumangarh-DunacA"
        };
        return dealers[RANDOM.nextInt(dealers.length)];
    }

    private static String[] generateRTO() {
        String[][] rtoData = {
                {"TN", "TN 5"},
                {"MH", "MH 12"},
                {"RJ", "RJ 14"},
                {"KA", "KA 03"},
                {"DL", "DL 01"}
        };
        return rtoData[RANDOM.nextInt(rtoData.length)];
    }

    private static String generateMobileNumber() {
        return "9" + getRandomNumeric(9);
    }

    private static String generateRandomDate(int startYear, int endYear) {
        int dayOfYear = RANDOM.nextInt(365);
        int year = startYear + RANDOM.nextInt(endYear - startYear + 1);
        return LocalDate.ofYearDay(year, dayOfYear).format(DATE_FORMATTER);
    }

    private static String generateVehicleModel() {
        String[] manufacturers = {"HONDA", "SUZUKI", "TATA", "HYUNDAI", "FORD", "TOYOTA", "MAHINDRA", "BMW", "MERCEDES", "KIA"};
        String[] models = {"Sedan", "SUV", "Hatchback", "Truck", "Electric", "Hybrid"};
        return manufacturers[RANDOM.nextInt(manufacturers.length)] + " " + models[RANDOM.nextInt(models.length)];
    }

    private static String getRandomAlphaNumeric(int length) {
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            sb.append(chars.charAt(RANDOM.nextInt(chars.length())));
        }
        return sb.toString();
    }

    private static String getRandomAlpha(int length) {
        String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            sb.append(chars.charAt(RANDOM.nextInt(chars.length())));
        }
        return sb.toString();
    }

    private static String getRandomNumeric(int length) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            sb.append(RANDOM.nextInt(10));
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String[] headers = {
                "CHASSIS_NO", "ICCID", "IMEI", "SERIAL_NO", "DEVICE_MAKE", "DEVICE_MODEL",
                "ENGINE_NO", "REG_NUMBER", "DEALER_NAME", "DEALER_CODE", "RTO_OFFICE_CODE",
                "RTO_STATE", "PRIMARY_OPERATOR", "PRIMARY_MOBILE_NUMBER", "SECONDARY_OPERATOR",
                "SECONDARY_MOBILE_NUMBER", "VEHICLE_MODEL", "SIM_STATUS", "ACTIVATION_STATUS",
                "ACTIVATION_STATUS_DATE", "ACTIVATION_EXPIRY", "VAHAN_UPLOAD_STATUS"
        };

        String[] primaryOperators = {"BHA", "Airtel", "Jio"};
        String[] secondaryOperators = {"BSNL", "Vodafone"};
        String[] simStatusOptions = {"Active", "Inactive"};
        String[] activationStatusOptions = {"Commercial", "Pending"};
        String[] vahanUploadStatusOptions = {"SUCCESS", "FAILED"};

        int startYear = LocalDate.now().getYear() - 5;
        int endYear = LocalDate.now().getYear() + 5;

        try (FileWriter writer = new FileWriter(CSV_FILE)) {
            // Write headers
            writer.append(String.join(",", headers)).append("\n");

            for (int i = 0; i < NUMBER_OF_RECORDS; i++) {
                String chassisNo = generateChassisNo();
                String iccid = generateICCID();
                String imei = generateIMEI();
                String serialNo = generateSerialNo();
                String engineNo = generateEngineNo();
                String regNumber = generateRegNumber();
                String dealerName = generateDealerName();
                String dealerCode = dealerName.split("-")[0];
                String[] rtoData = generateRTO();
                String rtoOfficeCode = rtoData[1];
                String rtoState = rtoData[0];
                String primaryOperator = primaryOperators[RANDOM.nextInt(primaryOperators.length)];
                String primaryMobileNumber = generateMobileNumber();
                String secondaryOperator = secondaryOperators[RANDOM.nextInt(secondaryOperators.length)];
                String secondaryMobileNumber = generateMobileNumber();
                String vehicleModel = generateVehicleModel();
                String simStatus = simStatusOptions[RANDOM.nextInt(simStatusOptions.length)];
                String activationStatus = activationStatusOptions[RANDOM.nextInt(activationStatusOptions.length)];
                String activationStatusDate = generateRandomDate(startYear, endYear);
                String activationExpiry = generateRandomDate(startYear, endYear);
                String vahanUploadStatus = vahanUploadStatusOptions[RANDOM.nextInt(vahanUploadStatusOptions.length)];

                writer.append(String.join(",", chassisNo, iccid, imei, serialNo, "ACCOLADE", "ACONITS140I", engineNo,
                        regNumber, dealerName, dealerCode, rtoOfficeCode, rtoState, primaryOperator, primaryMobileNumber,
                        secondaryOperator, secondaryMobileNumber, vehicleModel, simStatus, activationStatus,
                        activationStatusDate, activationExpiry, vahanUploadStatus)).append("\n");
            }

            System.out.println(NUMBER_OF_RECORDS + " records have been written to " + CSV_FILE);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
