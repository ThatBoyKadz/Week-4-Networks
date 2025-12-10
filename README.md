# File Integrity Monitoring and Network Security Portfolio

This portfolio documents a set of Python scripts designed to implement file integrity monitoring, detect file changes, hash files with timestamps, simulate network propagation, and perform signature-based malware scanning.

---

## 1. Overview

The project contains seven scripts and two CSV files to demonstrate various aspects of cybersecurity:

1. **baseline.py** – Creates a trusted baseline of file hashes for a folder.
2. **detect_changes.py** – Compares current files to the baseline and detects changes, deletions, and new files.
3. **hash_files.py** – Hashes files with SHA256 and logs the timestamp for auditing.
4. **network_propagation.py** – Simulates malware or infection propagation through a network.
5. **signature_scanner.py** – Scans files for suspicious patterns using regular expressions.
6. **baseline.csv** – Stores trusted file hashes.
7. **hashes.csv** – Stores hashes with timestamps for reference.

This project demonstrates practical techniques in file integrity monitoring, malware detection, and network security simulation.

---

## 2. File Explanations

### 2.1 baseline.py

**Purpose:** Establish a trusted SHA256 hash baseline for files in a directory.

**Key Features:**

* Computes SHA256 hashes for all files in a folder.
* Writes hashes to `baseline.csv`.
* Useful for detecting unauthorized modifications later.

**Usage:**

```
python baseline.py
```

*(Insert screenshot showing baseline CSV being generated and console output)*

---

### 2.2 detect_changes.py

**Purpose:** Detect modifications, deletions, and new files compared to the trusted baseline.

**Key Features:**

* Loads `baseline.csv` and compares with current files.
* Reports modified, deleted, and new files.
* Provides a clear file integrity report.

**Usage:**

```
python detect_changes.py
```

*(Insert screenshot showing detection of changed, deleted, and new files)*

---

### 2.3 hash_files.py

**Purpose:** Generate SHA256 hashes for all files and log with timestamps.

**Key Features:**

* Records hash along with the timestamp of hashing.
* Output saved to `hashes.csv` for audit purposes.
* Supports large files with chunked reading.

**Usage:**

```
python hash_files.py
```

*(Insert screenshot showing hashes being calculated and saved with timestamps)*

---

### 2.4 network_propagation.py

**Purpose:** Simulate the spread of malware or infection across a network of computers.

**Key Features:**

* Models the network as a graph (nodes = computers, edges = connections).
* Uses a probability factor to simulate infection spread.
* Prints step-by-step propagation until no new infections occur.

**Usage:**

```
python network_propagation.py
```

*(Insert screenshot showing network propagation steps and final infected nodes)*

---

### 2.5 signature_scanner.py

**Purpose:** Scan files for suspicious code patterns.

**Key Features:**

* Uses regular expressions to detect potentially malicious functions (e.g., `eval()`, `exec()`).
* Skips binary files and reads text safely.
* Reports detected signatures per file.

**Usage:**

```
python signature_scanner.py
```

*(Insert screenshot showing scan results for clean and suspicious files)*

---

### 2.6 baseline.csv & hashes.csv

**Purpose:** Serve as reference files for file integrity monitoring.

**Details:**

* `baseline.csv`: Stores filenames and SHA256 hashes for trusted files.
* `hashes.csv`: Stores filenames, SHA256 hashes, and timestamps for auditing.

**Usage:**

* Used by `detect_changes.py` to verify integrity.
* Provides historical hash data for forensic analysis.

*(Insert screenshots showing CSV content in a spreadsheet or console view)*

---

## 3. Workflow Demonstration

1. **Create baseline:** Run `baseline.py` to generate trusted hashes.
2. **Detect changes:** Use `detect_changes.py` after modifying or adding files.
3. **Audit hashes:** Optionally run `hash_files.py` to maintain timestamped records.
4. **Network simulation:** Run `network_propagation.py` to study propagation dynamics.
5. **Malware scan:** Run `signature_scanner.py` to identify suspicious patterns.

*(Insert sequential screenshots showing workflow from baseline creation to change detection and scanning)*

---

## 4. Conclusion

This project provides hands-on experience in:

* File integrity monitoring and baseline creation.
* Detecting unauthorized changes to files.
* Hashing with timestamps for auditing purposes.
* Simulating network-based malware propagation.
* Signature-based malware detection.

These scripts are essential for learning foundational concepts in system security, monitoring, and network safety.

---

*(Add all relevant screenshots where indicated to complete the portfolio.)*
