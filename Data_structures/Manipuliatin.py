# my_list = [10, 20, 30, 40, 50, 60, 70, 80,]
# my_list.remove(70)
# print(my_list)


# student_score={'ALice' : 80, 'Frank' : 85, 'Jayvian' : 90}
# print(student_score.get('Frank'))

# Define a dictionary
student_ages = {
    "Alice": 14,
    "Bob": 15,
    "Charlie": 13
}

# Get all the keys
values = student_ages.values()

print(values)  # Output: dict_keys(['Alice', 'Bob', 'Charlie'])

# You can also loop through the keys
for name in student_ages.values():
    print(name)
