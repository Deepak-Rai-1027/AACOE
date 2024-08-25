# Strings

# Exercise 1:
animal = 'cat'
vegetable = 'broccoli'
mineral = 'gold'

print("Here is an animal, a vegetable, and a mineral.")
print(animal)
print(vegetable)
print(mineral)

# Exercise 2:
sText = input("Please type something and press enter: ")
print("You entered:")
print(sText)

# Exercise 3:
# Get the input from the user.
text  = input("What word you like the cat to say")

# Determine the length of the input.
text_length = len(text)

# Make the border of the same size as the input.
print('            {}'.format('_' * text_length))
print('          < {} >'.format(text))
print('            {}'.format('-' * text_length))
print('          /')
print(' /\_/\   /')
print('( o.o )')
print(' > ^ <')


# Numbers

# Exercise 1:
# Cost of one server per hour
charges_hrs = 0.51

print('How much does it cost($) to operate one server per day? : {:.2f}'
      .format(charges_hrs*24))

print('How much does it cost($) to operate one server per month? : {:.2f}'
      .format(charges_hrs*24*30))

# Exercise 2:
# Budget available
budget = 918

# Cost of the one server per hour
charges_hrs = 0.51

print('How much does it cost($) to operate one server per day? : ${:.2f}'
      .format(charges_hrs*24))

print('How much does it cost($) to operate one server per month? : ${:.2f}'
      .format(charges_hrs*24*30))

print('How much does it cost($) to operate twenty servers per day? : ${:.2f}'
      .format(charges_hrs*24*20))

print('How much does it cost($) to operate twenty servers per month? : ${:.2f}'
      .format(charges_hrs*24*30*20))

print('How many days can I operate one server with ${:.2f}? : {:.2f} days'
      .format(budget, (budget / (charges_hrs*24))))
      

# Booleans and Conditionals

# Exercise 1:
# Ask for distance from user
intTravel_miles = int(input("How far you want to travel in miles?"))

if intTravel_miles > 0 and intTravel_miles <= 3:
      mode_of_transport = 'walk'
elif intTravel_miles > 3 and intTravel_miles < 300:
      mode_of_transport = 'drive'
elif intTravel_miles >= 300:
      mode_of_transport = 'fly'
else:
      print("Please enter a valid number!")
      
print("You may {} for {} miles.".format(mode_of_transport, intTravel_miles)) 

# List
# Exercise 1:

to_do = list()
index = 0 
done = False

while not done:
      text = input("Enter a task for your to-do list. Enter blank once done.")
      if len(text) == 0:
            done = True
      else:
            to_do.append(text)
            print('Task added.')
            
print()
print('Your to-do list:')
print('-' * 16)
for task in to_do:
      print(task)      
      

