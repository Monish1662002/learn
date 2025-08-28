# Explanation: Executes the block only if the condition is True.

# Common Errors:

# IndentationError – Forgetting indentation
x=10
if x > 5:
#print("x is greater than 5")  # Wrong


#SyntaxError – Missing colon

#if x > 5
    print("x is greater than 5")  # Wrong

#2. if-else Statement
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")


#Explanation: else runs when the if condition is False.

#Common Errors:

#Misaligned indentation for else block

#Forgetting the colon after else

#3. if-elif-else Statement
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is 5 or less")


#Explanation: elif (else if) checks additional conditions when if is False.

#Common Errors:

#Writing elseif instead of elif

#Incorrect indentation or missing colons

#4. for Loop
for i in range(5):
    print(i)


#Explanation: Loops through values from 0 to 4 (excluding 5).

#Common Errors:

#Using range incorrectly (e.g., range[5] instead of range(5))

#Indentation errors

#5. while Loop
count = 0
while count < 5:
    print(count)
    count += 1


#Explanation: Loops until the condition becomes False.

#Common Errors:

#Infinite loop if condition never becomes False

#Forgetting count += 1

#6. break Statement
for i in range(10):
    if i == 5:
        break
    print(i)


#Explanation: Exits loop when i == 5.

#7. continue Statement
for i in range(5):
    if i == 2:
        continue
    print(i)


#Explanation: Skips iteration when i == 2 and continues loop.

#8. pass Statement
for i in range(3):
    pass


#Explanation: Does nothing, acts as a placeholder.
#9. Range Function
range() #allows you to generate a series of Numbers
#3 parameters
#1. Start   
#2. End
#3. Jump    
#default start is 0
#default jump is 1 when range is used with single parameter it is considered as end
list1 = list(range(5))  # [0, 1, 2, 3, 4]
list2 = list(range(2, 7))  # [2, 3, 4, 5, 6]
list3 = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]
list4 = list(range(10, 1, 1))  # []
#when start is greater than end and jump is positive it will return empty list  
list5 = list(range(10, 1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]
#when start is greater than end and jump is negative it will return list in decreasing order
print(list1)    
print(list2)
print(list3)