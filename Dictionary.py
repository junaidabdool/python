dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print(dict.get("Name"))# using get
#Updating Dictionary
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School";# Add new entry
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name']# remove entry with key 'Name'
