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


import os


################################################################################


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


################################################################################


if __name__ == "__main__":
    print('Please run main.py or read software documentation')

    exit()
