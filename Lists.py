# Lists
animals = ['man', 'bear', 'pig', 'lion']
num = [2, 4, 6, 8]

# user defined function to print the elements of a list
def print_list(lst):
    for i in range(len(lst)):
        print(lst[i])
    

# negative index
rev = [-1, -3, -2, -4]

for i in rev:
    print(animals[i])
    
# append method
animals.append('Cow')

print_list(animals)

print_list(num)

num.append(10)
print_list(num)

# extend method
num.extend([12, 14, 16, 18, 20])

print_list(num)

# adding element at specific index
num.insert(1, 'test')
print_list(num)

# Slicing
num[1:4]
num[:4]
num[4:]

# Example
num = int(input("Enter a numner"))
lstEven = list()

for i in range(1, num + 1):
    if i % 2 == 0:
        lstEven.append(i)
        
print("List of even numbers from 1 to {}".format(num))
print_list(lstEven)


# String slices
name = "Deepak"

print(name[0:4])







