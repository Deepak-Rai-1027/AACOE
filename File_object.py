ftext = open('C:\\Users\\deepak\\Desktop\\ENBD_AACOE\\Python_Course\\test.txt')

ftext_read = ftext.read()
sText = ftext.read(3)

print(ftext_read)
print(sText)
print(ftext.tell())

ftext.close()
print('File Closed? {}'.format(ftext.closed))
# seek(n)
# tell()
# read(n)

# With statement
print('Started reading the file.')
with open('C:\\Users\\deepak\\Desktop\\ENBD_AACOE\\Python_Course\\test.txt') as ftext2:
    print(ftext2.read())
    print('File Closed? {}'.format(ftext2.closed))

print('Finished reading the file.')
print('File Closed? {}'.format(ftext2.closed))

# Reading all the lines in a file
print('Started reading the file.')
with open('C:\\Users\\deepak\\Desktop\\ENBD_AACOE\\Python_Course\\test2.txt') as ftext3:
    for line in ftext3:
        print(line)

print('Finished reading the file.')
print('File Closed? {}'.format(ftext3.closed))
    
# Removing the white space in the output.
print('Started reading the file.')
print('\n')
with open('C:\\Users\\deepak\\Desktop\\ENBD_AACOE\\Python_Course\\test2.txt') as ftext3:
    for line in ftext3:
        print(line.rstrip())

print('\n')
print('Finished reading the file.')
print('File Closed? {}'.format(ftext3.closed))


# file mode.
print('Started reading the file.')
print('\n')
with open('C:\\Users\\deepak\\Desktop\\ENBD_AACOE\\Python_Course\\test2.txt', 'rt') as ftext3:
    print('File Mode {}'.format(ftext3.mode))
    for line in ftext3:
        print(line.rstrip())

print('\n')
print('Finished reading the file.')
print('File Closed? {}'.format(ftext3.closed))


# Writing text to a file.
print('Opened the file for writing.')
print('\n')
with open('C:\\Users\\deepak\\Desktop\\ENBD_AACOE\\Python_Course\\test2.txt', 'a') as ftext3:
    print('File Mode {}'.format(ftext3.mode))
    ftext3.write('\nThis text will be written to the file.\n')
    ftext3.write('This is another text added at the end.')
    
print('File is written with new text and closed.')   

# Reading the file
print('Started reading the file.')
print('\n')
with open('C:\\Users\\deepak\\Desktop\\ENBD_AACOE\\Python_Course\\test2.txt', 'rt') as ftext3:
    print('File Mode {}'.format(ftext3.mode))
    for line in ftext3:
        print(line.rstrip())

print('\n')
print('Finished reading the file.')
print('File Closed? {}'.format(ftext3.closed))


