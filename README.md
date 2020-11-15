#### **Pysces Ransomware**

A simple ransomware virus implemented in python, which encrypts files in a target system
and opens up a window with a ransom message.

install requirements.txt:

`pip install requirements.txt`


#### **Disclaimer:**

This software is for educational purposes ONLY. The author doesnt take
responsibility for any illegal use of this software.

#### **Features:**

1. Works without internet during local file encryption.

2. Hides console and runs in background to prevent suspicion by victim.

3. Searches for files recursively and encrypts them.

4. Creates and opens a ransom note as well as a window showing the ransom demands after encrypting.

5. Deletes itself (ransomware) after infecting the system and delivering the ransom message and note.
This is to avoid the malware being recovered by malware analysts for dissection.

6. Scans for hosts on LAN and tries to connect via FTP port and brute forces it's password.
If successful, it encrypts all files on the network.

7. Infects certain file extensions and makes them executable, which when opened
will spread to other uninfected files on other systems and execute its payload.
It also cannot infect an already infected file.

Thank you.