The purpose is to demonstrate competence in areas such as file integrity monitoring, malware detection, hashing, and network propagation simulation. Each section includes an explanation of the practical task, code snippets, and instructions for running the program.

1) baseline.py:

baseline.py script creates a trusted baseline of all files inside a directory by computing SHA-256 hashes. when Python baseline.py is run it will create baseline.csv which is opned in a spreadsheet shown here: 

<img width="681" height="183" alt="image" src="https://github.com/user-attachments/assets/a4d0b9a0-525d-4724-bc0a-a5bc836cd6b6" />

these trusted baselines are used  for integrity checks later.


2) detect_changes.py: 

Once baseline.py has created baseline.cv, detect_changes.py compares current file to the trusted baselines and checks:
--modified files
--deleted files
--newly added files
checking for any tampering 

This is important to help uncover, malware injections, insider modification and web defacement


Detecting modified files: 
<img width="325" height="41" alt="image" src="https://github.com/user-attachments/assets/25a6666b-5566-4863-aa07-6c05db4425fd" />


Detecting Deleted or new Files:
<img width="272" height="49" alt="image" src="https://github.com/user-attachments/assets/ff6694e1-6f0c-4c00-bc13-ad4350e8dc29" />



3) Hash_files.py: 

Purpose of this file being run is also very imporant, because it hashes all of the files and logs them with a timestamp.
As you can see from this screenshot below after the code had been implemented in terminal:

<img width="860" height="109" alt="image" src="https://github.com/user-attachments/assets/2bdd7bcf-8185-47bc-854e-aa97ed402f96" />

In cybersecurity relevance, this can be used for evidence logging, malware analysis and trackingg changes over time.


4) network_propagation.py:

network_propagation.py simulates how malware spreads across a network usng probability based infection demonstrating:
--lateral movement
--Worm propagation
--Risk of interconnected systems



5) Signature_scanner.py:

signature_scanner.py scans files in a folder for suspicious patterns that commonly appear in malicious scripts shown below: 

<img width="208" height="114" alt="image" src="https://github.com/user-attachments/assets/25b8fa0e-6883-4efd-a24d-c7c592008022" />

signature based scanning is used by classic antivirus engines, email gateways and static malware analysis tools

   
