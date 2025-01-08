input_string = input("Enter a string: ")
print("The entered string is:", input_string)

print("\nUsing range() to iterate through the string:")
for i in range(len(input_string)):
    print(f"Index {i}: {input_string[i]}")

print("\nUsing enumerate() to iterate through the string:")
for index, char in enumerate(input_string):
    print(f"Index {index}: {char}")
