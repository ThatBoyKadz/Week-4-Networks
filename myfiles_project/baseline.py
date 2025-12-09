import os
import hashlib
import csv

def sha256_for_file(path, chunk_size=8192):
    """Return the SHA256 hash of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

folder = "myfiles"          # Folder to monitor
baseline_file = "baseline.csv"  # CSV to save trusted hashes

with open(baseline_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Filename", "SHA256"])  # CSV header

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            hash_value = sha256_for_file(path)
            writer.writerow([filename, hash_value])
            print(f"Recorded baseline: {filename}")

print(f"Trusted baseline saved to {baseline_file}")
