s="arjun"

def reverse(f, l):
    if f >= l:
        return s
    s.replace(s[f],s[l])
    return reverse(f + 1, l - 1)

print(reverse(0, len(s) - 1))
