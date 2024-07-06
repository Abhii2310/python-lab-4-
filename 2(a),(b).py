# 2)a.write a python program to display all the prime numbers in the given range .

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start, end = map(int, input("Enter interval (start end): ").split())

print("Prime numbers in the interval are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")



# 2)b.program to create a list with all the subject names and perform following operations 


# List of subject names for the 4th semester
subjects = [
    "Mathematics", 
    "DCN", 
    "FAFL", 
    "DAA", 
    "MC-IOT", 
    "Python Programming Lab", 
    "angular js"
]

# Display the list using a for loop
print("All subjects:")
for subject in subjects:
    print(subject)

# Display 2nd and 5th elements of the list
print("\n2nd and 5th subjects:")
print(subjects[1])  
print(subjects[4])  

# Display first 4 elements of the list using the range of indexes
print("\nFirst 4 subjects:")
print(subjects[:4])  

# Display last 4 elements of the list using the range of negative indexes
print("\nLast 4 subjects:")
print(subjects[-4:])  

# Check if "Python Programming Lab" is available in the list
print("\nCheck if 'Python Programming Lab' is in the list:")
print("Python Programming Lab" in subjects)

# Demonstrate the working of append() and insert() functions
subjects.append("Artificial Intelligence")  
print("\nAfter appending 'Artificial Intelligence':")
print(subjects)

subjects.insert(3, "Machine Learning")  
print("\nAfter inserting 'Machine Learning' at index 3:")
print(subjects)

# Demonstrate the working of remove() and pop() functions
subjects.remove("Software Engineering") 
print("\nAfter removing 'Software Engineering':")
print(subjects)

removed_subject = subjects.pop()  
print(f"\nAfter popping the last element '{removed_subject}':")
print(subjects)



#output 

# All subjects:
# Mathematics
# DCN
# FAFL
# DAA
# MC-IOT
# Python Programming Lab
# angular js

# 2nd and 5th subjects:
# DCN
# MC-IOT

# First 4 subjects:
# ['Mathematics', 'DCN', 'FAFL', 'DAA']

# Last 4 subjects:
# ['DAA', 'MC-IOT', 'Python Programming Lab', 'angular js']

# Check if 'Python Programming Lab' is in the list:
# True

# After appending 'Artificial Intelligence':
# ['Mathematics', 'DCN', 'FAFL', 'DAA', 'MC-IOT', 'Python Programming Lab', 'angular js', 'Artificial Intelligence']

# After inserting 'Machine Learning' at index 3:
# ['Mathematics', 'DCN', 'FAFL', 'Machine Learning', 'DAA', 'MC-IOT', 'Python Programming Lab', 'angular js', 'Artificial Intelligence']
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 44, in <module>
# ValueError: list.remove(x): x not in list



