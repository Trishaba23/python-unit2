import array
# Create an integer array with eight elements
a = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80])
print("Array:", a.tolist())
# a) Indexing and slicing
print("First element:", a[0])
print("Last element:", a[-1])
print("Slicing:", a[2:5].tolist())
# b) Insert an element at a specified position
pos = int(input("Enter insertion position (0 to length): "))
value = int(input("Enter value to insert: "))
if 0 <= pos <= len(a):
    a.insert(pos, value)
    print("After insert:", a.tolist())
else:
    print("Invalid position")
# c) Remove a specified element and pop the last element
value = int(input("Enter element to remove: "))
if value in a:
       a.remove(value)
       print("After remove:", a.tolist())
else:
      print("Element not found")

if len(a) > 0:
     a.pop()
     print("After pop:", a.tolist())
 # d) Search for an element and display its index
value = int(input("Enter element to search: "))
if value in a:
    print("Index:", a.index(value))
else:
    print("Element not found")
# e) Membership operators
value = int(input("Enter value to check: "))
print("Present:", value in a)
print("Not present:", value not in a)
# f) Maximum, minimum and length
if len(a) > 0:
    print("Maximum:", max(a))
    print("Minimum:", min(a))
    print("Length:", len(a))
# g) Reverse the array
a.reverse()
print("Reversed array:", a.tolist())