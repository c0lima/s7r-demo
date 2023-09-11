import json
import random
from faker import Faker
import time
import os


fake = Faker()

home = os.path.expanduser("~")
log_file_path = os.path.join(home, "app_logs.json")

def generate_log():
    log_entry = {
        "user": fake.user_name(),
        "fee": round(random.uniform(1.0, 50.0), 2),
        "address": fake.address().replace("\n", ", "),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    }
    return log_entry

if __name__ == "__main__":
    while True:
        with open(log_file_path, "a") as f:
            log_entry = generate_log()
            f.write(json.dumps(log_entry) + "\n")
        time.sleep(2)  # Generar un nuevo log cada 2 segundos

