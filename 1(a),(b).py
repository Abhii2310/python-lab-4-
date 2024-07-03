# 1)a.Basic Arithmetic Operations:

a, b = map(int, input("Enter two numbers: ").split())
op = int(input("1-Add, 2-Subtract, 3-Multiply, 4-Divide: "))

if op == 1:
    result = a + b
    print(f"Addition: {result}")
elif op == 2:
    result = a - b
    print(f"Subtraction: {result}")
elif op == 3:
    result = a * b
    print(f"Multiplication: {result}")
elif op == 4:
    if b != 0:
        result = a / b
        print(f"Division: {result}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid choice")


# 2)b.write a python program to create a list of tuples having first element as the strings and the second element as the length of the string .output the list of tuples sorted based on the length of the string 

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Create a list of tuples (string, length of string)
tuples_list = [(s, len(s)) for s in strings]

# Sort the list of tuples based on the length of the string
sorted_tuples_list = sorted(tuples_list, key=lambda x: x[1])

print(sorted_tuples_list)

#output : [('fig', 3), ('date', 4), ('apple', 5), ('grape', 5), ('banana', 6), ('cherry', 6), ('elderberry', 10)]






