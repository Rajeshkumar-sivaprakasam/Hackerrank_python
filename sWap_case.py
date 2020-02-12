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