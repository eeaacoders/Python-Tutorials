students = ("ALI", "Abdul Rehman", "Noman", "Awais", "Hassam", "Ahmed")

temp = list(students)
temp.append("Shabir")
print(temp)
temp.pop(3)
temp[2] = "Aslam"
students = tuple(temp)
print(students)

# WE CAN CHANGE THE TUPLE INTO THE LIST AND THE LIST IN THE TUPLE

tup1 = ("ALI","HASSAN")
tup2 = ("WARIS","MIRZA")
tup3 = tup1 + tup2
print(tup3)

tup4 = (11,2,3,4,5,5,5,5,6,6,7,8)
print(tup4.count(5),"times.")
print(tup4.count(2),"times.")
print(tup4.count(6),"times.")

# INDEX()

tupi = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(tupi.index(6))
# i i want that to iteratre in the selected portion then i can use the starting and ending
# res = tupi.index(3,8,12)
# print(res)