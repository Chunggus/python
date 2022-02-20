# 1)User inputs a string, your task is to find how many vowel letters in this string.
# Example:
# Input: Hello world!
# Output: a-0 e-1 i-0 o-2 u-0
#  2)You have a string "P>O>P>U>L>A>R s.u.m.m.e.r s u n g l a s s e s (CATALOG)", your task is to transform it in
# normal look "Popular summer sunglasses catalog"
# tip!(You need to convert a string into list, then make some changes, after which transform it
a = "P>O>P>U>L>A>R s.u.m.m.e.r s u n g l a s s e s (CATALOG)"
a = a.split()
a[0] = a[0].lower()
a[0] = a[0].split(">")
a[1] = a[1].lower()
a[1] = a[1].split(".")
a1 = a[0]
a2 = a[1]
a.pop(0)
a.pop(0)
a[len(a)-1] = a[len(a)-1].lower()
a[len(a)-1] = a[len(a)-1].strip("()")
a4 = a[len(a)-1]
a.remove("catalog")
a1 = "".join(a1)
a2 = "".join(a2)
a = "".join(a)
c = a1 + " " + a2 + " " + a + " " + a4 
print(c)
