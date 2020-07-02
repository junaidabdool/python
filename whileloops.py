i = 1
while i <= 10:
    print("Hello world")
    i += 1
print("Done with the while loop")

#for loop
print("Trying the for loop")
Tv_Shows = ["Dark", "Breaking Bad", "Mr Robot", "Lucifer", "Elite", "Blacklist", "Mindhunter"]
for x in Tv_Shows:
    print(x)
#Using range
for index in range(len(Tv_Shows)):
    print(Tv_Shows[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:print("Not first iteration")
