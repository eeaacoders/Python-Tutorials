# Some times the sytax of while is convineient and some time the synatx of for loop is convienient.
# So our task will be done by both of these loops
# As if we talk about a little come throw of for loop is

for i in range(3):
    print(i)
print("----------")
# Second case from this numebr to this number(0,10);
for i in range(0,5):
    print(i)
print("----------")
# Third case as the increment also added
for i in range(0,10,2):
    print(i)

# While Loop
print("---------------")
i = 0
while(i<=5):
    print(i)
# increment the i
    i = i+1

#--------------------------------

print("Enter the numbers.")
i = 1
while(i <= 5):
    i = int(input("Enter the number: "))
    print(i)
    i = i+1

count = 5
while(count > 0):
    print(count)
    count = count-1

# while loop with the else:

cnt = 5
while(cnt > 0):
    print(cnt)
    cnt = cnt - 1
else:
    print("I am in the else condition.")

# FACTORIAL IN THE WHILE LOOPS

count = 1
fact = 1
num = int(input("Enter the number: "))

while(count <= num):
    fact = fact*count
    count = count+1
else:
    print("The factorial of the number is: ",fact)




