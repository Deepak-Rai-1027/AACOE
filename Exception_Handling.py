strNames = ['Deepak', 'RAHUL', 'priya', 'Aryan']

text = 'Deepak'

for i, v in enumerate(strNames):
    if v == text:
        print("The text {} is at index: {}".format(text,strNames.index(v)))

print("The text is not in list.")

try:
    index_value = strNames.index(text)
    print(index_value)
except:
    print("The text is not in the list.")
    
