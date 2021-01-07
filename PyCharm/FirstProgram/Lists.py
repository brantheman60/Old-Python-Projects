lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
print(friends[1])
print(friends[-1])
print(friends[2:])
print(friends[2:4])

friends[1] = "Mike"
print(friends[1])

friends.append("Creed")
friends.extend("Harry")
friends.extend(lucky_numbers)
print(friends)

friends.clear()
friends.append("Jack")
friends.append("Paul")
friends.insert(1,"Henry")
friends.remove("Paul")
print(friends)
print(friends.index("Henry"))

new_friends = friends.copy()
new_friends.append("Karen")
new_friends.append("Isabelle")
new_friends.append("Michael")
new_friends.pop()
print(new_friends)
new_friends.sort()
print(new_friends)
new_friends.reverse()
print(new_friends)

