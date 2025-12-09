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

folder = "myfiles"
baseline_file = "baseline.csv"

# Step 1: Load trusted baseline
trusted_hashes = {}
with open(baseline_file, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        trusted_hashes[row["Filename"]] = row["SHA256"]

# Step 2: Scan current files
current_hashes = {}
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
        current_hashes[filename] = sha256_for_file(path)

# Step 3: Detect changes
modified = []
deleted = []
new_files = []

# Check for modified or deleted files
for filename, hash_val in trusted_hashes.items():
    if filename in current_hashes:
        if current_hashes[filename] != hash_val:
            modified.append(filename)
    else:
        deleted.append(filename)

# Check for new files
for filename in current_hashes:
    if filename not in trusted_hashes:
        new_files.append(filename)

# Step 4: Report
print("\n=== File Integrity Report ===")
if modified:
    print("Modified files:", modified)
else:
    print("No modified files detected.")

if deleted:
    print("Deleted files:", deleted)
else:
    print("No deleted files detected.")

if new_files:
    print("New files detected:", new_files)
else:
    print("No new files detected.")
