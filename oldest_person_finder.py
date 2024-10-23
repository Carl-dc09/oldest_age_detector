
# Define a valid name (The name must only contain letters, spaces, and period for middle initials and shortened junior and senior)
def valid_name_criteria(name):
    return name.replace(" ", "").isalpha()

# Define a valid age criteria (The age must be a positive integer between 0 and 122 - the highest age is based on Jeanne Calment, a French woman who passed away at the age of 122 years old in 1997)
def valid_age_criteria(age):
    return age.isdigit() and 0 <= int(age) <= 122

# Find the person with the highest age
def get_oldest_person(people_info):
    if not people_info:
        return []

    
    # Find the highest or maximum age
    highest_age = max(old_person["age"] for old_person in people_info)

    # Collect all people with the highest age
    oldest_people = [old_person for old_person in people_info if old_person["age"] == highest_age]
    
    return oldest_people

# Set up an array to store people's information
people_info = []

# Input name and age
while True:
    name = input("Enter a name: ")
    while not valid_name_criteria(name):
        print("Error: Invalid name. Please enter a valid name (letters and spaces only).")
        name = input("Enter a name: ")
    
    age = input("Enter age: ")
    while not valid_age_criteria(age):
        print("Error: Invalid age. Please enter a valid age (0 to 122).")
        age = input("Enter age: ")

    # Store the valid entry into the array
    people_info.append({"name": name, "age": int(age)})

    while True:
    # Ask if the user wants to add another entry
        another_entry = input("Do you want to add another entry? (Yes/No): ").strip().lower() # The strip is to remove any spaces in the input, while the lower is to make the inputs case insensitive
        if another_entry in {"Yes", "yes"}:
            break
        elif another_entry in {"No", "no"}:
            print("Thank you for your entries.")
            break
        else:
            print("Error: Only respond with 'Yes' or 'No'.")
    if another_entry in {"No", "no"}:
        break
# Find the name and age of the oldest person
