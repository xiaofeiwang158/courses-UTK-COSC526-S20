# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:15:38 2020

@author: xwang158
"""

def parse_delimited_file(filename, delimiter=","):
    # Open and read in all lines of the file
    # (I do not recommend readlines for LARGE files)
    # `open`: ref [1]
    # `readlines`: ref [2]
    with open(filename, 'r', encoding='utf8') as dsvfile:
        lines = dsvfile.readlines()
    # Strip off the newline from the end of each line
    # HINT: ref [3]
        lines = [i.rstrip('\n') for i in lines]
    # Using list comprehension is the recommended pythonic way to iterate through lists
    # HINT: ref [4]
        
        
    # Split each line based on the delimiter (which, in this case, is the comma)
    # HINT: ref [5]
        lines = [i.split(',') for i in lines]
    # Separate the header from the data
    # HINT: ref [6]
        header = lines[0]
        data = lines[1:len(lines)]
    # Find "age" within the header
    # (i.e., calculating the column index for "age")
    # HINT: ref [7]
        age_index = header.index('age')
    # Calculate the number of data rows and columns
    # HINT: [8]
        num_data_rows = len(data)
        num_data_cols = len(header)
        
    # Sum the "age" values
    # HINT: ref [9]
        age = [x[age_index] for x in data]
        age = [int(i) for i in age]
        age_sum = sum(age)
        
    # Calculate the average age
        ave_age = age_sum/num_data_rows
    
    # Print the results
    # `format`: ref [10]
    print("Number of rows of data: {}".format(num_data_rows))
    print("Number of cols: {}".format(num_data_cols))
    print("Average Age: {}".format(ave_age))
    
# Parse the provided csv file
parse_delimited_file('data.csv')


translit_dict = {
    "ä" : "ae",
    "ö" : "oe",
    "ü" : "ue",
    "Ä" : "Ae",
    "Ö" : "Oe",
    "Ü" : "Ue", 
    "ł" : "l",
    "ō" : "o",
}
#print(translit_dict['ä'])
with open("data.csv", 'r', encoding='utf8') as csvfile:
    lines = csvfile.readlines()
# Strip off the newline from the end of each line
    #lines = [i.rstrip('\n') for i in lines]
    lines = [i.rstrip('\n') for i in lines]
    
# Split each line based on the delimiter (which, in this case, is the comma)
    lines = [i.split(',') for i in lines]
    
# Separate the header from the data
    header = lines[0]
    data = lines[1:len(lines)]

# Find "name" within the header
    name_index = header.index('name')
    #print(name_index)
# Extract the names from the rows
unicode_names = [x[name_index] for x in data]

# Iterate over the names
translit_names = []
for unicode_name in unicode_names:
    # Perform the replacements in the translit_dict
    # HINT: ref [1]
    translit_names.append(unicode_name)
    for i in unicode_name:
        if i in translit_dict:
            unicode_name = unicode_name.replace(i, translit_dict[i])
            translit_names[-1] = unicode_name
    False

# Write out the names to a file named "data-ascii.txt"
# HINT: ref [2]
f = open('data-ascii.txt', 'w')
for i in translit_names:
    f.write(i)
    f.write('\n')
f.close

# Verify that the names were converted and written out correctly
with open("data-ascii.txt", 'r') as infile:
    for line in infile:
        print(line.rstrip())
        
import itertools
import functools

def square(x):
    return x**2
list(map(square, [1,2,3,4,5]))

print(list(map(square, [1,2,3,4,5])))

def add(x,y):
    return x + y
a = [1,2,3,4,5]
functools.reduce(add,a)


















