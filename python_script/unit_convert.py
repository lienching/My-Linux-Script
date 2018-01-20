#!/usr/bin/python3
import sys

def lbTokg(lb):
    kg = float(lb) * 0.45359237
    return kg

def kgTolb(kg):
    lb = float(kg) * 2.20462262
    return lb

def main():
    method=sys.argv[1]
    result=0.0
    unit=''
    if method == "lbTokg":
        try:
            lb=sys.argv[2]
            result=lbTokg(lb)
            unit='kg'
        except:
            print("python unit_convert.py [method] [value]")
            sys.exit(2)
    elif method == "kgTolb":
        try:
            kg=sys.argv[2]
            result=kgTolb(kg)
            unit='lb'
        except:
            print("python unit_convert.py [method] [value]")
            sys.exit(2)
    print(result,unit)

if __name__ == "__main__":
    main()
