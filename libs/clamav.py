#!/usr/bin/python3.10


################################################################################
#                                                                              #
#                                                                              #
#                   GNU AFFERO GENERAL PUBLIC LICENSE                          #
#                       Version 3, 19 November 2007                            #
#                                                                              #
#    This library is a wrapper for the ClamAV CLI Software.                    #
#    Copyright (C) 2022 Gavroche, Roxane                                       #
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


def analyze(path):

    c = None

    # Defender CLI tool path
    clamav_cli = """ "C:\\Program Files (x86)\\ClamAV\\clamscan.exe" """

    # Run analysis
    with spinner(f'Analyzing {path}'):
        cmd = subprocess.run(f"""cmd /c {clamav_cli} {path}""", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # If file is not flagged as malicious
    if cmd.returncode == 0:
        success('File was declared safe by ClamAV')
        c = True

    # If file is flagged as malicious
    if cmd.returncode == 1:
        warning('File was flagged as malicious by ClamAV')
        c = False

    return c


################################################################################


if __name__ == "__main__":
    print('Please run main.py or read software documentation')

    exit()
