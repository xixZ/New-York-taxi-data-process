import csv
import datetime


def convert_date_time(csv_date_time):
    d = datetime.datetime.strptime(csv_date_time, '%Y-%m-%d %H:%M:%S')
    return d.strftime('%Y-%m-%dT%H:%M:%S')

fo = open("taxi.adm", "wb")

with open('/media/sony/16B87538B8751787/yellow_tripdata_2015-01.csv', 'rb') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        count += 1
        try:
            newline = "{"
            newline += "\"vendor_id\": int8(\"" + row['VendorID'] + "\"), "
            newline += "\"pickup_datetime\": datetime(\"" + convert_date_time(row['tpep_pickup_datetime']) + "\"), "
            newline += "\"dropoff_datetime\": datetime(\"" + convert_date_time(row['tpep_dropoff_datetime']) + "\"), "
            newline += "\"passenger_count\": int8(\"" + row['passenger_count'] + "\"), "
            newline += "\"trip_distance\": " + str(float(row['trip_distance'])) + "f, "
            newline += "\"pickup_location\": point(\"" + row['pickup_latitude'] + "," + row['pickup_longitude'] + "\"),"
            newline += "\"ratecode_id\": int8(\"" + row['RateCodeID'] + "\"), "
            newline += "\"store_and_fwd_flag\": \"" + row['store_and_fwd_flag'] + "\","
            newline += "\"dropoff_location\": point(\"" + row['dropoff_latitude'] + "," + row['dropoff_longitude'] + "\"),"
            newline += "\"payment_type\": int8(\"" + row['payment_type'] + "\"), "
            newline += "\"fare_amount\": " + str(float(row['fare_amount'])) + "f, "
            newline += "\"extra\": " + str(float(row['extra'])) + "f, "
            newline += "\"mta_tax\": " + str(float(row['mta_tax'])) + "f, "
            newline += "\"tip_amount\": " + str(float(row['tip_amount'])) + "f, "
            newline += "\"tolls_amount\": " + str(float(row['tolls_amount'])) + "f, "
            newline += "\"improvement_surcharge\": " + str(float(row['improvement_surcharge'])) + "f, "
            newline += "\"total_amount\": " + str(float(row['total_amount'])) + "f"
            newline += "}\n"
            fo.write(newline)
        except ValueError:
            print count
        if count % 1000000 == 0:
            print count
    print count
fo.close()
