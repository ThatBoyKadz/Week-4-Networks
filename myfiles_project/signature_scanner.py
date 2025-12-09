import os
import re

# Suspicious signatures (simple regex patterns)
SIGNATURES = [
    r"eval\(",
    r"exec\(",
    r"base64\.b64decode",
    r"socket\.connect",
]

FOLDER_TO_SCAN = "myfiles"   # change if needed

def scan_file(filepath):
    """Reads file as text and checks for suspicious patterns."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except:
        # Probably a binary file → skip
        return []

    found = []
    for sig in SIGNATURES:
        if re.search(sig, content):
            found.append(sig)

    return found


print("\n=== Signature-Based Malware Scan ===\n")

for filename in os.listdir(FOLDER_TO_SCAN):
    path = os.path.join(FOLDER_TO_SCAN, filename)

    if os.path.isfile(path):
        matches = scan_file(path)

        if matches:
            print(f"⚠ Suspicious content found in {filename}:")
            for m in matches:
                print(f"   → matches signature: {m}")
        else:
            print(f"✓ {filename}: clean (no signatures detected).")

print("\nScan complete.")
