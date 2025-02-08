def my_atoi(s):
    s = s.strip()  
    if not s:
        return 0

    negative = False
    i = 0
    if s[0] == '-':
        negative = True
        i += 1
    elif s[0] == '+':
        i += 1

    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + (ord(s[i]) - ord('0'))
        i += 1

    if negative:
        result = -result

    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result

s = "  -123abc"
print(my_atoi(s))  
