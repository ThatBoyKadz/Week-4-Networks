import os
import hashlib
import csv
from datetime import datetime

def sha256_for_file(path, chunk_size=8192):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            h.update(data)
    return h.hexdigest()

folder = "myfiles"
output_csv = "hashes.csv"

with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Filename", "SHA256", "Timestamp"])

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):
            hash_value = sha256_for_file(filepath)
            timestamp = datetime.now().isoformat()

            writer.writerow([filename, hash_value, timestamp])
            print(f"Hashed: {filename}")

print("Done! Hashes saved to hashes.csv")
