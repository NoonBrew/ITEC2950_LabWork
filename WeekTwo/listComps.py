# The classes a student is registered for (list)
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list of only ITEC classes
only_itec = [ c for c in classes_registered if c.startswith('ITEC') ]
print(only_itec)

# Record Temperature every day. Record -1 if not possibel to take measurement.
high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

# Make a list of only numbers that represent a valid temperature measurement
only_real_temps = [temp for temp in high_temps if temp != -1]

print(only_real_temps)

# Say you want to convert to Celsius

# Round takes a value and a precison
temp_celsius = [round((temp_f - 32) * 5 / 9, 2) for temp_f in only_real_temps ]
print(temp_celsius)

average = sum(temp_celsius) / len(temp_celsius)

print('The average is {:.2f}'.format(average))

# My turn

number_list = [2, 4, 6]

# Using list comp increase each number by one

add_number_list = [n+1 for n in number_list]
print(add_number_list)

# Filter out all the non-sero numbers
list_with_zeros = [0,3,4,0,22,1]

list_without_zeros = [n for n in list_with_zeros if n != 0]
print(list_without_zeros)

# Get a list with only non-ITEC classes 

class_list = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']

non_itec_list = [c for c in class_list if not c.startswith('ITEC')]
print(non_itec_list)

# Making a list with no zeros and doubling all the non zero numbers

list_to_double = [0,10,4,0,32]

list_doubled = [n*2 for n in list_to_double if n != 0]
print(list_doubled)