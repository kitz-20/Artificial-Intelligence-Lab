'''
ASSIGNMENT 3 : Cripth Arithmetic
PA 17 KETAKI PATIL
BATCH A1
'''
import itertools
import string


def correct_vals(p, puzzle):
    op1, op, op2, e, r = break_puzzle(puzzle.translate(p))

    return eval(op1 + op + op2 + "==" + r)

def break_puzzle(puzzle):
    return tuple(puzzle.upper().split())

def get_unique_letters(puzzle):
    return [i for i in set(''.join(break_puzzle(puzzle))) if i.isalpha()]

def get_starting_letters(puzzle, letters):
    return [i for i in range(len(letters)) if letters[i] == break_puzzle(puzzle)[0][0] or letters[i] == break_puzzle(puzzle)[2][0] or letters[i] == break_puzzle(puzzle)[4][0]]

def get_valid_permutations(puzzle):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = get_unique_letters(puzzle)
    critical_indices = get_starting_letters(puzzle, letters)
    poss_perms = []
    for perm in itertools.permutations(digits, len(letters)):
        flag = 0
        for i in critical_indices:
            if perm[i] == '0':
                flag = 1
                break
        if flag == 0:
            poss_perms.append(perm)
    return poss_perms

def solve(puzzle):
    letters = get_unique_letters(puzzle)
    if len(letters) > 10:
        print("INVALID EQUATION : more than one letter maps to same digit")
        return
    for poss in get_valid_permutations(puzzle):
        p = str.maketrans(''.join(letters), ''.join(poss))
        if correct_vals(p,puzzle):
            answer = dict(zip(letters, poss))
            #print(answer)
            solved_puzzle = puzzle
            for c in answer:
                x = solved_puzzle.replace(c, answer[c])
                solved_puzzle = x
            print(solved_puzzle)

n=1
while(n==1):
    puzzle=input("Enter the equation : ")
    print(puzzle)
    solve(puzzle)
    print("--------------------------------")
    n=int(input("Do you wish to continue : yes=1\n"))


'''
OUT PUT :

PS D:\SEM_9\AI>  d:; cd 'd:\SEM_9\AI'; & 'C:\Users\ketak\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\python.exe' 'c:\Users\ketak\.vscode\extensions\ms-python.python-2021.5.842923320\pythonFiles\lib\python\debugpy\launcher' '52461' '--' 'd:\SEM_9\AI\lab3.py'
Enter the equation : BASE + BALL = GAMES
BASE + BALL = GAMES
7483 + 7455 = 14938
--------------------------------
Do you wish to continue : yes=1
1
Enter the equation : SEND + MORE = MONEY
SEND + MORE = MONEY
9567 + 1085 = 10652
--------------------------------
Do you wish to continue : yes=1
1
Enter the equation : CROSS + ROADS = DANGER
CROSS + ROADS = DANGER
96233 + 62513 = 158746
--------------------------------
Do you wish to continue : yes=1
1
Enter the equation : RED + BLUE = COLOR 
RED + BLUE = COLOR
--------------------------------
Do you wish to continue : yes=1
1
Enter the equation : ABC + XYZ = LETTERS
ABC + XYZ = LETTERS
INVALID EQUATION : more than one letter maps to same digit
--------------------------------
Do you wish to continue : yes=1
0

'''