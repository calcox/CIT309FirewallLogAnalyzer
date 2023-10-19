import argparse
import csv
from datetime import datetime, timezone, timedelta
from log_analyzer import LogEntry

def convert_to_us_style_date(event_time):
    #est timezone
    event_time = event_time.astimezone(timezone(timedelta(hours=-5)))
    return event_time.strftime("%m/%d/%Y %H:%M %Z")

def main():
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("--filename", required=True, help="firewall_logs_sample.csv")

    args = parser.parse_args()
    filename = args.filename

    log_entries = []

    #read csv file
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            log_entry = LogEntry()
            log_entry.event_time = datetime.strptime(row["event_time"], "%Y-%m-%d %H:%M:%S %Z")
            log_entry.internal_ip = row["internal_ip"]
            log_entry.port_number = int(row["port_number"])
            log_entry.protocol = row["protocol"]
            log_entry.action = row["action"]
            log_entry.rule_id = int(row["rule_id"])
            log_entry.source_ip = row["source_ip"]
            log_entry.country = row["country"]
            log_entry.country_name = row["country_name"]

            log_entries.append(log_entry)

    #loop through first 5
    for entry in log_entries[:5]:
        print("Date of the log entry:", convert_to_us_style_date(entry.event_time))
        print("Action:", entry.action)
        print("Source IP:", entry.source_ip)
        print("IPv4 Class:", entry.ipv4_class)
        print("Country Name:", entry.country_name)
        print("\n")

if __name__ == "__main__":
    main()
