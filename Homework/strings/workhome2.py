# 1)User inputs a string, your task is to find how many vowel letters in this string.
# Example:
# Input: Hello world!
# Output: a-0 e-1 i-0 o-2 u-0
a = input()
a = list(a)
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for i in range(len(a)):
    if a[i] == "a":
        f1 = f1+1
    if a[i] == "e":
        f2 = f2+1
    if a[i] == "i":
        f3 = f3+1
    if a[i] == "o":
        f4 = f4+1
    if a[i] == "u":
        f5 = f5+1
    if a[i] == "y":
        f6 = f6+1
print(f1, "letters a")
print(f2, "letters e")
print(f3, "letters i")
print(f4, "letters o")
print(f5, "letters u")
print(f6, "letters y")