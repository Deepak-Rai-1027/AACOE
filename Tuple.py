# Tuple

tuple_name = ('Deepak', 'Rahul', 'Priya')

print(tuple_name[0])

# cannot modify values in a tuple
tuple_name[2] = 'Ajay'

for name in tuple_name:
    print(name)

# deleting the tuple    
del tuple_name

print(tuple_name)

# Switching between tuple and list
print('{} is {}.'.format('tuple_name', type(list(tuple_name))))
print('{} is {}.'.format('tuple_name', type(tuple_name)))

# Example
weekend_days = ('Saturday', 'Sunday')

(sat, sun) = weekend_days
print(sat, sun)
