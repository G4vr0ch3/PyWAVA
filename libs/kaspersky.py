import os

def analyze(path, rem="i0"):

    c = None

    # Kasperski CLI tool path
    kasperski_cli = """ "C:\\Program Files (x86)\\Kaspersky Lab\\Kaspersky Anti-Virus 21.3\\avp.com" """

    # Disable Kaspersky file treatment on infected file by default
    Remediation = rem

    # Run analysis
    cmd = os.system(f"""cmd /c {kasperski_cli} SCAN /{Remediation} {path}""")

    if cmd == 0:
        c = True

    if cmd == 3 or cmd == 2 :
        c = False

    return c
