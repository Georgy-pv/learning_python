

def parse_command(command: str) -> list:
    parsedlone = command.replace(' ', '')
    res = list(parsedlone)
    # print(res)
    return res

def calc(command: str) -> float:
    print(command)
    precalc = ''.join(parse_command(command))
    res = eval(precalc)
    return res
    

def getfromfile(file_name: str):
    # print(file_name)
    with open(file_name, 'r') as f:
        line = f.readline()
    return line

import sys

print(sys.argv)

if len(sys.argv) <= 1:
    print('if ', sys.argv)
    command = input("some calc: ")
    print(calc(command))
else:
    print('else ', sys.argv)
    filename = sys.argv[1]
    command = getfromfile(filename)
    print(calc(command))
