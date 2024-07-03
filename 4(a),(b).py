# Initialize the dictionary
passwd = {'rahul': 'genius', 'kumar': 'smart', 'ankita': 'intelligent'}

# Function to print all items in the dictionary
def print_all_items():
    print("All items:", passwd)

# Function to print all keys in the dictionary
def print_all_keys():
    print("All keys:", passwd.keys())

# Function to print all values in the dictionary
def print_all_values():
    print("All values:", passwd.values())

# Function to get the password of a user
def get_password(user):
    return f"Password of {user}: {passwd.get(user, 'User not found')}"

# Function to change the password of a particular user
def change_password(user, new_password):
    if user in passwd:
        passwd[user] = new_password
        print(f"Password for {user} changed to: {new_password}")
    else:
        print(f"User {user} not found.")

# Main program to demonstrate the functions
if __name__ == "__main__":
    print_all_items()
    print_all_keys()
    print_all_values()
    print(get_password('rahul'))
    change_password('ankita', 'brilliant')
    print_all_items()