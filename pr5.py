# Accept a sentence
s = input("Enter a sentence: ")
# Remove leading and trailing spaces
print("lstrip:", s.lstrip())
print("rstrip:", s.rstrip())
print("strip:", s.strip())
# a) Search for a substring using find() and index()
word = input("Enter substring to search: ")
print("find():", s.find(word))
try:
    print("index():",s.index(word))
except ValueError:
    print("Substring not found")
    # b) Count occurrences of a specified word
word = input("Enter word to count: ")
print("Occurrences:", s.count(word))
# c) Replace a word or character
old = input("Enter word/character to replace: ")
new = input("Enter replacement: ")
print("Replaced sentence:", s.replace(old, new))
# d) Split into words and join them
words = s.split()
print("Words:", words)
print("Joined:", "-".join(words))
# e) Demonstrate string immutability
try:
     s[0] = "A"
except(TypeError, IndexError):
    print("Cannot modify a string character by indexing.")
print("Strings are immutable in Python.")
# f) Sort words alphabetically print("Sorted words:", sorted(words))