def dial(name, dict_name):
    print('Dial {} to call {}.'.format(dict_name[name], name))
    

contacts = {'Jason': '555-0123', 'Carl': '555-087'}

dial('Jason', contacts)
dial('Carl', contacts)

# adding value in dictionary
contacts['Deepak'] = '555-0570'

dial('Deepak', contacts)

# Removing value from dictionary
del contacts['Deepak']
print(contacts)

print(contacts.keys())
print(contacts.values())
print('555-087' in contacts.values())

# Looping dictionary
for k, v in contacts.items():
    print(k, v)
    
print(len(contacts))
    
