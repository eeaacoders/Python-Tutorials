# TUPLE IN PYHTON
# Operations on tuple
tup = ("AB","BC","CD","EF")
temp = list(tup)
temp.append("XY")
print(temp)
temp.pop(1)
temp[2] = "Asia"
tup = tuple(temp)
print(tup)

tup2 = (111,2,3,4,5,6,66,6,6)

print(tup2.count(5),"times.")
print(tup2.count(6),"times")

