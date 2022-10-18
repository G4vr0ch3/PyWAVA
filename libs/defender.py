#!/usr/bin/python3.10


################################################################################
#                                                                              #
#                                                                              #
#                   GNU AFFERO GENERAL PUBLIC LICENSE                          #
#                       Version 3, 19 November 2007                            #
#                                                                              #
#    This library is a wrapper for the Microsoft Windows Defender CLI Software.#
#    Copyright (C) 2022 Gavroche                                               #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
#    it under the terms of the GNU Affero General Public License as published  #
#    by the Free Software Foundation, either version 3 of the License, or      #
#    (at your option) any later version.                                       #
#                                                                              #
#     This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU Affero General Public License for more details.                       #
#                                                                              #
#    You should have received a copy of the GNU Affero General Public License  #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.    #
#                                                                              #
#                                                                              #
################################################################################


import subprocess
from Asterix_libs.spinner import spinner
from Asterix_libs.prints import *


################################################################################


def analyze(path, rem="-DisableRemediation"):

    c = None

    # Defender CLI tool path
    defender_cli = """ "C:\\Program Files\\Windows Defender\\MpCmdRun.exe" """

    # File and directory custom scan
    ScanType = 3

    # Disable defender file treatment on file by default
    Remediation = rem

    # Run analysis
    with spinner(f'Analyzing {path}'):
        cmd = subprocess.run(f'cmd /c {defender_cli} -Scan -ScanType {ScanType} {Remediation} -File "{path}"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # If the file is not flagged as malicious
    if cmd.returncode == 0:
        success('File was declared safe by Microoft Windows Defender')
        c = True

    # If the file is flagged as malicious
    if cmd.returncode == 2:
        warning('File was flagged as malicious by Microsoft Windows Defender')
        c = False

    return c


################################################################################


if __name__ == "__main__":
    print('Please run main.py or read software documentation')

    exit()
