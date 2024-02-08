# WAP to check Palindrom in python

def palindrom_check(string):
    start, end = 0, len(string)-1
    while start < end:
        if string[start] != string[end]:
            return False
        start, end = start + 1, end -1
    return True

print(palindrom_check("hello"))