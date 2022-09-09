import os

def analyze(path, rem="-DisableRemediation"):

    # Defender CLI tool path
    defender_cli = """ "C:\\Program Files\\Windows Defender\\MpCmdRun.exe" """

    # File and directory custom scan
    ScanType = 3

    # Disable defender file treatment on file by default
    Remediation = rem

    # Run analysis
    cmd = os.system(f"""cmd /c {defender_cli} -Scan -ScanType {ScanType} {Remediation} -File {path}""")

    # If the file is not flagged as malicious
    if cmd == 0:
        c = True

    # If the file is flagged as malicious
    if cmd == 2:
        c = False

    return c
