import os

def analyze(path):

    c = None

    # Defender CLI tool path
    clamav_cli = """ "C:\\Program Files (x86)\\ClamAV\\clamscan.exe" """

    # Run analysis
    cmd = os.system(f"""cmd /c {clamav_cli} {path}""")

    # If file is not flagged as malicious
    if cmd == 0:
        c = True

    # If file is flagged as malicious
    if cmd == 1:
        c = False

    return c
