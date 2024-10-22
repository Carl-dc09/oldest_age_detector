
# Define valid name (The name must only contain letters, spaces, and period for middle initials and shortened junior and senior)
def valid_name_criteria(name):
    for char in name:
        if not (char.isalpha() or char.isspace() or char in "-'.,"):
            return False
    return True

# Define valid age criteria (The age must be a positive integer between 0 and 122 - the highest age is based on Jeanne Calment, a French woman who passed away at the age of 122 years old in 1997)
def valid_age_criteria(age):
    return age.isdigit() and 0 <= int(age) <= 122

# Find the person with the highest age
def get_oldest_person(people):
    oldest_person = max(people, key=lambda person: person['age'])
    return oldest_person

# Set up an array to store people's information
people_info = []

# Input name and age
while True:
    name = input("Enter a name: ")
    while not valid_name_criteria(name):
        print("Error: Invalid name. Please enter a valid name (letters and spaces only).")
        name = input("Enter name: ")
    
    age = input("Enter age: ")
    while not valid_age_criteria(age):
        print("Error: Invalid age. Please enter a valid age (0 to 122).")
        age = input("Enter age: ")

    # Store the valid entry into the array
    people_info.append({"name": name, "age": int(age)})

    # Ask if the user wants to add another entry
    another_entry = input("Do you want to add another entry? (Yes/No): ").strip().lower()
    if another_entry != 'yes':
        break

# Display the name and age of the oldest person
if people_info:
    oldest_person = get_oldest_person(people_info)
    print(f"The oldest person is {oldest_person["name"]} with the age of {oldest_person["age"]} year(s) old.")
else:
    print("No valid entries were added.")