import psutil
import time
import csv
from datetime import datetime

# CSV file name
FILE_NAME = "pc_usage_log.csv"

# Create CSV file and header if not exists
try:
    with open(FILE_NAME, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Date",
            "Time",
            "RAM Used (GB)",
            "RAM Total (GB)",
            "Disk Used (GB)",
            "Disk Total (GB)"
        ])
except FileExistsError:
    pass

print("PC Usage Tracker Started... Press CTRL+C to stop")

while True:
    # Time
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    # RAM info
    ram = psutil.virtual_memory()
    ram_used = round((ram.total - ram.available) / (1024 ** 3), 2)
    ram_total = round(ram.total / (1024 ** 3), 2)

    # Disk info
    disk = psutil.disk_usage('/')
    disk_used = round(disk.used / (1024 ** 3), 2)
    disk_total = round(disk.total / (1024 ** 3), 2)

    # Save to CSV
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            date,
            time_now,
            ram_used,
            ram_total,
            disk_used,
            disk_total
        ])

    # Wait 5 minutes (300 seconds)
    time.sleep(300)
