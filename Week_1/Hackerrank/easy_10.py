def swap_case(s):
    somestring = ""
    for item in s:
        if item.isupper():
            somestring += item.lower()
        else:
            somestring += item.upper()
    return somestring
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)