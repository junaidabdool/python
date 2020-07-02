Tv_Shows = ["Dark", "Breaking Bad", "Mr Robot", "Lucifer", "Elite", "Blacklist", "Mindhunter"]
print(Tv_Shows)
print(Tv_Shows[0])  # access element based on the index
print(Tv_Shows[-1])  # access back of the list
print(Tv_Shows[1:])  # starting with index 1
print(Tv_Shows[3:5])
Tv_Shows[4] = "The Vampire Diaries"  # update list
print(Tv_Shows)
# list function
for x in Tv_Shows: print(x) # iteration
lucky_number = [66, 3, 11, 10]
Tv_Shows.extend(lucky_number) # extend the list
print(Tv_Shows)
Tv_Shows.append("Original")
print(Tv_Shows)
print(len(Tv_Shows))
print(max(lucky_number))
lucky_number.insert(1, 4)
print(lucky_number)
Tv_Shows.remove("Original")
print(Tv_Shows)
lucky_number.pop()
print(lucky_number)
print(Tv_Shows.index("The Vampire Diaries"))
lucky_number.sort()# sort the list
print(lucky_number)
lucky_number2 = lucky_number.copy()
print(lucky_number)
