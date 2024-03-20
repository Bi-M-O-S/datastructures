# Q1. Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
#Creating an empty list
numbers = []
# prompting usrer input
number = int(input('give me a number: '))
number1 = int(input('give me another number: '))
number2 = int(input('give me another number: '))
number3 = int(input('give me another number: '))
number4 = int(input('give me another number: '))
number5 = int(input('give me another number: '))
number6 = int(input('give me the last number: '))
#appending the user input numbers to initially created empty list
numbers.append(number)
numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)
numbers.append(number5)
numbers.append(number6)
#generating the list formed
print(numbers)
#summation function
print(sum(numbers))


# Q2. Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
favBooks = {'But how do it know','automatethebotingstuffswithpython', 'Hacking Electronics', 'Learn Arduino','Learn Chinese'}
for book in favBooks:
    print(book)


# Q3. Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
#creating personal info dict
person_info = {}
#collecting user input
person_info['Name'] = input('What is your name? ')
person_info['Age'] = input('How old are you? ')
person_info['FavColor'] = input('What is your favorite color? ')
#printing the dictionary
print(person_info)


#Sets
# empty_set = set()
# empty_set.add(1)
# empty_set.add('Phoebe')
# empty_set.add(5.66)
# empty_set.add(3)
# empty_set.add('Boy')
# empty_set.add(1)

# randomList = ['bicycle', 'demio', 'premio', 'tx', 'audi']
#Updating or appending another list to a set
# empty_set.update(randomList)
#deleting an element from a set
# empty_set.discard('demio')

# random_dict = {'name':'Michael', 'Age':28, 'Nationality':'Kenyan'}
#Updating a dict into set
# empty_set.update(random_dict)
# print(all(empty_set))
# print(any(empty_set))
# print(enumerate(empty_set))
# print(len(empty_set))
#print(max(empty_set))
#print(min(empty_set))
#print(sorted(empty_set))
#print(sum(empty_set))

#Union ; intersection; subtraction and symmetric difference
#Union\ all the elements in A merged with B(Use | or union()).
# set1 = {1,3,5,7}
# set2 = {2,4,6,8}

# print(set1|set2)
# print(set1.union(set2))

#set intersection\ only common elements in A as in B(Use & or intersection()).
# set3 = {1,2,3,4,6,7}
# set4 = {2,4,5,6,7,8}
# print(set3&set4)
# print(set3.intersection(set4))

#set diffeence. Elements in A that are not in B(Use - or difference()).
# print(set3-set4)
# print(set3.difference(set4))

#Set symmetric diference includes all the elements in A and B that are not at the common point(use ^ or symmetric_difference()).
# print (set3 ^ set4)
# print (set3.symmetric_difference(set4))

# Q4. Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
user1numbers = set()
#user inputs
user1numbers.update(set(input('Enter a number: ')))
user1numbers.update(set(input('Enter another number: ')))
user1numbers.update(set(input('Enter another number: ')))
user1numbers.update(set(input('Enter another number: ')))
user1numbers.update(set(input('Enter another number: ')))
user1numbers.update(set(input('Enter another number: ')))
#first set
print(user1numbers)

user2numbers = set()
user2numbers.update(set(input('Enter a number: ')))
user2numbers.update(set(input('Enter another number: ')))
user2numbers.update(set(input('Enter another number: ')))
user2numbers.update(set(input('Enter another number: ')))
user2numbers.update(set(input('Enter another number: ')))
user2numbers.update(set(input('Enter another number: ')))
#second set
print(user2numbers)

#intersection elements
print('Here are the numbers common in both sets you\'ve created')
print(user1numbers|user2numbers)

# Q5. Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

userList = []
userList.append(input('Tell a fruit that you like: '))
userList.append(input('Tell another fruit that you like: '))
userList.append(input('Tell another fruit that you like: '))
userList.append(input('Tell another fruit that you like: '))
userList.append(input('Tell another fruit that you like: '))
userList.append(input('Tell another fruit that you like: '))
userList.append(input('Tell another fruit that you like: '))
print(len(userList))
newList =[]
for item in userList:
    if len(item)%2 != 0:
        newList.append(item)
print('Here is a new list that has items with odd number of characters from your list.')
print(newList) 
