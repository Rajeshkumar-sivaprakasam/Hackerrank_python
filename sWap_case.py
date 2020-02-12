"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string .

Constraints


Output Format

Print the modified string .

Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""
def swap_case(s):
    change = ''
    for i in s:
        if i.isupper():
            change += i.lower()
        elif i.islower():
            change += i.upper()
        else:
            change += i
    return change

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)