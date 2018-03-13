''' Lists Exercise 2: Working list '''

# Make a list that includes four careers, such as 'programmer', 'truck driver', etc....

work_list = ['programmer','truck driver','teacher','scientist']
# Use the list.index() function to find the index of one career in your list.
print(work_list.index('teacher'))

# Use the in function to show that this career is in your list.
print('teacher' in work_list)

# Use the append() function to add a new career to your list.
work_list.append('doctor')

# Use the insert() function to add a new career at the beginning of the list.
work_list.insert(0,'nurse')

# Use a loop to show all the careers in your list.
for x in work_list:
    print(x)
