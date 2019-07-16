lucky_numbers=[23,56,75,34,5]
friends=["Barshon","Shoily", "Shoily", "Ayon", "Zunayed"]
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends.extend(lucky_numbers)
friends.append("Munif")
friends.insert(4,"Marno")
friends.remove(("Ayon"))
friends.pop()

friends_another=friends.copy()
print(friends_another)



print(friends)
print(friends.index("Barshon"))
print(friends.count("Shoily"))

