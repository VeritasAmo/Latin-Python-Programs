#!/usr/bin/env python3
"""print out the list of week days in Latin"""

def main():
    eng = str(input("Quid dies hodie in Anglico? "))
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    gods = ['dies lunae', 'dies Martis', 'dies Mercurii', 'dies Iovis', 'dies Veneris', 'dies Saturni', 'dies solis']

    for god in gods:
        if gods.index(god) == days.index(eng):
            print ("Hodie %s est." % god)

main()
