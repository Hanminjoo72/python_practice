a,b = input().split(", ")

def long(str1,str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        print("==")

print(long(a,b))