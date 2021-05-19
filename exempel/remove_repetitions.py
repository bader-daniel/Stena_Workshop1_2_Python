# This is my solution to a task from the first course over at The Python Institute.
# The task was to loop through a list and remove any repetitive elements. 
# Their own solution used a new list to store the new values, while my solution
# updates the current list. Notice the .insert() method which we haven't discussed. 


myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for enum, i in enumerate(myList):
    myList.pop(i)
    if i in myList:
        continue
    myList.insert(enum, i)


print("The list with unique elements only:")
print(myList)

# Walk Through
# 1. Loop through the list with a for loop. i is the current element and enum is the index of the element
# 2. Remove the element from the list using pop(), regardless if it's a duplicate or not
# 3. Check if the element is still in the list after being removed. If it is, do nothing. 
# 4. If the element is not in the list it was not a duplicate, then add it back. 

# Steps 3 and 4 can be done in one step using not in and an inline if, which are short if statements on a single line.  
