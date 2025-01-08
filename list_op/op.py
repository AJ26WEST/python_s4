my_list = [10, 20, 30, 40]
print("Original list:", my_list)

my_list.append(50)
print("After appending 50:", my_list)

my_list.insert(2, 25)
print("After inserting 25 at index 2:", my_list)

my_list.remove(20)
print("After removing 20:", my_list)

my_list.sort(reverse=True)
print("After sorting in descending order:", my_list)

recovered_list = my_list.copy()
print("Recovered list:", recovered_list)
