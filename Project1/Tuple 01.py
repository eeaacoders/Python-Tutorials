tup = (1,2,3,4)
print(tup)
print(type(tup),tup)

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(len(tup))
print(tup[-1])
print(tup[len(tup)-1])
print(tup[0:])   # Right side py len(tup) lga do
print(tup[:4])   # left side py 0 lga do

tup2 = (1,2,3,4,"Mai Hon na",False)

if False in tup2:
    print("Present Sir!")
else:
    print("no present sir")

tup3 = tup[1:3]
print(tup3)
#  It will make a new tuple not changed the already existing tuple
