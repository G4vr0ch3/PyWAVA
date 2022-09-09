#!/usr/bin/python3.10


################################################################################
#                                                                              #
#                                                                              #
#                   GNU AFFERO GENERAL PUBLIC LICENSE                          #
#                       Version 3, 19 November 2007                            #
#                                                                              #
#    This programms aims at runing anti-virus analysis.                        #
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


import argparse
import json

from pyfiglet import figlet_format as pff

from libs import defender, kaspersky
from datetime import datetime
from libs.prints import *


################################################################################


def tests():
    kaspersky.analyze("D:\\PFE\\stoa.docx")


################################################################################


def analyze(path):

    info(f'Analysing {path}')

    try:
        defender_analysis = defender.analyze(path)
        kaspersky_analysis = kaspersky.analyze(path)
    except:
        fail('Analysis failed')
        return False


    analysis = [defender_analysis, kaspersky_analysis]

    state = analysis.count(False)

    if state == 0 and None not in analysis :
        success('Done. No was threat detected.')
    elif None in analysis:
        print('')
    elif state > 0:
        warning(f'Done. File was flaged as malicious by {state}/{len(analysis)} AV Solution vendors')

    return analysis


################################################################################


if __name__ == '__main__':

    # Software definition
    print(pff("PyAAVA"))

    # Argument parser creation
    parser = argparse.ArgumentParser(description='PYthon Wrapper for Anti-Virus Analysis. Copyright (C) 2022 Gavroche, Roxane.')

    parser.add_argument('--test', help="Run software test", action="store_true")
    parser.add_argument('-f', metavar='file', type=str, help="Target file path")
    parser.add_argument('-r', help="Source file removal flag", action="store_true")

    args=parser.parse_args()

    if args.test: tests(); exit()

    # Retrieve file path and type
    f_path = args.f

    if f_path is None: fail('No file path specified'); exit()

    analyze(f_path)
