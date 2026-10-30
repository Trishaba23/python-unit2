# Accept two strings
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
 # a) Display strings and their lengths
print("First string:", s1)
print("Second string:", s2)
print("Length of first:",len(s1))
print("Length of second:", len(s2))
 # b) Positive and negative indexing
if s1:
    print("First character:", s1)
if s2:
    print("First character:", s1[0])
print("Last character:", s1[-1])
# c) Extract a substring using slicing
print("Substring:", s1[0:3])
 # d) Repetition and concatenation
print("Repetition:", s1 * 2)
print("Concatenation:", s1 + s2)
# e) Membership
ch = input("Enter character or substring to check: ")
print("Present:", ch in s1)
print("Not present:", ch not in s1)
 # f) Compare strings
print("Equal:", s1 == s2)
print("Not equal:", s1 != s2)
print("First less than second:", s1 < s2)
print("First greater than second:", s1 > s2)
# g) Uppercase and lowercase
print("First uppercase:", s1.upper())
print("First lowercase:", s1.lower())
print("Second uppercase:", s2.upper())
print("Second lowercase:", s2.lower())

